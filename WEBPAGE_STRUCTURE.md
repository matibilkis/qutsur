# QutSur Landing Page - Implementation Guide for Claude Code

## File Structure for GitHub Pages

```
qutsur-landing/
├── index.html (main landing page)
├── css/
│   └── styles.css (all styling)
├── js/
│   └── script.js (minimal interactivity)
├── assets/
│   ├── logo.svg
│   ├── hero.jpg (or video background)
│   └── icons/ (pillar icons, social, etc)
├── _redirects (for custom domain)
└── CNAME (GitHub Pages custom domain)
```

---

## HTML Structure Outline

### Document Head
```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="QutSur: Quantum technology consulting, training, and ecosystem building for Latin America.">
  <meta name="keywords" content="quantum computing, quantum machine learning, Argentina, consulting, training">
  <title>QutSur - Quantum Tech for South America</title>
  <link rel="stylesheet" href="css/styles.css">
</head>
```

### Document Body Structure

#### 1. Navigation Header
```html
<header>
  <nav>
    <div class="nav-brand">QutSur</div>
    <ul class="nav-links">
      <li><a href="#training">Training</a></li>
      <li><a href="#monitoring">Monitoring</a></li>
      <li><a href="#ecosystem">Ecosystem</a></li>
      <li><a href="#contact" class="nav-cta">Contact</a></li>
    </ul>
  </nav>
</header>
```
**CSS Notes:**
- Sticky position (stays at top on scroll)
- Background: rgba with slight transparency
- Mobile hamburger menu for <768px

---

#### 2. Hero Section
```html
<section class="hero">
  <div class="hero-content">
    <h1>Our mission is to make the quantum tech ecosystem in South America stronger.</h1>
    <p class="subheadline">We bridge the gap between frontier quantum science and business reality.</p>
    <div class="hero-cta">
      <button class="btn btn-primary">Start a Conversation</button>
      <button class="btn btn-secondary">Learn More</button>
    </div>
  </div>
  <div class="hero-visual">
    <!-- Hero image or video background -->
  </div>
</section>
```
**CSS Notes:**
- Full viewport height (min-height: 100vh)
- Centered text with max-width container
- Gradient or solid background (teal-to-darker gradient recommended)
- Hero visual: large imagery or animated quantum circuit visualization
- Hero buttons: primary (solid teal), secondary (outline)

---

#### 3. Three Pillars Section
```html
<section class="pillars" id="offerings">
  <div class="container">
    <h2>Three Pillars of Quantum Readiness</h2>
    
    <div class="pillars-grid">
      <!-- Pillar 1: Training -->
      <div class="pillar-card">
        <div class="pillar-icon">
          <svg><!-- training icon --></svg>
        </div>
        <h3>Training</h3>
        <p class="pillar-headline">Design the Quantum Future in Argentina</p>
        <p class="pillar-description">We are designing Argentina's first master-level program...</p>
        <ul class="pillar-points">
          <li>First inter-university master program...</li>
          <li>Tailored workshops and in-company trainings...</li>
          <!-- etc -->
        </ul>
        <a href="#" class="pillar-cta">Explore training programs →</a>
      </div>
      
      <!-- Pillar 2: Monitoring -->
      <div class="pillar-card">
        <!-- Similar structure -->
      </div>
      
      <!-- Pillar 3: Ecosystem -->
      <div class="pillar-card">
        <!-- Similar structure -->
      </div>
    </div>
  </div>
</section>
```
**CSS Notes:**
- 3-column grid on desktop (1 column on mobile, 2 on tablet)
- Cards: border-left with teal accent
- Equal height cards (flexbox)
- Icons: 60x60px, centered, teal color
- Hover effect: subtle shadow lift, background color shift

---

#### 4. Why QutSur Section
```html
<section class="why-qutsur">
  <div class="container">
    <h2>Why QutSur</h2>
    
    <div class="why-grid">
      <div class="why-column">
        <h3>Leadership & Track Record</h3>
        <ul>
          <li>PhD in quantum machine learning...</li>
          <li>Group leader at CVC Barcelona...</li>
          <!-- etc -->
        </ul>
      </div>
      
      <div class="why-column">
        <h3>Market Position</h3>
        <ul>
          <li>50–70% cost advantage...</li>
          <li>Time zone alignment with US...</li>
          <!-- etc -->
        </ul>
      </div>
      
      <div class="why-column">
        <h3>Why Now</h3>
        <ul>
          <li>$850B quantum market by 2040...</li>
          <li>Enterprise budgets: $3M–$6M...</li>
          <!-- etc -->
        </ul>
      </div>
    </div>
  </div>
</section>
```
**CSS Notes:**
- 3-column layout (similar to pillars)
- Background: light gray or subtle pattern
- Lists: checkmarks or bullet points in teal
- Font: sans-serif, 16px base

