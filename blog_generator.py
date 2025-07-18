#!/usr/bin/env python3
"""
Blog Post Generator

This script converts Markdown blog posts to HTML and updates the blog listing page.
Usage: python blog_generator.py path/to/your/markdown_file.md
"""

import os
import sys
import re
import shutil
import datetime
from pathlib import Path
import markdown
from bs4 import BeautifulSoup

# Configuration
BLOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "blog"))
BLOG_HTML_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "blog.html"))
TEMPLATE_DIR = os.path.join(BLOG_DIR, "template")
TEMPLATE_PATH = os.path.join(TEMPLATE_DIR, "index.html")

def parse_markdown_frontmatter(md_content):
    """Extract frontmatter from markdown content"""
    frontmatter = {}
    # Check if the content starts with frontmatter
    if md_content.startswith("---"):
        # Find the second occurrence of "---"
        end_idx = md_content.find("---", 3)
        if end_idx != -1:
            # Extract the frontmatter content
            frontmatter_content = md_content[3:end_idx].strip()
            
            # Parse the frontmatter
            for line in frontmatter_content.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    frontmatter[key.strip()] = value.strip()
            
            # Remove frontmatter from content
            content = md_content[end_idx + 3:].strip()
            return frontmatter, content
    
    # If no frontmatter is found or it's not properly formatted
    return frontmatter, md_content

def convert_markdown_to_html(markdown_content):
    """Convert markdown to HTML with extensions for code highlighting and LaTeX"""
    # Set up markdown extensions
    extensions = [
        'markdown.extensions.fenced_code',  # For code blocks
        'markdown.extensions.tables',       # For tables
        'markdown.extensions.toc',          # For table of contents
        'markdown.extensions.attr_list',    # For attributes
        'markdown.extensions.smarty',       # For smart quotes
    ]
    
    # Convert markdown to HTML
    html = markdown.markdown(markdown_content, extensions=extensions)
    return html

def create_blog_post_directory(post_slug, title=None):
    """Create a new directory for a blog post"""
    post_dir = os.path.join(BLOG_DIR, post_slug)
    
    # Check if directory exists, create if not
    if not os.path.exists(post_dir):
        os.makedirs(post_dir)
        print(f"Created directory: {post_dir}")
    
    return post_dir

def get_image_paths_from_markdown(markdown_content):
    """Extract image paths from markdown content"""
    # Find all image references in the markdown content
    image_paths = []
    pattern = r'!\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, markdown_content)
    
    for match in matches:
        image_path = match[1]
        if "http" not in image_path and "://" not in image_path:  # Skip external URLs
            image_paths.append(image_path)
    
    return image_paths

def copy_markdown_images(markdown_path, post_dir, markdown_content):
    """Copy images referenced in the markdown to the post directory"""
    image_paths = get_image_paths_from_markdown(markdown_content)
    
    for image_path in image_paths:
        # Get the absolute path of the image relative to the markdown file
        md_dir = os.path.dirname(markdown_path)
        abs_image_path = os.path.abspath(os.path.join(md_dir, image_path))
        
        if os.path.exists(abs_image_path):
            # Copy the image to the post directory
            dest_path = os.path.join(post_dir, os.path.basename(image_path))
            shutil.copy2(abs_image_path, dest_path)
            print(f"Copied image: {abs_image_path} -> {dest_path}")
        else:
            print(f"Warning: Image not found: {abs_image_path}")

