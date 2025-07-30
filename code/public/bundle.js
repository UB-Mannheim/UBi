// Terms and Conditions Cookie Handler
// Cookie configuration will be set by Python via window.cookieConfig
let cookieConfig = {
    name: "accepted_terms",
    durationDays: 365,
    path: "/"
};

// Function to set cookie configuration from Python
function setCookieConfig(config) {
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
    <span>
      © 2025 UB Mannheim
      <a href="https://www.bib.uni-mannheim.de/impressum/" target="_blank">Impressum</a>
      <a href="https://www.uni-mannheim.de/datenschutzerklaerung/datenschutzinformationen-der-universitaetsbibliothek/" target="_blank">Datenschutz</a>
    </span>
  `;

  document.body.appendChild(footer);
  updateFooterStyle();

  const observer = new MutationObserver(() => updateFooterStyle());
  observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["class"]
  });

  // Slight delay to ensure styles are computed correctly after load
  setTimeout(updateFooterStyle, 50);
});

// Add BETA-Version heading at the top center
window.addEventListener("load", function () {
  const betaHeading = document.createElement("div");
  betaHeading.id = "beta-heading";
  betaHeading.textContent = "Testversion des KI-Chats der UB Mannheim";
  Object.assign(betaHeading.style, {
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
  betaHeading.style.setProperty(
    "font-family",
    "SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace",
    "important"
  );
  document.body.appendChild(betaHeading);

  // Functions to show/hide beta heading
  function hideBetaHeading() {
    const heading = document.getElementById("beta-heading");
    if (heading) heading.style.display = "none";

  }
  function showBetaHeading() {
    const heading = document.getElementById("beta-heading");
    if (heading) heading.style.display = "block";

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
        hideBetaHeading();
        hideFooter();
      } else {
        showBetaHeading();
        showFooter();
      }
      // Observe attribute changes
      const observer = new MutationObserver(() => {
        if (readmeButton.getAttribute("aria-expanded") === "true") {
          hideBetaHeading();
          hideFooter();
        } else {
          showBetaHeading();
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