---

#### 5. Market Opportunity Section (with Stats)
```html
<section class="market">
  <div class="container">
    <h2>The Quantum Opportunity in Latin America</h2>
    
    <div class="stats-grid">
      <div class="stat">
        <div class="stat-number">$125B</div>
        <p>Global quantum market by 2030</p>
      </div>
      
      <div class="stat">
        <div class="stat-number">85%</div>
        <p>Investment concentrated in US, EU, China</p>
      </div>
      
      <div class="stat">
        <div class="stat-number">&lt;0.1%</div>
        <p>Latin America's share of quantum investment</p>
      </div>
      
      <div class="stat">
        <div class="stat-number">30%</div>
        <p>Quantum consulting market CAGR (2023–2030)</p>
      </div>
    </div>
  </div>
</section>
```
**CSS Notes:**
- 4-column grid (2x2 on tablet, 1 column on mobile)
- Stats styled with large numbers (48px), smaller descriptive text
- Cards: centered, padding 20–30px
- Background: white or subtle gradient
- Border-top accent line in teal

---

#### 6. Who We Serve (Table or Cards)
```html
<section class="clients">
  <div class="container">
    <h2>Who We Serve</h2>
    
    <table class="clients-table">
      <thead>
        <tr>
          <th>Client Type</th>
          <th>What They Need</th>
          <th>How We Help</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Governments & Policymakers</td>
          <td>Strategic quantum roadmaps...</td>
          <td>Real-time intelligence...</td>
        </tr>
        <!-- More rows -->
      </tbody>
    </table>
  </div>
</section>
```
**CSS Notes:**
- Responsive table (scrollable on mobile)
- Alternating row backgrounds (white / light gray)
- Hover effect on rows
- Font: 14–16px
- Padding: 12–16px per cell

---

#### 7. Credibility & Social Proof
```html
<section class="proof">
  <div class="container">
    <h2>Trusted by Leading Institutions</h2>
    
    <div class="proof-grid">
      <div class="proof-item">
        <h4>Publications & Recognition</h4>
        <ul>
          <li>Published in Nature, Science, IEEE...</li>
          <li>10,000+ citations in academic literature</li>
          <!-- etc -->
        </ul>
      </div>
      
      <div class="proof-item">
        <h4>Network & Partnerships</h4>
        <ul>
          <li>Los Alamos National Laboratory...</li>
          <!-- etc -->
        </ul>
      </div>
      
      <div class="proof-item">
        <h4>Industry Impact</h4>
        <ul>
          <li>Developed algorithms for Anyverse, GMV...</li>
          <!-- etc -->
        </ul>
      </div>
    </div>
    
    <!-- Partner logos (optional) -->
    <div class="partner-logos">
      <img src="assets/logo-lanl.png" alt="Los Alamos">
      <img src="assets/logo-cvc.png" alt="Computer Vision Center">
      <!-- etc -->
    </div>
  </div>
</section>
```
**CSS Notes:**
- 3-column grid
- Partner logos: 80–120px height, grayscale by default, color on hover
- Background: light teal or off-white

---

#### 8. Call-to-Action Section
```html
<section class="cta-main">
  <div class="container">
    <h2>Let's Build Quantum Capacity Together</h2>
    <p>Whether you're exploring quantum readiness, need strategic intelligence, or want to invest in the region's quantum future, we're ready to help.</p>
    
    <div class="cta-buttons">
      <button class="btn btn-primary btn-lg">Start a Conversation</button>
      <button class="btn btn-secondary btn-lg">Explore Programs</button>
    </div>
  </div>
</section>
```
**CSS Notes:**
- Background: solid teal or gradient
- Text color: white
- Buttons: larger padding (12–16px), 18px font
- Centered layout

---

