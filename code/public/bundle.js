// Terms and Conditions Cookie Handler
// Cookie configuration will be loaded from ui_config.json
let cookieConfig = {
    name: "accepted_terms",
    durationDays: 365,
    path: "/"
};

// Configuration data loaded from ui_config.json
let configData = null;

// Function to load configuration from ui_config.json
async function loadConfig() {
    try {
        // Add cache-busting timestamp parameter
        const cacheBuster = new Date().getTime();
        const response = await fetch(`./public/ui_config.json?_=${cacheBuster}`, {
            cache: 'no-cache',
            headers: {
                'Cache-Control': 'no-cache, no-store, must-revalidate',
                'Pragma': 'no-cache'
            }
        });
        if (response.ok) {
            configData = await response.json();
            
            // Update cookie config
            if (configData.cookieConfig) {
                cookieConfig = { ...cookieConfig, ...configData.cookieConfig };
            }
            
            // Update last crawl date if available
            if (configData.last_updated) {
                setLastUpdated(configData.last_updated);
            }
            
            return true;
        }
    } catch (error) {
        console.log('Could not load config from ui_config.json:', error);
    }
    return false;
}

// Function to set cookie configuration from Python (fallback)
function setCookieConfig(config) {
    cookieConfig = { ...cookieConfig, ...config };
}

// Function to set last crawl date from Python
function setLastUpdated(dateString) {
    const lastUpdatedElement = document.getElementById('last-updated');
    if (lastUpdatedElement) {
        lastUpdatedElement.textContent = `Last updated: ${dateString}`;
    }
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
    // Load configuration first
    loadConfig();
    
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

// Imprint and Data Protection Declaration
let footer; // Move footer to higher scope
window.addEventListener("load", function () {
  footer = document.createElement("div");
  const footerHeight = 18;

  function getIsDarkMode() {
    return document.documentElement.classList.contains("dark");
  }

  function getAppBackgroundColor() {
    // Try to get the real background color from the root or body
    const root = document.querySelector("#root") || document.body;
    return getComputedStyle(root).backgroundColor;
  }

  function updateFooterStyle() {
    const isDark = getIsDarkMode();

    Object.assign(footer.style, {
      position: "fixed",
      bottom: "0",
      left: "0",
      width: "100%",
      background: getAppBackgroundColor(),
      color: isDark ? "#ccc" : "#999",
      borderTop: `0px solid ${isDark ? "#444" : "#eee"}`,
      fontSize: "12px",
      zIndex: "1000",
      height: `${footerHeight}px`,
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      gap: "10px"
    });

    footer.querySelectorAll("a").forEach(link => {
      link.style.color = isDark ? "#ccc" : "#999";
      link.style.margin = "0 5px";
      link.style.textDecoration = "none";
    });
  }

  footer.innerHTML = `
    <div style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
      <span></span>
      <span style="text-align: center;" id="footer-content">
        Loading...
      </span>
      <span id="last-updated" style="font-size: 12px; color: #888 !important; opacity: 0.7; font-family: inherit;">
      </span>
    </div>
  `;

  // Function to update footer content from config
  function updateFooterContent() {
    const footerContentSpan = document.getElementById('footer-content');
    if (footerContentSpan && configData && configData.footer) {
      const footer = configData.footer;
      const links = footer.links;
      
      footerContentSpan.innerHTML = `
        ${footer.copyright}
        <a href="${links.impressum.href}" target="_blank">${links.impressum.text}</a>
        <a href="${links.datenschutz.href}" target="_blank">${links.datenschutz.text}</a>
      `;
    }
  }

  document.body.appendChild(footer);
  updateFooterStyle();

  // Load config and update footer content
  loadConfig().then(success => {
    if (success) {
      updateFooterContent();
    } else {
      // Fallback to hardcoded values
      const footerContentSpan = document.getElementById('footer-content');
      if (footerContentSpan) {
        footerContentSpan.innerHTML = `
          © 2025 UB Mannheim
          <a href="https://www.bib.uni-mannheim.de/impressum/" target="_blank">Impressum</a>
          <a href="https://www.uni-mannheim.de/datenschutzerklaerung/datenschutzinformationen-der-universitaetsbibliothek/" target="_blank">Datenschutz</a>
        `;
      }
    }
  });

  const observer = new MutationObserver(() => updateFooterStyle());
  observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["class"]
  });

  // Slight delay to ensure styles are computed correctly after load
  setTimeout(updateFooterStyle, 50);
});

// Add Heading at the top center
window.addEventListener("load", function () {
  const heading = document.createElement("div");
  heading.id = "heading";
  heading.textContent = "Loading...";
  
  // Default styles
  Object.assign(heading.style, {
    position: "fixed",
    top: "0",
    left: "50%",
    width: "50%",
    transform: "translateX(-50%)",
    textAlign: "center",
    fontWeight: "bold",
    fontSize: "18px",
    color: "rgb(0, 149, 255)",
    zIndex: "10",
    padding: "18px 0 4px 0",
    letterSpacing: "1px",
    textShadow: "0 0 22px rgba(0, 102, 255, 0.41)"
  });
  heading.style.setProperty(
    "font-family",
    "SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace",
    "important"
  );
  
  // Function to update heading from config
  function updateHeading() {
    if (configData && configData.heading) {
      const headingConfig = configData.heading;
      
      if (headingConfig.enabled) {
        heading.textContent = headingConfig.text;
        
        // Apply custom styles if provided
        if (headingConfig.styles) {
          Object.assign(heading.style, {
            fontSize: headingConfig.styles.fontSize || "18px",
            color: headingConfig.styles.color || "rgb(0, 149, 255)",
            textShadow: headingConfig.styles.textShadow || "0 0 22px rgba(0, 102, 255, 0.41)"
          });
          
          if (headingConfig.styles.fontFamily) {
            heading.style.setProperty("font-family", headingConfig.styles.fontFamily, "important");
          }
        }
      } else {
        heading.style.display = "none";
      }
    } else {
      // Fallback to default text
      heading.textContent = "Testversion des KI-Chats der UB Mannheim";
    }
  }
  
  document.body.appendChild(heading);
  
  // Load config and update heading
  if (configData) {
    updateHeading();
  } else {
    loadConfig().then(success => {
      if (success) {
        updateHeading();
      }
    });
  }

  // Functions to show/hide heading
  function hideHeading() {
    const headingElement = document.getElementById("heading");
    if (headingElement) headingElement.style.display = "none";

  }
  function showHeading() {
    const headingElement = document.getElementById("heading");
    if (headingElement) headingElement.style.display = "block";

  }

  // Functions to show/hide footer
  function hideFooter() {
    if (footer) footer.style.display = "none";

  }
  function showFooter() {
    if (footer) footer.style.display = "flex";

  }

  // Wait for the readme button to exist
  function waitForReadmeButton() {
    const readmeButton = document.getElementById("readme-button");
    if (readmeButton) {
      // Initial check
      if (readmeButton.getAttribute("aria-expanded") === "true") {
        hideHeading();
        hideFooter();
      } else {
        showHeading();
        showFooter();
      }
      // Observe attribute changes
      const observer = new MutationObserver(() => {
        if (readmeButton.getAttribute("aria-expanded") === "true") {
          hideHeading();
          hideFooter();
        } else {
          showHeading();
          showFooter();
        }
      });
      observer.observe(readmeButton, { attributes: true, attributeFilter: ["aria-expanded"] });
    } else {
      setTimeout(waitForReadmeButton, 100); // Try again in 100ms
    }
  }
  waitForReadmeButton();
});
