/**
 * QutSur Landing Page - JavaScript
 * Premium interactions and animations
 */

document.addEventListener('DOMContentLoaded', function() {
  // ============================================
  // Sticky Navigation
  // ============================================
  const header = document.querySelector('header');

  function handleScroll() {
    if (window.scrollY > 50) {
      header.classList.add('sticky');
    } else {
      header.classList.remove('sticky');
    }
  }

  window.addEventListener('scroll', handleScroll);
  handleScroll();

  // ============================================
  // Mobile Navigation Toggle
  // ============================================
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function() {
      navLinks.classList.toggle('active');
      navToggle.classList.toggle('active');
    });

    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', function() {
        navLinks.classList.remove('active');
        navToggle.classList.remove('active');
      });
    });

    document.addEventListener('click', function(e) {
      if (!navToggle.contains(e.target) && !navLinks.contains(e.target)) {
        navLinks.classList.remove('active');
        navToggle.classList.remove('active');
      }
    });
  }

  // ============================================
  // Smooth Scrolling
  // ============================================
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#' || href === '') return;

      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        const headerHeight = header.offsetHeight;
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset;
        const offsetPosition = targetPosition - headerHeight - 20;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // ============================================
  // Collapsible Pillar Cards
  // ============================================
  const pillarToggles = document.querySelectorAll('.pillar-toggle');

  pillarToggles.forEach(toggle => {
    toggle.addEventListener('click', function() {
      const card = this.closest('.pillar-card');
      const isExpanded = this.getAttribute('aria-expanded') === 'true';

      this.setAttribute('aria-expanded', !isExpanded);
      card.classList.toggle('expanded');
    });
  });

  // ============================================
  // Scroll Reveal Animation
  // ============================================
  const revealElements = document.querySelectorAll(
    '.pillar-card, .who-item, .about-point, .contact-content'
  );

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  revealElements.forEach(element => {
    revealObserver.observe(element);
  });

  // ============================================
  // Cursor Glow Effect (Desktop Only)
  // ============================================
  if (window.matchMedia('(pointer: fine)').matches) {
    const cursorGlow = document.createElement('div');
    cursorGlow.className = 'cursor-glow';
    document.body.appendChild(cursorGlow);

    let mouseX = 0, mouseY = 0;
    let currentX = 0, currentY = 0;

    document.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
    });

    function animateCursor() {
      const dx = mouseX - currentX;
      const dy = mouseY - currentY;

      currentX += dx * 0.1;
      currentY += dy * 0.1;

      cursorGlow.style.left = currentX + 'px';
      cursorGlow.style.top = currentY + 'px';

      requestAnimationFrame(animateCursor);
    }

    animateCursor();

    // Hide cursor glow when mouse leaves window
    document.addEventListener('mouseleave', () => {
      cursorGlow.style.opacity = '0';
    });

    document.addEventListener('mouseenter', () => {
      cursorGlow.style.opacity = '1';
    });
  }

  // ============================================
  // Animated Counter for Stats
  // ============================================
  const stats = document.querySelectorAll('.stat-number');

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
        entry.target.classList.add('counted');
        animateCounter(entry.target);
      }
    });
  }, { threshold: 0.5 });

  stats.forEach(stat => counterObserver.observe(stat));

  function animateCounter(element) {
    const text = element.textContent;
    const hasPrefix = text.startsWith('$') || text.startsWith('<');
    const hasSuffix = text.endsWith('%') || text.endsWith('B') || text.endsWith('+');

    let prefix = '';
    let suffix = '';
    let numStr = text;

    if (hasPrefix) {
      prefix = text.charAt(0);
      numStr = text.slice(1);
    }
    if (hasSuffix) {
      suffix = text.slice(-1);
      numStr = numStr.slice(0, -1);
    }

    const target = parseFloat(numStr);
    if (isNaN(target)) return;

    const duration = 2000;
    const start = performance.now();

    function update(currentTime) {
      const elapsed = currentTime - start;
      const progress = Math.min(elapsed / duration, 1);

      // Ease out cubic
      const easeProgress = 1 - Math.pow(1 - progress, 3);
      const current = target * easeProgress;

      if (Number.isInteger(target)) {
        element.textContent = prefix + Math.round(current) + suffix;
      } else {
        element.textContent = prefix + current.toFixed(1) + suffix;
      }

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        element.textContent = text; // Ensure exact final value
      }
    }

    requestAnimationFrame(update);
  }

  // ============================================
  // Contact Form Handler
  // ============================================
  const contactForm = document.querySelector('.contact-form');

  if (contactForm) {
    contactForm.addEventListener('submit', async function(e) {
      e.preventDefault();

      const submitButton = contactForm.querySelector('button[type="submit"]');
      const originalText = submitButton.textContent;

      submitButton.textContent = 'Sending...';
      submitButton.disabled = true;

      try {
        const formData = new FormData(contactForm);
        const response = await fetch(contactForm.action, {
          method: 'POST',
          body: formData,
          headers: { 'Accept': 'application/json' }
        });

        if (response.ok) {
          submitButton.textContent = 'Message Sent!';
          submitButton.style.background = '#10B981';
          contactForm.reset();

          setTimeout(() => {
            submitButton.textContent = originalText;
            submitButton.style.background = '';
            submitButton.disabled = false;
          }, 3000);
        } else {
          throw new Error('Form submission failed');
        }
      } catch (error) {
        submitButton.textContent = 'Error - Try Again';
        submitButton.style.background = '#EF4444';

        setTimeout(() => {
          submitButton.textContent = originalText;
          submitButton.style.background = '';
          submitButton.disabled = false;
        }, 3000);

        console.error('Form submission error:', error);
      }
    });
  }

  // ============================================
  // Magnetic Button Effect (Optional)
  // ============================================
  const magneticButtons = document.querySelectorAll('.btn-primary');

  if (window.matchMedia('(pointer: fine)').matches) {
    magneticButtons.forEach(btn => {
      btn.addEventListener('mousemove', function(e) {
        const rect = btn.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;

        btn.style.transform = `translate(${x * 0.1}px, ${y * 0.1}px)`;
      });

      btn.addEventListener('mouseleave', function() {
        btn.style.transform = '';
      });
    });
  }

  // ============================================
  // Parallax Effect on Hero
  // ============================================
  const hero = document.querySelector('.hero');

  if (hero && window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;
      const heroHeight = hero.offsetHeight;

      if (scrolled < heroHeight) {
        const parallaxValue = scrolled * 0.3;
        hero.style.setProperty('--parallax-offset', `${parallaxValue}px`);
      }
    });
  }
});