#### 9. Secondary CTAs (Optional Grid)
```html
<section class="secondary-ctas">
  <div class="container">
    <h3>Quick Links</h3>
    
    <div class="cta-grid">
      <a href="#" class="cta-link">
        <h4>Request a Quantum Readiness Assessment</h4>
        <p>30-min discovery call →</p>
      </a>
      
      <a href="#" class="cta-link">
        <h4>Explore Training Programs</h4>
        <p>See curriculum and enrollment →</p>
      </a>
      
      <a href="#" class="cta-link">
        <h4>Join the Quantum Residency</h4>
        <p>Apply to Edge City program →</p>
      </a>
      
      <a href="#" class="cta-link">
        <h4>Connect with Quantum Nation</h4>
        <p>Access funding and mentorship →</p>
      </a>
    </div>
  </div>
</section>
```
**CSS Notes:**
- 4-column grid (2x2 on tablet, 1 column on mobile)
- Cards: border-top accent in teal
- Hover effect: slight lift, color transition
- Padding: 20–30px

---

#### 10. Contact / Newsletter Section
```html
<section class="contact" id="contact">
  <div class="container">
    <h2>Get In Touch</h2>
    
    <div class="contact-content">
      <div class="contact-info">
        <h3>QutSur LLC</h3>
        <p><strong>Email:</strong> hello@qutsur.com</p>
        <p><strong>Location:</strong> La Plata, Argentina | Barcelona, Spain</p>
        <p><strong>Address:</strong> La Plata, Provincia de Buenos Aires, Argentina</p>
        
        <div class="social-links">
          <a href="#" class="social-icon">LinkedIn</a>
          <a href="#" class="social-icon">Twitter</a>
          <a href="#" class="social-icon">GitHub</a>
        </div>
      </div>
      
      <form class="contact-form">
        <input type="text" placeholder="Your Name" required>
        <input type="email" placeholder="Your Email" required>
        <textarea placeholder="Message..." rows="5"></textarea>
        <button type="submit" class="btn btn-primary">Send Message</button>
      </form>
    </div>
  </div>
</section>
```
**CSS Notes:**
- 2-column layout (1 column on mobile)
- Form inputs: clean borders, focus states with teal outline
- Background: light gray or white
- Button: primary teal color

---

#### 11. Footer
```html
<footer>
  <div class="container">
    <div class="footer-content">
      <div class="footer-col">
        <h4>QutSur</h4>
        <p>Building quantum capacity in South America.</p>
      </div>
      
      <div class="footer-col">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="#training">Training</a></li>
          <li><a href="#monitoring">Monitoring</a></li>
          <li><a href="#ecosystem">Ecosystem</a></li>
        </ul>
      </div>
      
      <div class="footer-col">
        <h4>Resources</h4>
        <ul>
          <li><a href="#">Blog</a></li>
          <li><a href="#">Papers</a></li>
          <li><a href="#">Whitepaper</a></li>
        </ul>
      </div>
    </div>
    
    <div class="footer-bottom">
      <p>&copy; 2026 QutSur LLC. All rights reserved.</p>
      <p><a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a></p>
    </div>
  </div>
</footer>
```
**CSS Notes:**
- Background: dark (charcoal or near-black)
- Text color: white
- 3–4 column grid (1 column on mobile)
- Footer bottom: smaller font, border-top accent

---

## CSS Implementation Notes

### Design System Variables
```css
:root {
  /* Colors */
  --primary: #20A69E; /* Teal */
  --primary-dark: #1D7876;
  --primary-light: #E0F5F3;
  --secondary: #2A5264; /* Deep blue */
  --neutral: #F5F5F5; /* Light gray */
  --text-dark: #1F2121;
  --text-light: #FFFFFF;
  
  /* Typography */
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-size-base: 16px;
  --font-size-lg: 18px;
  --font-size-xl: 20px;
  --font-size-2xl: 24px;
  --font-size-3xl: 30px;
  --font-size-4xl: 36px;
  
  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  
  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  
  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.15);
}
```

### Container & Grid
```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-lg);
}

.grid {
  display: grid;
  gap: var(--spacing-lg);
}

.grid-2 {
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}

.grid-3 {
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

@media (max-width: 768px) {
  .grid-3, .grid-2 {
    grid-template-columns: 1fr;
  }
}
```

### Typography
```css
h1 {
  font-size: var(--font-size-4xl);
  line-height: 1.2;
  margin-bottom: var(--spacing-lg);
  color: var(--text-dark);
}

h2 {
  font-size: var(--font-size-3xl);
  margin-bottom: var(--spacing-lg);
}

p {
  line-height: 1.6;
  color: var(--text-dark);
  margin-bottom: var(--spacing-md);
}
```

