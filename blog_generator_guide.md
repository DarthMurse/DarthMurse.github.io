# Using the Blog Generator

This guide explains how to use the included `blog_generator.py` script to automatically convert Markdown blog posts to HTML and update your blog listing page.

## Prerequisites

The script requires Python 3 and the following packages:
- markdown
- beautifulsoup4

Install these packages using pip:

```bash
pip install markdown beautifulsoup4
```

## Writing a Markdown Blog Post

1. Create a new Markdown file for your blog post (e.g., `my-new-post.md`)

2. Add frontmatter at the top of your file with the following format:

```markdown
---
title: Your Blog Post Title
date: 2025-07-18
category: Your Category
readTime: 10 min read
tags: Tag1, Tag2, Tag3
excerpt: A brief summary of your blog post that will appear on the blog listing page.
---
```

3. Write your blog content in Markdown format. You can include:
   - Headings (# Heading)
   - Lists (- item)
   - Links [text](url)
   - Images ![alt](image.jpg)
   - Code blocks (```python)
   - Math formulas using LaTeX ($E=mc^2$ or $$\int f(x) dx$$)

4. Save your markdown file with a `.md` extension

## Converting Your Blog Post

Run the blog generator script with your markdown file as an argument:

```bash
python blog_generator.py path/to/your/post.md
```

You can also specify a custom slug (URL) for your blog post:

```bash
python blog_generator.py path/to/your/post.md custom-url-slug
```

## What the Script Does

1. Parses your Markdown file and extracts frontmatter metadata
2. Creates a new directory for your blog post with the appropriate slug
3. Converts your Markdown content to HTML
4. Inserts the HTML into a blog post template
5. Copies any local images referenced in your post
6. Updates the blog listing page (`blog.html`) with your new post

## After Running the Script

After running the script, you should:

1. Add a featured image for your blog post:
   - Create or find an image
   - Save it as `featured.jpg` in your blog post directory (e.g., `/blog/your-post-slug/featured.jpg`)

2. Test your site locally by opening `index.html` in a web browser

3. Commit and push your changes to GitHub to publish your blog post

## Example

```bash
python blog_generator.py example-blog-post.md python-data-science
```

This will:
- Convert `example-blog-post.md` to HTML
- Create a directory at `/blog/python-data-science/`
- Save the HTML as `/blog/python-data-science/index.html`
- Update `blog.html` with a new card for this post
- Use the title, date, category, and excerpt from the frontmatter
- Copy any images referenced in the blog post

## Customizing Templates

If you want to change the look of your blog posts:

1. Edit the template in `/blog/template/index.html`
2. Run the script again to apply your changes

## Troubleshooting

- **Error: No module named 'markdown'**: Install the markdown package using `pip install markdown`
- **Error: No module named 'bs4'**: Install Beautiful Soup using `pip install beautifulsoup4`
- **Missing images**: Ensure image paths in your markdown are correct and relative to the markdown file
- **Featured image not showing**: Add a `featured.jpg` file to your blog post directory

## Additional Tips

- Use meaningful, descriptive file names for your markdown posts
- Include relevant tags to categorize your posts
- Write a compelling excerpt to attract readers
- Test your posts locally before publishing
- Add high-quality images to make your posts more engaging
