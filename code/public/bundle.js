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
    setTimeout(() => window.location.reload(), 1000);
}

// Check if terms are accepted
function checkTermsAccepted() {
    const cookieName = cookieConfig.name;
    const hasAccepted = document.cookie.split("; ").find(row => row.startsWith(cookieName + "="));
    return hasAccepted !== undefined;
}

// Listen for accept_terms_button action clicks
document.addEventListener('DOMContentLoaded', function() {
    // Monitor for action button clicks
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList') {
                mutation.addedNodes.forEach(function(node) {
                    if (node.nodeType === Node.ELEMENT_NODE) {  
                        // Also look for the first button that starts with ✅
                        const allButtons = document.querySelectorAll('button');
                        for (let i = 0; i < allButtons.length; i++) {
                            const button = allButtons[i];
                            if (button && !button.hasAttribute('data-terms-handled') && button.textContent.trim().startsWith("✅")) {
                                button.setAttribute('data-terms-handled', 'true');
                                button.addEventListener('click', function() {
                                    console.log('Accept terms button clicked (by emoji)');
                                    setTermsCookie();
                                });
                                break; // Found the first one, stop searching
                            }
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

// Hides a div if a button starting with "✅" exists.
function monitorAndHideDiv() {
    const TARGET_DIV_SELECTOR = '.flex.flex-col.mx-auto.w-full.p-4.pt-0';

    const checkAndToggleVisibility = () => {
        const buttonExists = Array.from(document.querySelectorAll('button'))
                                  .some(btn => btn.textContent.trim().startsWith("✅"));
        
        const targetDiv = document.querySelector(TARGET_DIV_SELECTOR);
        if (!targetDiv) return;
        console.log('buttonExists', buttonExists);
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

// Imprint and Data Protection Declaration
window.addEventListener("load", function () {
  const footer = document.createElement("div");
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
      borderTop: `1px solid ${isDark ? "#444" : "#eee"}`,
      fontSize: "10px",
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
      <a href="https://www.uni-mannheim.de/datenschutzerklaerung/" target="_blank">Datenschutz</a>
    </span>
  `;

  document.body.appendChild(footer);
  updateFooterStyle();

  const appWrapper = document.querySelector("#root") || document.body;
  appWrapper.style.paddingBottom = `${footerHeight + 6}px`;

  const observer = new MutationObserver(() => updateFooterStyle());
  observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["class"]
  });

  // Slight delay to ensure styles are computed correctly after load
  setTimeout(updateFooterStyle, 50);
});
