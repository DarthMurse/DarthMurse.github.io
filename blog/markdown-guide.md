# How to Create Blog Posts in Markdown

This guide explains how to create blog posts in Markdown format and convert them to HTML for your personal website.

## Why Markdown?

Markdown is a lightweight markup language that's easy to write and read. It allows you to focus on content while maintaining formatting, and it supports embedding HTML when needed for more complex elements.

## Markdown Blog Post Template

Create a new file named `post.md` in your blog post folder (e.g., `/blog/your-post-name/post.md`):

```markdown
---
title: Your Blog Post Title
date: 2025-07-18
category: Category Name
readTime: 10 min read
---

# Your Blog Post Title

Introduction paragraph. Provide an overview of what the post is about.

## First Main Heading

Content for the first section.

![Image Description](image-name.jpg)

- List item one
- List item two
- List item three

## Second Main Heading

Content for the second section.

You can include inline math like $E=mc^2$ or display equations:

$$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$$

### Subheading

More detailed content.

```python
def hello_world():
    print("Hello, World!")
    
hello_world()
```

## Conclusion

Summarize the key points of your blog post.

---

**Related Posts:** You can link to other related blog posts here.
```

## Converting Markdown to HTML

### Option 1: Using a Markdown Plugin (Recommended)

1. Install a Markdown converter like `markdown-it`:
   ```bash
   npm install -g markdown-it
   ```

2. Convert your Markdown to HTML:
   ```bash
   markdown-it post.md > content.html
   ```

3. Copy the content from `content.html` into the `blog-post-content` div in the blog post template.

### Option 2: Using Online Tools

Several online tools can convert Markdown to HTML:
- [Dillinger](https://dillinger.io/)
- [StackEdit](https://stackedit.io/)
- [Markdown Editor](https://jbt.github.io/markdown-editor/)

### Option 3: Using Visual Studio Code

1. Open your Markdown file in VS Code
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
3. Type "Markdown" and select "Markdown: Preview"
4. Right-click in the preview and select "Copy HTML"
5. Paste into your blog post template

## Creating a New Blog Post

1. Create a new folder in the `/blog/` directory with your post name (use hyphens for spaces)
2. Copy the template from `/blog/template/index.html` to your new folder
3. Write your post in Markdown format
4. Convert your Markdown to HTML and paste it into the template
5. Add your featured image and other resources
6. Update `blog.html` to include your new blog post in the listing

## Markdown Formatting Reference

### Basic Formatting

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*
~~Strikethrough~~

[Link text](https://example.com)

> Blockquote text

Horizontal rule:
---
```

### Lists

```markdown
- Unordered item 1
- Unordered item 2
  - Nested item

1. Ordered item 1
2. Ordered item 2
   1. Nested ordered item
```

### Code

```markdown
`Inline code`

```python
# Code block with syntax highlighting
def hello():
    return "world"
```
```

### Images

```markdown
![Alt text](image-path.jpg "Optional title")
```

### Tables

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

### LaTeX Math

```markdown
Inline math: $E=mc^2$

Display math:
$$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$$
```

## Tips for Writing Blog Posts

1. **Use headings logically**: Structure your content with proper heading levels (H1, H2, H3)
2. **Add images**: Visual content makes your posts more engaging
3. **Keep paragraphs short**: 3-4 sentences per paragraph is ideal for web readability
4. **Use formatting sparingly**: Bold and italics lose impact when overused
5. **Include code examples**: If you're discussing technical topics, include code snippets
6. **Add internal links**: Link to your other blog posts when relevant
7. **Check your math**: Ensure your LaTeX equations render correctly
8. **Add alt text**: Make your images accessible by including descriptive alt text
9. **Proofread**: Check for spelling and grammar errors before publishing
10. **Update regularly**: Set a schedule for posting new content