def generate_blog_post(markdown_path, post_slug=None):
    """Generate a blog post from a markdown file"""
    # Read the markdown file
    with open(markdown_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Parse frontmatter
    frontmatter, content = parse_markdown_frontmatter(markdown_content)
    
    # Extract title from frontmatter or first heading
    title = frontmatter.get('title')
    if not title:
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
        else:
            title = os.path.splitext(os.path.basename(markdown_path))[0].replace('-', ' ').title()
    
    # Get or generate post slug
    if not post_slug:
        post_slug = frontmatter.get('slug')
        if not post_slug:
            post_slug = title.lower().replace(' ', '-')
            # Remove special characters
            post_slug = re.sub(r'[^a-z0-9-]', '', post_slug)
    
    # Create the blog post directory
    post_dir = create_blog_post_directory(post_slug)
    
    # Copy images from markdown to the post directory
    copy_markdown_images(markdown_path, post_dir, content)
    
    # Read the template
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Create BeautifulSoup object for easier HTML manipulation
    soup = BeautifulSoup(template_content, 'html.parser')
    
    # Update title
    if soup.title:
        soup.title.string = f"{title} - Your Name"
    
    # Update blog post title
    blog_title = soup.select_one('.blog-post-title')
    if blog_title:
        blog_title.string = title
    
    # Update metadata
    blog_meta = soup.select_one('.blog-post-meta')
    if blog_meta:
        date_str = frontmatter.get('date', datetime.datetime.now().strftime("%Y-%m-%d"))
        category = frontmatter.get('category', 'Uncategorized')
        read_time = frontmatter.get('readTime', '5 min read')
        
        blog_meta.clear()
        blog_meta.append(f"{date_str} • {category} • {read_time}")
    
    # Convert markdown to HTML
    html_content = convert_markdown_to_html(content)
    
    # Update blog post content
    blog_content = soup.select_one('.blog-post-content')
    if blog_content:
        # Keep any existing images at the top
        existing_images = blog_content.select('img:first-child')
        
        # Clear the content div
        blog_content.clear()
        
        # If there was a featured image, add it back
        for img in existing_images:
            blog_content.append(img)
        
        # Insert the new HTML content
        new_content = BeautifulSoup(html_content, 'html.parser')
        for element in new_content:
            blog_content.append(element)
    
    # Write the updated HTML to the blog post directory
    output_path = os.path.join(post_dir, 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f"Generated blog post: {output_path}")
    return {
        'title': title,
        'slug': post_slug,
        'date': frontmatter.get('date', datetime.datetime.now().strftime("%Y-%m-%d")),
        'category': frontmatter.get('category', 'Uncategorized'),
        'excerpt': frontmatter.get('excerpt', content[:200] + '...'),
        'tags': frontmatter.get('tags', '').split(',') if frontmatter.get('tags') else []
    }

def update_blog_listing(blog_info):
    """Update the blog.html file with the new blog post"""
    # Read the blog.html file
    with open(BLOG_HTML_PATH, 'r', encoding='utf-8') as f:
        blog_html = f.read()
    
    soup = BeautifulSoup(blog_html, 'html.parser')
    
    # Find the blog grid
    blog_grid = soup.select_one('.blog-grid')
    if not blog_grid:
        print("Error: Could not find .blog-grid in blog.html")
        return
    
    # Create new blog card
    new_card = soup.new_tag('article', **{'class': 'blog-card'})
    new_card['onclick'] = f"location.href='blog/{blog_info['slug']}/index.html'"
    
    # Blog image
    blog_image_div = soup.new_tag('div', **{'class': 'blog-image'})
    img = soup.new_tag('img', src=f"blog/{blog_info['slug']}/featured.jpg", alt=blog_info['title'])
    blog_image_div.append(img)
    new_card.append(blog_image_div)
    
    # Blog content
    blog_content_div = soup.new_tag('div', **{'class': 'blog-content'})
    
    # Meta info
    blog_meta_div = soup.new_tag('div', **{'class': 'blog-meta'})
    blog_date = soup.new_tag('span', **{'class': 'blog-date'})
    blog_date.string = blog_info['date']
    blog_category = soup.new_tag('span', **{'class': 'blog-category'})
    blog_category.string = blog_info['category']
    blog_meta_div.append(blog_date)
    blog_meta_div.append(blog_category)
    blog_content_div.append(blog_meta_div)
    
    # Title
    blog_title = soup.new_tag('h2', **{'class': 'blog-title'})
    blog_title.string = blog_info['title']
    blog_content_div.append(blog_title)
    
    # Excerpt
    blog_excerpt = soup.new_tag('p', **{'class': 'blog-excerpt'})
    blog_excerpt.string = blog_info['excerpt']
    blog_content_div.append(blog_excerpt)
    
    # Tags
    if blog_info['tags']:
        tags_div = soup.new_tag('div', **{'class': 'blog-tags'})
        for tag in blog_info['tags']:
            tag_span = soup.new_tag('span', **{'class': 'tag'})
            tag_span.string = tag.strip()
            tags_div.append(tag_span)
        blog_content_div.append(tags_div)
    
    new_card.append(blog_content_div)
    
    # Insert the new card at the beginning
    if blog_grid.contents:
        blog_grid.insert(0, new_card)
    else:
        blog_grid.append(new_card)
    
    # Write the updated HTML back to the file
    with open(BLOG_HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f"Updated blog listing: {BLOG_HTML_PATH}")

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python blog_generator.py path/to/your/markdown_file.md [custom-slug]")
        return
    
    markdown_path = sys.argv[1]
    custom_slug = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not os.path.exists(markdown_path):
        print(f"Error: File not found: {markdown_path}")
        return
    
    # Generate the blog post
    blog_info = generate_blog_post(markdown_path, custom_slug)
    
    # Update the blog listing
    update_blog_listing(blog_info)
    
    print("\nBlog post generation complete!")
    print(f"Title: {blog_info['title']}")
    print(f"URL: blog/{blog_info['slug']}/index.html")
    print("\nPlease remember to:")
    print("1. Add a featured.jpg image in the blog post directory")
    print("2. Review and customize the generated HTML if needed")

if __name__ == "__main__":
    main()
