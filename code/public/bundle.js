// This script should only run once.
// We set a flag on the window object to prevent re-execution if the script is loaded twice.
if (window.aimaBundleLoaded) {
    console.warn("AIMA: bundle.js already loaded. Aborting duplicate execution.");
} else {
    window.aimaBundleLoaded = true;

    // Terms and Conditions Cookie Handler
    // Initialize with default values. These will be overwritten by ui_config.json if it loads.
    let cookieConfig = {
        name: "accepted_terms",
        durationDays: 365,
        path: "/"
    };

    // Function to set/merge cookie configuration from the fetched JSON
    function setCookieConfig(config) {
        // Merge provided config over the existing defaults.
        cookieConfig = { ...cookieConfig, ...config };
    }

    function setTermsCookie() {
        const maxAge = cookieConfig.durationDays * 24 * 60 * 60; // Convert days to seconds
        document.cookie = `${cookieConfig.name}=true; path=${cookieConfig.path}; max-age=${maxAge}`;
        // Remove terms CSS immediately when cookie is set
        loadTermsCSS();
        setTimeout(() => window.location.reload(), 1000);
    }

    // Check if terms are accepted
    function checkTermsAccepted() {
        const cookieName = cookieConfig.name;
        const hasAccepted = document.cookie.split("; ").find(row => row.startsWith(cookieName + "="));
        return hasAccepted !== undefined;
    }

    // Load terms.css if cookie is not accepted
    function loadTermsCSS() {
        if (!checkTermsAccepted()) {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.type = 'text/css';
            link.href = './public/css/terms.css';
            link.id = 'terms-css';

            // Check if the CSS is already loaded
            if (!document.getElementById('terms-css')) {
                document.head.appendChild(link);
            }
        }
    }

    // Listen for accept_terms_button action clicks
    document.addEventListener('DOMContentLoaded', function() {
        // Load terms CSS if cookie is not accepted
        loadTermsCSS();
        // Monitor for action button clicks
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.type === 'childList') {
                    mutation.addedNodes.forEach(function(node) {
                        if (node.nodeType === Node.ELEMENT_NODE) {
                            // Looks for the accept terms button
                            const acceptBtn = document.getElementById('accept_terms_btn');
                            if (acceptBtn && !acceptBtn.hasAttribute('data-terms-handled')) {
                                acceptBtn.setAttribute('data-terms-handled', 'true');
                                acceptBtn.addEventListener('click', function() {
                                    setTermsCookie();
                                });
                            }
                        }
                    });
                }
            });
        });

        // Start observing
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    });

    // Hides a div if the accept terms button exists.
    function monitorAndHideDiv() {
        const TARGET_DIV_SELECTOR = '.flex.flex-col.mx-auto.w-full.p-4.pt-0';

        const checkAndToggleVisibility = () => {
            const buttonExists = document.getElementById('accept_terms_btn');
            const targetDiv = document.querySelector(TARGET_DIV_SELECTOR);
            if (!targetDiv) return;
            targetDiv.classList.toggle('hidden', buttonExists);
        };

        const observer = new MutationObserver(checkAndToggleVisibility);
        observer.observe(document.body, {
            childList: true,
            subtree: true,
            characterData: true
        });

        // Initial check on load
        checkAndToggleVisibility();
    }

    monitorAndHideDiv();

    // Global functions to be called from Chainlit
    window.setTermsCookie = setTermsCookie;
    window.checkTermsAccepted = checkTermsAccepted;
    window.setCookieConfig = setCookieConfig;
    window.loadTermsCSS = loadTermsCSS;

    // --- AIMA UI Initialization ---

    // Define global variables for UI elements to be accessible by helper functions
    let footer;
    let Heading;

    // This single event listener runs when the entire page is loaded
    window.addEventListener("load", async function initializeAimaUI() {
      try {
        // 1. Fetch UI configuration files
        let config = {};
        let uiVars = {};
        try {
            const configResponse = await fetch('/public/ui_config.json');
            if (configResponse.ok) {
                config = await configResponse.json();
            } else {
                console.error('AIMA: Failed to fetch ui_config.json:', configResponse.statusText);
            }
            const varsResponse = await fetch('/public/ui_vars.json');
            if (varsResponse.ok) {
                uiVars = await varsResponse.json();
            }
        } catch (error) {
            console.error('AIMA: Error fetching configuration files:', error);
        }

        // 2. Determine the correct last_updated value with clear priority
        // Use ui_config.json if it has a non-empty value, otherwise fall back to ui_vars.json
        const lastUpdated = (config.last_updated && config.last_updated.trim() !== "")
            ? config.last_updated
            : uiVars.last_updated;

        // 3. Apply/merge Cookie Config from JSON
        setCookieConfig(config.cookieConfig);

        // 4. Create or Update Footer
        if (config.footer) {
            // Pass the config and the definitive lastUpdated value
            createOrUpdateFooter(config, lastUpdated);
        }

        // 5. Create and configure the heading from JSON
        if (config.heading && config.heading.enabled) {
          Heading = document.createElement("div");
          Heading.id = "beta-heading";
          Heading.textContent = config.heading.text;
          const defaultHeadingStyles = {
            position: "fixed", top: "0", left: "50%", width: "50%",
            transform: "translateX(-50%)", textAlign: "center", fontWeight: "bold",
            zIndex: "10", padding: "18px 0 4px 0", letterSpacing: "1px"
          };
          const combinedStyles = { ...defaultHeadingStyles, ...config.heading.styles };
          Object.assign(Heading.style, combinedStyles);
          if (config.heading.styles && config.heading.styles.fontFamily) {
            Heading.style.setProperty("font-family", config.heading.styles.fontFamily, "important");
          }
          document.body.appendChild(Heading);
        }

        // 6. Set up the logic to show/hide elements when the policy is viewed
        waitForReadmeButton();

      } catch (error) {
        // On error, the default cookieConfig will be used.
        console.error('AIMA: Error initializing UI from config:', error);
      }
    });

    // Helper functions to control UI element visibility
    function hideHeading() {
      if (Heading) Heading.style.display = "none";
    }
    function showHeading() {
      if (Heading) Heading.style.display = "block";
    }
    function hideFooter() {
      if (footer) footer.style.display = "none";
    }
    function showFooter() {
      if (footer) footer.style.display = "flex";
    }

    // Waits for the readme button to exist, then sets up an observer
    function waitForReadmeButton() {
      const readmeButton = document.getElementById("readme-button");
      if (readmeButton) {
        const checkStateAndToggleUI = () => {
          const isExpanded = readmeButton.getAttribute("aria-expanded") === "true";
          if (isExpanded) {
            hideHeading();
            hideFooter();
          } else {
            showHeading();
            showFooter();
          }
        };
        const observer = new MutationObserver(checkStateAndToggleUI);
        observer.observe(readmeButton, { attributes: true, attributeFilter: ["aria-expanded"] });
        checkStateAndToggleUI(); // Initial check
      } else {
        setTimeout(waitForReadmeButton, 100);
      }
    }
} // End of the main execution block

