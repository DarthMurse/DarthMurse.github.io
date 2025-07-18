// Mobile navigation toggle
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
        
        // Close menu when clicking on a link
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
            });
        });
    }
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// WeChat QR modal functionality
function showWeChatQR() {
    const modal = document.getElementById('wechatModal');
    if (modal) {
        modal.style.display = 'block';
    }
}

// Close modal functionality
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('wechatModal');
    const closeBtn = document.querySelector('.close');
    
    if (closeBtn && modal) {
        closeBtn.addEventListener('click', function() {
            modal.style.display = 'none';
        });
        
        // Close modal when clicking outside
        window.addEventListener('click', function(event) {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        });
    }
});

// Navbar scroll effect
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = 'none';
    }
});

// Active navigation link highlighting
function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        if (window.scrollY >= sectionTop) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
}

// Update active nav link on scroll
window.addEventListener('scroll', updateActiveNavLink);

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', function() {
    const animatedElements = document.querySelectorAll('.publication-card, .blog-card');
    
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// Copy email to clipboard
function copyEmail() {
    const email = 'your.email@example.com';
    navigator.clipboard.writeText(email).then(function() {
        // Show success message
        const emailElement = document.querySelector('.contact-item:first-child span');
        const originalText = emailElement.textContent;
        emailElement.textContent = 'Email copied!';
        emailElement.style.color = '#10b981';
        
        setTimeout(() => {
            emailElement.textContent = originalText;
            emailElement.style.color = '';
        }, 2000);
    });
}

// Add click event to email in contact section
document.addEventListener('DOMContentLoaded', function() {
    const emailElement = document.querySelector('.contact-item:first-child');
    if (emailElement) {
        emailElement.style.cursor = 'pointer';
        emailElement.addEventListener('click', copyEmail);
    }
});

// Blog search functionality (if needed)
function searchBlogs(query) {
    const blogCards = document.querySelectorAll('.blog-card');
    const searchTerm = query.toLowerCase();
    
    blogCards.forEach(card => {
        const title = card.querySelector('.blog-title').textContent.toLowerCase();
        const excerpt = card.querySelector('.blog-excerpt').textContent.toLowerCase();
        const tags = Array.from(card.querySelectorAll('.tag')).map(tag => tag.textContent.toLowerCase());
        
        const matches = title.includes(searchTerm) || 
                       excerpt.includes(searchTerm) || 
                       tags.some(tag => tag.includes(searchTerm));
        
        card.style.display = matches ? 'block' : 'none';
    });
}

// Initialize MathJax after page load
document.addEventListener('DOMContentLoaded', function() {
    if (typeof MathJax !== 'undefined') {
        MathJax.typesetPromise().catch(function (err) {
            console.log('MathJax typeset failed: ' + err.message);
        });
    }
});

// Reload MathJax when content is dynamically loaded
function reloadMathJax() {
    if (typeof MathJax !== 'undefined') {
        MathJax.typesetPromise().catch(function (err) {
            console.log('MathJax reload failed: ' + err.message);
        });
    }
}