### Buttons
```css
.btn {
  display: inline-block;
  padding: var(--spacing-md) var(--spacing-lg);
  border-radius: var(--radius-md);
  font-size: var(--font-size-base);
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  text-decoration: none;
}

.btn-primary {
  background-color: var(--primary);
  color: var(--text-light);
}

.btn-primary:hover {
  background-color: var(--primary-dark);
  box-shadow: var(--shadow-md);
}

.btn-secondary {
  background-color: transparent;
  border: 2px solid var(--primary);
  color: var(--primary);
}

.btn-secondary:hover {
  background-color: var(--primary-light);
}

.btn-lg {
  padding: var(--spacing-lg) var(--spacing-xl);
  font-size: var(--font-size-lg);
}
```

### Section Spacing
```css
section {
  padding: 60px 0;
}

section:nth-child(even) {
  background-color: var(--neutral);
}

@media (max-width: 768px) {
  section {
    padding: 40px 0;
  }
}
```

---

## JavaScript Interactivity (Minimal)

### Sticky Navigation
```javascript
window.addEventListener('scroll', () => {
  const header = document.querySelector('header');
  if (window.scrollY > 50) {
    header.classList.add('sticky');
  } else {
    header.classList.remove('sticky');
  }
});
```

### Smooth Scroll
```javascript
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});
```

### Contact Form Handler
```javascript
const form = document.querySelector('.contact-form');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  // Send to email service (e.g., Formspree, Netlify Forms)
  console.log('Form submitted');
});
```

---

## Deployment to GitHub Pages + Custom Domain

### 1. Create Repository
```bash
git init
git add .
git commit -m "Initial QutSur landing page"
git remote add origin https://github.com/yourusername/qutsur-landing.git
git push -u origin main
```

### 2. Enable GitHub Pages
- Go to repository Settings → Pages
- Set source to `main` branch, root folder
- GitHub will provide `yourusername.github.io/qutsur-landing`

### 3. Custom Domain (qutsur.com or similar)
- Register domain (e.g., DonWeb, Namecheap, GoDaddy)
- Add CNAME record: `qutsur.com` → `yourusername.github.io`
- Create `CNAME` file in repo root with `qutsur.com`
- Push changes

### 4. SSL Certificate (Free)
- GitHub Pages provides free SSL automatically
- Just wait 5–10 minutes after domain setup

---

## Analytics & Tracking

### Plausible Analytics (Privacy-Friendly)
```html
<script defer data-domain="qutsur.com" src="https://plausible.io/js/script.js"></script>
```

### Or Google Analytics
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXX');
</script>
```

---

## SEO Checklist

- [ ] Meta description (160 chars): *"QutSur: Quantum computing consulting, training, and ecosystem building for Latin America. Expert guidance on quantum readiness, technology monitoring, and regional capacity development."*
- [ ] H1 present and unique
- [ ] Keywords in headings and body text
- [ ] Internal links to `/blog`, `/resources`, `/contact`
- [ ] Open Graph tags for social sharing
- [ ] Mobile responsive (viewport meta tag)
- [ ] Fast page load (<3s)
- [ ] Structured data (schema.org JSON-LD for Organization)

### Schema.org JSON-LD
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "QutSur",
  "url": "https://qutsur.com",
  "logo": "https://qutsur.com/assets/logo.svg",
  "description": "Quantum computing consulting, training, and ecosystem building for Latin America.",
  "sameAs": ["https://linkedin.com/company/qutsur", "https://twitter.com/qutsur"],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "hello@qutsur.com"
  }
}
</script>
```

---

## Next Steps for Claude Code

1. **Accept CONTENT.md** as the source of truth for all text
2. **Use WEBPAGE_STRUCTURE.md** (this file) as the implementation roadmap
3. **Build index.html** with all sections listed above
4. **Create css/styles.css** with design system variables and responsive layout
5. **Add js/script.js** for sticky nav, smooth scroll, form handling
6. **Test responsively** on mobile (375px), tablet (768px), desktop (1200px)
7. **Optimize images** (WebP format, 1080–1920px width max)
8. **Deploy to GitHub** with custom domain setup

---

## File Checklist

```
✓ index.html (fully structured)
✓ css/styles.css (design system + responsive)
✓ js/script.js (minimal interactivity)
✓ assets/logo.svg
✓ assets/icons/ (training, monitoring, ecosystem)
✓ assets/hero-image.jpg (or video)
✓ CNAME (for custom domain)
✓ README.md (deployment instructions)
✓ .gitignore (for node_modules, etc)
```

Ready for Claude Code to build! 🚀