// 3. Create or Update Footer
function createOrUpdateFooter(config, lastUpdated) {
    let footer = document.getElementById("app-footer");
    if (!footer) {
        footer = document.createElement("div");
        footer.id = "app-footer";
        document.body.appendChild(footer);
    }

    // Build footer links HTML from config
    let linksHTML = '';
    if (config.footer && config.footer.links) {
        linksHTML = Object.values(config.footer.links).map(link =>
            `·<a href="${link.href}" target="_blank">${link.text}</a>`
        ).join('');
    }

    // Determine the version/date string from the definitive value passed in
    let versionText = "";
    if (lastUpdated) {
        versionText = `· v${lastUpdated}`;
    }
    
    const copyrightText = (config.footer && config.footer.copyright) ? config.footer.copyright : '';

    footer.innerHTML = `<span>${copyrightText}${linksHTML}${versionText}</span>`;

    // Style the footer and its links
    updateFooterStyle(footer);
}

// 4. Update Footer Styling (handles dark mode)
function updateFooterStyle(footerElement) {
    const footerHeight = 18;
    const isDark = document.documentElement.classList.contains("dark");
    const root = document.querySelector("#root") || document.body;
    const appBackgroundColor = getComputedStyle(root).backgroundColor;

    Object.assign(footerElement.style, {
        position: "fixed", bottom: "0", left: "0", width: "100%",
        background: appBackgroundColor,
        color: isDark ? "#ccc" : "#999",
        borderTop: `0px solid ${isDark ? "#444" : "#eee"}`,
        fontSize: "12px", zIndex: "1000", height: `${footerHeight}px`,
        display: "flex", justifyContent: "center", alignItems: "center", gap: "10px"
    });
    footerElement.querySelectorAll("a").forEach(link => {
        link.style.color = isDark ? "#ccc" : "#999";
        link.style.margin = "0 5px";
        link.style.textDecoration = "none";
    });
}
