import os

html_template = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
    <title>Darshan Naidu — Video Editor, Social Media Manager &amp; Visual Designer</title>
    
    <!-- SEO & Metadata -->
    <meta name="description" content="Darshan Naidu is a video editor, social media manager, and multidisciplinary visual designer crafting high-impact reels, cinematic cuts, and digital content with rhythm and personality." />
    <meta name="keywords" content="Darshan Naidu, video editor, social media manager, visual designer, reel editor, motion graphics, creative director, content creator, portfolio" />
    <meta name="author" content="Darshan Naidu" />
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://darshannaidu.vercel.app/" />
    <meta property="og:title" content="Darshan Naidu — Video Editor &amp; Visual Creative" />
    <meta property="og:description" content="I edit videos, build social content, and craft visuals that make people stop scrolling. Rhythm, pacing, and personality in every cut." />
    <meta property="og:image" content="https://darshannaidu.vercel.app/work-section/slider_img_1.webp" />

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="https://darshannaidu.vercel.app/" />
    <meta property="twitter:title" content="Darshan Naidu — Video Editor &amp; Visual Creative" />
    <meta property="twitter:description" content="I edit videos, build social content, and craft visuals that make people stop scrolling." />
    <meta property="twitter:image" content="https://darshannaidu.vercel.app/work-section/slider_img_1.webp" />

    <!-- Favicon & Touch Icons -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />
    <link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32" />
    <link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16" />
    <link rel="apple-touch-icon" href="/apple-icon.png" sizes="180x180" />
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
    <style>
      .footer-name, .footer-socials, .footer-copyright, .footer-label {
        font-family: 'FKGrotesk', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif !important;
      }
    </style>
    <script type="module" crossorigin src="/assets/index-CnbWzhzO.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-ZSMau8ex.css">
  </head>
  <body>
    <!-- Anti-flash script for direct route reloads -->
    <script>
      if (history.scrollRestoration) history.scrollRestoration = "manual";
      window.scrollTo(0, 0);
      (function () {
        var path = (window.location.pathname || "/").replace(/\\/$/, "") || "/";
        var h = window.location.hash;
        var segs = path.split("/").filter(Boolean);
        var last = segs[segs.length - 1] || "";
        var isAbout = path.indexOf("/about") !== -1 || last === "about" || h === "#about";
        var isWorks =
          path.indexOf("/works") !== -1 ||
          path.indexOf("/work-selection") !== -1 ||
          last === "works" ||
          last === "work-selection" ||
          h === "#work-selection";
        var isHome = path === "/" || path === "/index" || path === "/test" || path === "/test/" || path === "/test/index" || path === "/test/home";
        var reserved = { about: 1, works: 1, "work-selection": 1, test: 1, index: 1, home: 1, hub: 1 };
        var isProject = false;
        if (!isAbout && !isWorks && !isHome) {
          if (h && h.length > 1 && h !== "#about" && h !== "#work-selection") isProject = true;
          else if (last && !reserved[last]) isProject = true;
        }
        if (h && h.length > 1) {
          if (h === "#work-selection") isWorks = true;
          if (h === "#about") isAbout = true;
        }
        if (!h || h.length <= 1) {
          if (!isAbout && !isWorks && !isProject) {
            document.documentElement.style.backgroundColor = "#0f0f0f";
          }
        }
        if (isAbout) {
          document.write(
            '<style id="anti-flash-css">#slider-page { display: none !important; } #about-section { display: block !important; opacity: 1; } #about-preloader { display: flex !important; } .preloader-counter-about, .preloader-progress-bar-about, .preloader-progress-about { visibility: visible !important; opacity: 1 !important; } nav { opacity: 0 !important; visibility: hidden !important; pointer-events: none !important; } .about-content-wrapper { opacity: 0 !important; visibility: hidden !important; }</style>'
          );
        } else if (isWorks) {
          document.documentElement.style.backgroundColor = "#0f0f0f";
          document.write(
            '<style id="anti-flash-css">html, body { background-color: #0f0f0f !important; } #slider-page { display: none !important; } #about-section { display: none !important; } #project-page { display: none !important; } #work-selection-page { display: block !important; opacity: 1; } #work-selection-preloader { display: flex !important; } .preloader-counter-work-selection, .preloader-progress-bar-work-selection, .preloader-progress-work-selection { visibility: visible !important; opacity: 1 !important; } nav { opacity: 0 !important; visibility: hidden !important; pointer-events: none !important; } #slider-title-ws, #slider-indices-ws, #slider-number-ws, #slider-indices-wrapper-ws { opacity: 0 !important; visibility: hidden !important; }</style>'
          );
        } else if (isProject) {
          document.documentElement.style.backgroundColor = "#0f0f0f";
          document.write(
            '<style id="anti-flash-css">body { background-color: #0f0f0f !important; } #slider-page { display: none !important; } #project-page { display: block !important; opacity: 1; } #project-preloader { display: flex !important; } .preloader-counter-projects, .preloader-progress-bar-projects, .preloader-progress-projects { visibility: visible !important; opacity: 1 !important; } nav { opacity: 0 !important; visibility: hidden !important; pointer-events: none !important; } #hero-title, #project-number, #project-info-section, #project-images, #project-footer { opacity: 0 !important; visibility: hidden !important; }</style>'
          );
        }
      })();
    </script>
    
    <!-- Nav bar -->
    <nav>
      <span class="nav-logo"><a href="/" data-nav="home">Darshan Naidu</a></span>
      <div class="nav-links">
        <a href="/works" data-nav="works">Works,</a>
        <a href="/about" data-nav="about">About,</a>
        <a href="mailto:darshan@darshannaidu.com">Reach out</a>
      </div>
      <p class="menu-open">Menu</p>
    </nav>

    <!-- Menu overlay -->
    <div class="menu">
      <div class="menu-nav">
        <span class="nav-logo"><a href="/" data-nav="home">Darshan Naidu</a></span>
        <div class="menu-close"><p>Close</p></div>
      </div>
      <div class="menu-links">
        <div class="menu-link">
          <a href="/works" data-nav="works">Works</a>
        </div>
        <div class="menu-link">
          <a href="/about" data-nav="about">About</a>
        </div>
        <div class="menu-link">
          <a href="mailto:darshan@darshannaidu.com">Reach out</a>
        </div>
      </div>
      <div class="menu-footer">
        <div class="socials">
          <p>Socials</p>
          <div class="socials-list">
            <a href="https://www.instagram.com/fxdarshan/" target="_blank" rel="noopener noreferrer">Instagram</a>
            <a href="https://www.linkedin.com/in/darshannaidu" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a href="https://x.com" target="_blank" rel="noopener noreferrer">X (Twitter)</a>
          </div>
        </div>
      </div>
    </div>

    <div id="smooth-wrapper">
    <div id="slider-page">
      <!-- Scroll Down -->
      <p class="scroll-down" id="scroll-down">Scroll Down</p>

      <!-- Hero Preloader -->
      <div class="preloader-counter">
        <h1>0</h1>
      </div>

      <!-- Hero Section -->
      <section class="hero">
        <div class="hero-bg">
          <img src="/hero/hero.webp" alt="" />
        </div>
        <div class="hero-overlay"></div>
        <div class="card-reveal-bg"></div>
        <div class="card">
          <div class="card-top-left">
            <p class="label">Video Editor · Social Media · Visual Designer</p>
            <h1 class="make-it-last">
              <span class="make-it">Stop The</span><br>
              <span class="last">Scroll</span>
            </h1>
          </div>
          <div class="card-bottom-right">
            <p class="label">Portfolio</p>
            <h1>‘26</h1>
          </div>
        </div>
        <div class="progress-bar">
          <div class="progress"></div>
        </div>
      </section>

      <!-- Manifesto Section -->
      <div class="next-section manifesto" id="manifesto-section">
        <div class="manifesto__previews">
          <div class="manifesto__preview manifesto__preview--1" data-preview="1">
            <img src="/manifesto/img-1.webp" alt="" />
          </div>
          <div class="manifesto__preview manifesto__preview--2" data-preview="2">
            <img src="/manifesto/img-2.webp" alt="" />
          </div>
          <div class="manifesto__preview manifesto__preview--3" data-preview="3">
            <img src="/manifesto/img-3.webp" alt="" />
          </div>
        </div>
        <section class="manifesto__slide manifesto__slide--1" data-slide="1">
          <div class="manifesto__copy">
            <p class="manifesto__text manifesto__text--left">In an endless feed, <br />you have three seconds <br />to be remembered.</p>
          </div>
        </section>
        <div class="manifesto__spacer" data-spacer="1"></div>
        <section class="manifesto__slide manifesto__slide--2" data-slide="2">
          <div class="manifesto__copy">
            <p class="manifesto__text manifesto__text--center">Make them count.</p>
          </div>
        </section>
        <div class="manifesto__spacer" data-spacer="2"></div>
        <section class="manifesto__slide manifesto__slide--3" data-slide="3">
          <div class="manifesto__copy">
            <p class="manifesto__text manifesto__text--left">Great edits turn <br />attention into obsession.</p>
          </div>
        </section>
        <div class="manifesto__spacer" data-spacer="3"></div>
        <section class="manifesto__slide manifesto__slide--4 manifesto__slide--last" data-slide="4">
          <div class="manifesto__copy">
            <p class="manifesto__text manifesto__text--center">Rhythm. Pacing. Impact.</p>
          </div>
        </section>
      </div>

      <!-- Slider Section -->
      <section class="slider" id="slider-section">
        <div class="slider-images" id="slider-images">
          <img src="/work-section/slider_img_1.webp" alt="Slide 1" />
        </div>

        <div class="slider-title" id="slider-title">
          <h1>
            Rhythm &amp; Motion
          </h1>
        </div>

        <div class="slider-indicator" id="slider-indicator">
          <div class="slider-indices-wrapper" id="slider-indices-wrapper">
            <div class="slider-progress-bar" id="slider-progress-bar-container">
              <div class="slider-progress" id="slider-progress-bar"></div>
            </div>
            <div class="slider-indices" id="slider-indices"></div>
          </div>

          <div class="slider-number" id="slider-number">
            <span class="current-number" id="current-number">01</span>
          </div>
        </div>
      </section>

      <section class="outro-unified" id="outro-section" data-nav-theme="light">
        <!-- Outro Progress Bar -->
        <div class="outro-progress-bar" id="outro-progress-bar-container">
          <div class="outro-progress" id="outro-progress-bar"></div>
        </div>

        <!-- Part 1: Transition Text -->
        <div class="outro-transition-wrapper" id="outro-transition-wrapper">
          <h1 class="outro-transition-text" id="outro-transition-text">Behind the timeline.</h1>
        </div>
      </section>
    </div>

    <div class="outro-content-wrapper" id="outro-content-wrapper" style="opacity: 0; pointer-events: none;">
      <h1 class="outro-text" id="outro-carve">Cut with</h1>
      <div class="outro-img-container" id="outro-img-block">
        <img src="/outro-about/about-hero_img.webp" alt="Creative" />
      </div>
      <h2 class="outro-text into" id="outro-into">Pure</h2>
      <h1 class="outro-text" id="outro-memory">Intent</h1>
    </div>

    <div id="about-section" style="display: none;" data-nav-theme="light">
      <!-- Collapse Text Wrapper -->
      <div class="about-collapse-text-wrapper" id="about-collapse-text-wrapper">
        <div class="about-collapse-text"><p>Cut with</p></div>
        <div class="about-collapse-text"><p>Rhythm.</p></div>
      </div>

      <!-- About Preloader -->
      <div id="about-preloader" style="display: none;">
        <div class="preloader-counter-about">
          <h1>0</h1>
        </div>
        <div class="preloader-progress-bar-about">
          <div class="preloader-progress-about"></div>
        </div>
      </div>

      <div class="about-img-container" id="about-hero-img-block" style="opacity: 0;">
        <img src="/outro-about/about-hero_img.webp" alt="About Hero" />
      </div>

      <div id="about-text-container" style="position: absolute; top: 0; left: 0; width: 100%; height: 100vh; display: flex; align-items: center; justify-content: center; z-index: 10; pointer-events: none;">
      </div>

      <div class="about-content-wrapper">
        <div class="about-additional-content">
          <div class="about-col left">
          </div>
          
          <div class="about-col right">
            <div class="about-info-block who-am-i">
              <p class="about-description">
                <span class="about-label-who-am-i">Who am I.</span>
                Hey, I'm Darshan. A video editor, visual designer, and social media strategist obsessed with visual rhythm and retention. I take raw concepts and transform them into magnetic short-form reels, cinematic edits, and high-converting visual systems that thrive in fast feeds.
              </p>
            </div>

            <div class="about-info-block design-bridge">
              <p class="about-description">
                <span class="about-label-about">What drives me.</span>
                Audio transients that sync with visual cuts, typography that demands attention, and pacing that refuses to let the viewer swipe away. If it doesn't evoke a feeling in the first three seconds, it gets reworked.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Spotlight Section -->
    <section class="spotlight" id="spotlight-section" style="display: none;">
      <div class="spotlight-titles-container">
        <div class="spotlight-titles" id="spotlight-titles"></div>
      </div>
      <div class="spotlight-images" id="spotlight-images"></div>
    </section>

    <!-- Core Values Section -->
    <section class="core-values" id="core-values-section" style="display: none;">
      <div class="core-values-pinned">
        <div class="core-values-label">Creative Principles:</div>
        <span class="core-title-main" id="core-title-main">Rhythm.</span>
      </div>
      <div class="core-values-list-container">
        <p class="core-values-list" id="core-values-list">
          <span class="core-value-item" data-main="Rhythm.">Cut on the beat. Move with momentum.</span>
          <span class="core-value-item" data-main="Hook.">The first 3 seconds decide everything.</span>
          <span class="core-value-item" data-main="Form.">Design isn't decoration—it's direction.</span>
          <span class="core-value-item" data-main="Impact.">Make content that gets saved, shared, and remembered.</span>
        </p>
      </div>
    </section>

    <!-- Footer Section -->
    <section class="footer-section" id="footer-section">
      <div class="footer-img-wrapper" id="footer-img-wrapper">
        <img src="/outro-about/about3.webp" alt="Footer Image" />
      </div>
      <div class="footer-content" id="footer-content">
        <div class="footer-text footer-left" id="footer-left">
          <span class="footer-label">Got a brand or vision in mind?</span>
          <h1 class="footer-name" id="footer-name"><a href="mailto:darshan@darshannaidu.com" class="footer-name-link" style="color: inherit; text-decoration: none;">Let's Talk</a></h1>
        </div>
        <div class="footer-card-spacer" id="footer-card-spacer"></div>
        <div class="footer-text footer-right" id="footer-right">
          <span class="footer-label">Socials</span>
          <h1 class="footer-socials" id="footer-socials">
            <a href="https://www.instagram.com/fxdarshan/" target="_blank" rel="noopener noreferrer" class="social-link footer-social-link" style="color: inherit; text-decoration: none; margin-right: 0.5ch;">Ig</a>
            <a href="https://www.linkedin.com/in/darshannaidu/" target="_blank" rel="noopener noreferrer" class="social-link footer-social-link" style="color: inherit; text-decoration: none; margin-right: 0.5ch;">In</a>
            <a href="https://x.com" target="_blank" rel="noopener noreferrer" class="social-link footer-social-link" style="color: inherit; text-decoration: none;">X</a>
          </h1>
        </div>
      </div>
      <div class="footer-copyright" id="footer-copyright">&copy;2026 Darshan Naidu. All rights reserved.</div>
    </section>

    <div id="work-selection-page" style="display: none;">
      <!-- Work Selection Preloader -->
      <div id="work-selection-preloader" style="display: none;">
        <div class="preloader-counter-work-selection">
          <h1>0</h1>
        </div>
        <div class="preloader-progress-bar-work-selection">
          <div class="preloader-progress-work-selection"></div>
        </div>
      </div>
      <section class="slider slider--work-selection" id="work-selection-slider">
        <div class="slider-images" id="slider-images-ws">
          <img src="/work-section/slider_img_1.webp" alt="Slide 1" />
        </div>
        <div class="slider-title" id="slider-title-ws">
          <h1>Rhythm &amp; Motion</h1>
        </div>
        <div class="slider-indicator" id="slider-indicator-ws">
          <div class="slider-indices-wrapper" id="slider-indices-wrapper-ws">
            <div class="slider-progress-bar" id="slider-progress-bar-container-ws">
              <div class="slider-progress" id="slider-progress-bar-ws"></div>
            </div>
            <div class="slider-indices" id="slider-indices-ws"></div>
          </div>
          <div class="slider-number" id="slider-number-ws">
            <span class="current-number" id="current-number-ws">01</span>
          </div>
        </div>
      </section>
    </div>

    <div id="project-page" style="display: none;">
      <!-- Project Preloader -->
      <div id="project-preloader" style="display: none;">
        <div class="preloader-counter-projects">
          <h1>0</h1>
        </div>
        <div class="preloader-progress-bar-projects">
          <div class="preloader-progress-projects"></div>
        </div>
      </div>

      <!-- Main Title Section -->
      <section class="project-title-section" id="project-title-section">
        <h1 class="project-main-title" id="hero-title">Rhythm &amp; Motion,<br>Instagram Reels</h1>
        <div class="project-number-wrapper" id="project-number-wrapper">
          <div class="project-number" id="project-number"><span class="no-prefix">No.</span>1</div>
        </div>
      </section>

      <!-- Hero Image -->
      <section class="project-hero-image" id="project-hero-image-container">
        <div class="hero-image-inner" id="project-hero-image">
        </div>
      </section>

      <!-- Project Info Section -->
      <section class="project-info-section" id="project-info-section">
        <div class="project-description-wrapper" id="project-description-wrapper">
          <p id="project-description">High-energy video editing, relentless pacing, and kinetic storytelling designed for the infinite scroll. From punchy 9:16 vertical hooks to widescreen cinematic films, I turn raw footage into unforgettable visual experiences.</p>
        </div>
        <div class="project-metadata" id="project-metadata">
          <div class="project-metadata-wide">
            <div class="metadata-item brand">
              <span class="metadata-label">(Category)</span>
              <span class="metadata-value" id="project-brand">Instagram Reels</span>
            </div>
            <div class="metadata-item role">
              <span class="metadata-label">(Role)</span>
              <span class="metadata-value" id="project-role">Video Editing · Motion · Direction</span>
            </div>
          </div>
          <div class="project-metadata-right">
            <div class="metadata-item location">
              <span class="metadata-label">(Location)</span>
              <span class="metadata-value" id="project-location">India</span>
            </div>
            <div class="metadata-item year">
              <span class="metadata-label">(Year)</span>
              <span class="metadata-value" id="project-year">24-26</span>
            </div>
          </div>
        </div>
      </section>

      <!-- Project Images Grid -->
      <section class="project-images-grid" id="project-images">
      </section>

      <!-- Footer / Next Project Section -->
      <footer class="project-footer" id="project-footer">
        <div class="footer-header-wrapper" id="project-footer-header">
          <h1 class="next-project-main-title" id="next-project-title">Visual Archive,<br>Poster Collection</h1>
          <div class="next-project-number-wrapper" id="next-project-number-wrapper">
            <div class="next-project-number" id="next-project-number"><span class="next-prefix">Next.</span>2</div>
          </div>
        </div>
        
        <div class="next-project-progress" id="next-project-progress-container">
          <div class="next-project-progress-bar" id="next-progress-bar"></div>
        </div>
      </footer>
    </div>

    </div><!-- #smooth-wrapper -->

  </body>
</html>'''

files = ["index.html", "works.html", "about.html", "instagram-reels.html", "poster-archive.html", "reels.html", "triadlight.html", "itmatters.html"]
for name in files:
    with open(name, "w") as f:
        f.write(html_template)

print("✅ Saved all 8 HTML files with pretty formatted code, full SEO/metas, new favicons, and Darshan Naidu creative copy!")
