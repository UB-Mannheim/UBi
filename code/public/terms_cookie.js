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
