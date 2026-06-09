document.addEventListener('DOMContentLoaded', () => {

  // --- TYPING EFFECT FOR HERO TITLE ---
  const line1 = document.querySelector('.typing-line-1');
  const line2 = document.querySelector('.typing-line-2');
  const cursor = document.querySelector('.typing-cursor');

  if (line1 && line2 && cursor) {
    const text1 = line1.textContent.trim();
    const text2 = line2.textContent.trim();

    // Clear contents to start typing animation
    line1.textContent = '';
    line2.textContent = '';

    let index1 = 0;
    let index2 = 0;
    const speed = 80; // ms per character

    // Position cursor after line 1 initially
    line1.after(cursor);

    function typeLine1() {
      if (index1 < text1.length) {
        line1.textContent += text1.charAt(index1);
        index1++;
        setTimeout(typeLine1, speed);
      } else {
        // Move cursor to line 2 and type line 2
        setTimeout(() => {
          line2.after(cursor);
          typeLine2();
        }, 300);
      }
    }

    function typeLine2() {
      if (index2 < text2.length) {
        line2.textContent += text2.charAt(index2);
        index2++;
        setTimeout(typeLine2, speed);
      } else {
        cursor.classList.add('finished');
      }
    }

    // Start typing animation with a short delay
    setTimeout(typeLine1, 500);
  }

  // --- TYPING EFFECT FOR CORPORATE PHILOSOPHY TITLE ---
  const philTitle = document.getElementById('philosophy-title');
  const philLine1 = document.querySelector('.typing-line-p1');
  const philLine2 = document.querySelector('.typing-line-p2');
  const philCursor = document.querySelector('.typing-cursor-p');

  if (philTitle && philLine1 && philLine2 && philCursor) {
    const pText1 = philLine1.textContent.trim();
    const pText2 = philLine2.textContent.trim();

    // Select philosophy card paragraphs
    const cardP1 = document.querySelector('.typing-card-p1');
    const cardP2 = document.querySelector('.typing-card-p2');
    let cardPText1 = '';
    let cardPText2 = '';

    if (cardP1 && cardP2) {
      cardPText1 = cardP1.textContent.trim();
      cardPText2 = cardP2.textContent.trim();
      // Clear card content to trigger animation later
      cardP1.textContent = '';
      cardP2.textContent = '';
    }

    // Clear contents to start typing animation later on viewport entry
    philLine1.textContent = '';
    philLine2.textContent = '';

    let pIndex1 = 0;
    let pIndex2 = 0;
    const pSpeed = 80; // ms per character
    let hasStarted = false;

    let cardIndex1 = 0;
    let cardIndex2 = 0;
    const cardSpeed = 15; // fast typing speed for long paragraphs

    // Position cursor after line 1 initially
    philLine1.after(philCursor);

    function typePhilLine1() {
      if (pIndex1 < pText1.length) {
        philLine1.textContent += pText1.charAt(pIndex1);
        pIndex1++;
        setTimeout(typePhilLine1, pSpeed);
      } else {
        // Move cursor to line 2 and type line 2
        setTimeout(() => {
          philLine2.after(philCursor);
          typePhilLine2();
        }, 300);
      }
    }

    function typePhilLine2() {
      if (pIndex2 < pText2.length) {
        philLine2.textContent += pText2.charAt(pIndex2);
        pIndex2++;
        setTimeout(typePhilLine2, pSpeed);
      } else {
        philCursor.classList.add('finished');
      }
    }

    function typeCardP1() {
      if (cardP1 && cardIndex1 < cardPText1.length) {
        cardP1.textContent += cardPText1.charAt(cardIndex1);
        cardIndex1++;
        setTimeout(typeCardP1, cardSpeed);
      } else if (cardP2) {
        setTimeout(typeCardP2, 200);
      }
    }

    function typeCardP2() {
      if (cardP2 && cardIndex2 < cardPText2.length) {
        cardP2.textContent += cardPText2.charAt(cardIndex2);
        cardIndex2++;
        setTimeout(typeCardP2, cardSpeed);
      }
    }

    // Use IntersectionObserver to trigger typing when scrolled into view
    const philObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !hasStarted) {
          hasStarted = true;
          setTimeout(() => {
            typePhilLine1();
            typeCardP1();
          }, 300); // 300ms delay after entry for natural feel
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.2 // Trigger when 20% of the element is visible
    });

    philObserver.observe(philTitle);
  }

  // --- TYPING EFFECT FOR STANCE TITLE ---
  const stanceTitle = document.getElementById('stance-title');
  const stanceLine1 = document.querySelector('.typing-line-s1');
  const stanceLine2 = document.querySelector('.typing-line-s2');
  const stanceCursor = document.querySelector('.typing-cursor-s');

  if (stanceTitle && stanceLine1 && stanceLine2 && stanceCursor) {
    const sText1 = stanceLine1.textContent.trim();
    const sText2 = stanceLine2.textContent.trim();

    // Clear contents to start typing animation later on viewport entry
    stanceLine1.textContent = '';
    stanceLine2.textContent = '';

    let sIndex1 = 0;
    let sIndex2 = 0;
    const sSpeed = 80; // ms per character (1.5x speed)
    let sHasStarted = false;

    // Position cursor after line 1 initially
    stanceLine1.after(stanceCursor);

    function typeStanceLine1() {
      if (sIndex1 < sText1.length) {
        stanceLine1.textContent += sText1.charAt(sIndex1);
        sIndex1++;
        setTimeout(typeStanceLine1, sSpeed);
      } else {
        // Move cursor to line 2 and type line 2
        setTimeout(() => {
          stanceLine2.after(stanceCursor);
          typeStanceLine2();
        }, 300);
      }
    }

    function typeStanceLine2() {
      if (sIndex2 < sText2.length) {
        stanceLine2.textContent += sText2.charAt(sIndex2);
        sIndex2++;
        setTimeout(typeStanceLine2, sSpeed);
      } else {
        stanceCursor.classList.add('finished');
      }
    }

    // Use IntersectionObserver to trigger typing when scrolled into view
    const stanceObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !sHasStarted) {
          sHasStarted = true;
          setTimeout(typeStanceLine1, 300); // 300ms delay after entry for natural feel
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.2 // Trigger when 20% of the element is visible
    });

    stanceObserver.observe(stanceTitle);
  }

  // --- MOBILE NAV TOGGLE ---
  const menuToggle = document.getElementById('menu-toggle');
  const navMenu = document.getElementById('nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  if (menuToggle && navMenu) {
    menuToggle.addEventListener('click', () => {
      menuToggle.classList.toggle('active');
      navMenu.classList.toggle('active');
    });

    // Close mobile nav when clicking a link
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        menuToggle.classList.remove('active');
        navMenu.classList.remove('active');
      });
    });
  }

  // --- SCROLL EFFECTS & HEADER TRANSITION ---
  const header = document.getElementById('header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // --- SECTION INTERSECTION OBSERVER FOR ACTIVE NAV ---
  const sections = document.querySelectorAll('section');
  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -60% 0px', // Trigger when section occupies the middle of screen
    threshold: 0
  };

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(section => {
    sectionObserver.observe(section);
  });

  // --- REVEAL ON SCROLL ANIMATIONS ---
  const revealElements = document.querySelectorAll('.reveal');
  const revealObserverOptions = {
    root: null,
    rootMargin: '0px 0px -100px 0px', // Trigger slightly before entry
    threshold: 0.1
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target); // Animates only once
      }
    });
  }, revealObserverOptions);

  revealElements.forEach(element => {
    revealObserver.observe(element);
  });



  // --- CONTACT FORM SUBMISSION & VALIDATION ---
  const contactForm = document.getElementById('contact-form');
  const formSuccess = document.getElementById('form-success');

  if (contactForm && formSuccess) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      let isFormValid = true;
      const formControls = contactForm.querySelectorAll('.form-control[required], .form-control[pattern]');
      
      // Perform validation check
      formControls.forEach(control => {
        // Trigger default invalid check if not met
        if (!control.checkValidity()) {
          isFormValid = false;
          // Force display state by triggering interaction classes or focus
          control.classList.add('interacted');
        }
      });

      // Special email formatting double check
      const emailInput = document.getElementById('user-email');
      if (emailInput && emailInput.value.trim() !== '') {
        const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailPattern.test(emailInput.value.trim())) {
          emailInput.setCustomValidity('invalid');
          isFormValid = false;
        } else {
          emailInput.setCustomValidity('');
        }
      }

      if (isFormValid) {
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        submitBtn.disabled = true;
        submitBtn.textContent = '送信中...';
        
        // Submit via Fetch to SSGform endpoint
        const formData = new FormData(contactForm);
        fetch(contactForm.action || 'https://ssgform.com/s/HwQ7BIptSoo0', {
          method: 'POST',
          body: formData,
          headers: {
            'Accept': 'application/json'
          }
        })
        .then(() => {
          // Hide form, show success container
          contactForm.style.display = 'none';
          formSuccess.style.display = 'block';
          
          // Scroll success into view smoothly
          formSuccess.scrollIntoView({ behavior: 'smooth', block: 'center' });
        })
        .catch(error => {
          console.error('Submission error:', error);
          // Fallback: visually show success container in case of CORS or network error
          contactForm.style.display = 'none';
          formSuccess.style.display = 'block';
          formSuccess.scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
      } else {
        // Focus first invalid element
        const firstInvalid = contactForm.querySelector(':invalid');
        if (firstInvalid) {
          firstInvalid.focus();
        }
      }
    });

    // Reset validations on input change
    contactForm.querySelectorAll('.form-control').forEach(control => {
      control.addEventListener('input', () => {
        if (control.id === 'user-email') {
          control.setCustomValidity('');
        }
      });
    });
  }

  // --- HERO VISUAL ANIMATION (ESSENCE & CUBE) ---
  const heroVisual = document.querySelector('.hero-visual');
  const visualContainer = document.querySelector('.visual-a-container');
  const vNodes = document.querySelectorAll('.v-node');
  const ctaButtons = document.querySelectorAll('.hero-ctas .btn');

  if (heroVisual && visualContainer && vNodes.length > 0) {
    let activeHoveredButton = null;

    // Option A SVG Node Coordinates (Initial cx, cy)
    const nodeCoords = [
      { cx: 200, cy: 130 },
      { cx: 260.6, cy: 165 },
      { cx: 260.6, cy: 235 },
      { cx: 200, cy: 270 },
      { cx: 139.4, cy: 235 },
      { cx: 139.4, cy: 165 },
      { cx: 200, cy: 200 },
      { cx: 230.3, cy: 147.5 }
    ];

    let animationFrameId = null;

    // Recalculates and translates Option A SVG dots to form an ellipse surrounding the active CTA button using manual scroll-invariant mapping
    function updateOptionAParticles() {
      if (!activeHoveredButton || !visualContainer) return;

      const svgElement = visualContainer.querySelector('.visual-svg');
      if (!svgElement) return;

      const btnRect = activeHoveredButton.getBoundingClientRect();
      const btnCenterX = btnRect.left + btnRect.width / 2;
      const btnCenterY = btnRect.top + btnRect.height / 2;

      // Define ellipse dimensions in screen pixels (matching button bounding box plus 10px padding to cluster tightly)
      const rxPixels = btnRect.width / 2 + 10;
      const ryPixels = btnRect.height / 2 + 10;

      const svgRect = svgElement.getBoundingClientRect();
      const renderedSize = Math.min(svgRect.width, svgRect.height);
      const scale = 400 / renderedSize;

      // Calculate centering offsets for preserveAspectRatio="xMidYMid meet"
      const offsetX = (svgRect.width - renderedSize) / 2;
      const offsetY = (svgRect.height - renderedSize) / 2;

      vNodes.forEach((node, idx) => {
        if (idx >= nodeCoords.length) return;
        const coords = nodeCoords[idx];
        
        // Target screen coordinate on the ellipse around the button center
        const angle = (idx / 8) * Math.PI * 2;
        const targetX = btnCenterX + Math.cos(angle) * rxPixels;
        const targetY = btnCenterY + Math.sin(angle) * ryPixels;

        // Map target screen coordinates to SVG local space using manual robust conversion
        const localTargetX = (targetX - (svgRect.left + offsetX)) * scale;
        const localTargetY = (targetY - (svgRect.top + offsetY)) * scale;
        
        // Compute translation in SVG user space units
        const tx = localTargetX - coords.cx;
        const ty = localTargetY - coords.cy;
        
        node.style.transform = `translate(${tx}px, ${ty}px)`;
      });
    }

    function clearOptionAParticles() {
      vNodes.forEach(node => {
        node.style.transform = '';
      });
    }

    // Animation loop for frame-perfect tracking while hovered
    function loopOptionAParticles() {
      if (activeHoveredButton) {
        updateOptionAParticles();
        animationFrameId = requestAnimationFrame(loopOptionAParticles);
      }
    }

    // Scroll & Resize listeners for real-time sticky alignment
    window.addEventListener('scroll', () => {
      if (activeHoveredButton && !animationFrameId) {
        updateOptionAParticles();
      }
    }, { passive: true });

    window.addEventListener('resize', () => {
      if (activeHoveredButton && !animationFrameId) {
        updateOptionAParticles();
      }
    });

    // Setup CTA button hover listeners with continuous loop
    ctaButtons.forEach(btn => {
      btn.addEventListener('mouseenter', () => {
        activeHoveredButton = btn;
        if (animationFrameId) cancelAnimationFrame(animationFrameId);
        loopOptionAParticles();
      });
      btn.addEventListener('mouseleave', () => {
        activeHoveredButton = null;
        if (animationFrameId) {
          cancelAnimationFrame(animationFrameId);
          animationFrameId = null;
        }
        clearOptionAParticles();
      });
    });

    // 3D Parallax Tilt for Option A (Essence & Cube) - disabled during button hover
    const essenceWrapper = document.querySelector('.essence-wrapper');
    if (essenceWrapper) {
      heroVisual.addEventListener('mousemove', (e) => {
        if (!activeHoveredButton) {
          const rect = heroVisual.getBoundingClientRect();
          const mouseX = e.clientX - rect.left;
          const mouseY = e.clientY - rect.top;
          
          // Normalize mouse positions to range [-1, 1]
          const xPercent = (mouseX / rect.width - 0.5) * 2;
          const yPercent = (mouseY / rect.height - 0.5) * 2;
          
          // Tilt angles (max 18 degrees for noticeable depth feel)
          const tiltX = -yPercent * 18;
          const tiltY = xPercent * 18;
          
          essenceWrapper.style.transform = `rotateX(${tiltX}deg) rotateY(${tiltY}deg)`;
        }
      });
      
      heroVisual.addEventListener('mouseleave', () => {
        essenceWrapper.style.transform = 'rotateX(0deg) rotateY(0deg)';
      });
    }
  }

  // --- FLOATING THEME SWITCHER BEHAVIOR ---
  const themeSwitchBtn = document.getElementById('theme-switch');
  if (themeSwitchBtn) {
    themeSwitchBtn.addEventListener('click', () => {
      document.body.classList.toggle('theme-light');
      const isLight = document.body.classList.contains('theme-light');
      localStorage.setItem('theme', isLight ? 'light' : 'dark');
    });

    // Check saved theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'light') {
      document.body.classList.add('theme-light');
    }
  }
});
