# Personal Website

This is a personal website template designed to be hosted on GitHub Pages. It features a clean, responsive design with a main page for your profile and a blog section that supports Markdown and LaTeX rendering.

## Structure

```
DarthMurse.github.io/
├── index.html              # Main page with personal information
├── blog.html               # Blog listing page
├── css/
│   └── style.css           # Main stylesheet
├── js/
│   └── script.js           # JavaScript functionality
├── images/
│   ├── profile.jpg         # Your profile photo
│   └── wechat-qr.png       # Your WeChat QR code
└── blog/
    ├── blog-post-name/     # Each blog post has its own folder
    │   ├── index.html      # The blog post HTML
    │   ├── featured.jpg    # Featured image for the blog post
    │   └── other-images/   # Other resources for the blog post
    └── another-blog-post/
        └── ...
```

## Features

- Responsive design that works on mobile, tablet, and desktop
- Dark/light mode toggle
- Clean and modern UI with subtle animations
- Blog system with Markdown and LaTeX support via MathJax
- Social media integration (GitHub and WeChat)
- Publications section with links to papers, code, and DOIs
- Contact information section

## Customization

### Personal Information

Edit `index.html` to update:
- Your name (replace "Your Name" throughout the file)
- Your profile description
- Your publications list
- Your contact information
- Social media links

### Profile Photo

1. Replace `/images/profile.jpg` with your own photo
2. Recommended size: 300x300 pixels, square format

### WeChat QR Code

1. Replace `/images/wechat-qr.png` with your WeChat QR code
2. Ensure it's clear and scannable

### Adding Blog Posts

1. Create a new folder in the `/blog/` directory with your post name (use hyphens for spaces)
2. Copy the structure from an existing blog post folder
3. Update the content in `index.html`
4. Add your featured image and any other resources
5. Update `blog.html` to include your new blog post in the listing

### Colors and Styling

Edit `css/style.css` to change:
- Primary color: `--primary-color: #2563eb;` (blue)
- Secondary color: `--secondary-color: #64748b;` (gray)
- Accent color: `--accent-color: #f59e0b;` (amber)
- Background colors, text colors, etc.

## Deployment on GitHub Pages

1. Ensure your repository is named `username.github.io` (where `username` is your GitHub username)
2. Push your changes to the `master` branch (or `main` branch, depending on your GitHub settings)
3. Go to Settings > Pages in your GitHub repository
4. Select "Deploy from a branch" as the source
5. Choose `master` (or `main`) branch and save
6. Your site will be published at `https://username.github.io/`

## Adding a Custom Domain (Optional)

1. Purchase a domain name from a domain registrar
2. Add a file named `CNAME` to your repository root with your domain name
3. Configure DNS settings with your domain registrar as per GitHub's instructions
4. In your repository, go to Settings > Pages > Custom domain and add your domain name
5. Check "Enforce HTTPS" for secure connections

## Local Development

To test locally before deploying:

1. Clone this repository
2. Open `index.html` in a web browser or use a local server
   - Python simple server: `python -m http.server`
   - Node.js: `npx serve`
3. Make your changes and test
4. Commit and push to deploy

## Credits

- Fonts: Inter from Google Fonts
- Icons: Font Awesome 6
- Math rendering: MathJax
- Code highlighting: highlight.js

## License

MIT License
