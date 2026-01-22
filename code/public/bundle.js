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
        injectHeaderLogo();
        setTimeout(() => window.location.reload(), 1000);
    }

    // Check if terms are accepted
    function checkTermsAccepted() {
        // Always return true to disable terms check
        return true;
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
    document.addEventListener('DOMContentLoaded', function () {
        // Normalize markup to avoid validator complaints from dynamic UI
        scheduleMarkupNormalization();
        ensureWelcomeLinkStyles();
        applyPolicyLinkStyling();

        // Load terms CSS if cookie is not accepted (DISABLED)
        // loadTermsCSS();
        // Monitor for action button clicks
        const observer = new MutationObserver(function (mutations) {
            mutations.forEach(function (mutation) {
                if (mutation.type === 'childList') {
                    mutation.addedNodes.forEach(function (node) {
                        if (node.nodeType === Node.ELEMENT_NODE) {
                            // Looks for the accept terms button
                            const acceptBtn = document.getElementById('accept_terms_btn');
                            if (acceptBtn && !acceptBtn.hasAttribute('data-terms-handled')) {
                                acceptBtn.setAttribute('data-terms-handled', 'true');
                                acceptBtn.addEventListener('click', function () {
                                    setTermsCookie();
                                });
                            }
                            scheduleMarkupNormalization();
                            ensureWelcomeLinkStyles();
                            applyPolicyLinkStyling();
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

    // monitorAndHideDiv();

    function normalizeMarkup(root) {
        const scope = root || document;
        // Remove obsolete style type attributes to satisfy validators.
        scope.querySelectorAll('style[type]').forEach((styleEl) => {
            styleEl.removeAttribute('type');
        });
        // Ensure button children are phrasing content.
        scope.querySelectorAll('button').forEach((button) => {
            Array.from(button.children).forEach((child) => {
                if (child.tagName === 'DIV' || child.tagName === 'P') {
                    const span = document.createElement('span');
                    Array.from(child.attributes).forEach((attr) => {
                        span.setAttribute(attr.name, attr.value);
                    });
                    while (child.firstChild) {
                        span.appendChild(child.firstChild);
                    }
                    child.replaceWith(span);
                }
            });
        });
        // Ensure span children are phrasing content.
        scope.querySelectorAll('span').forEach((span) => {
            Array.from(span.children).forEach((child) => {
                if (child.tagName === 'P' || child.tagName === 'DIV') {
                    const inlineSpan = document.createElement('span');
                    Array.from(child.attributes).forEach((attr) => {
                        inlineSpan.setAttribute(attr.name, attr.value);
                    });
                    while (child.firstChild) {
                        inlineSpan.appendChild(child.firstChild);
                    }
                    child.replaceWith(inlineSpan);
                }
            });
        });
        // Remove aria-controls pointing to non-existent IDs.
        scope.querySelectorAll('[aria-controls]').forEach((el) => {
            const targetId = el.getAttribute('aria-controls');
            if (targetId && !document.getElementById(targetId)) {
                el.removeAttribute('aria-controls');
            }
        });
    }

    let normalizeQueued = false;
    function scheduleMarkupNormalization() {
        if (normalizeQueued) return;
        normalizeQueued = true;
        window.requestAnimationFrame(() => {
            normalizeQueued = false;
            normalizeMarkup(document);
            if (window.cl_shadowRootElement) {
                normalizeMarkup(window.cl_shadowRootElement);
            }
            ensureWelcomeLinkStyles();
            applyPolicyLinkStyling();
        });
    }

    function ensureWelcomeLinkStyles() {
        const styleId = 'ubi-welcome-link-style';
        const css = [
            '.ubi-welcome-link {',
            '  color: #232e58 !important;',
            '  font-weight: 700 !important;',
            '  text-decoration: none !important;',
            '  position: relative !important;',
            '  padding-left: 1.1em !important;',
            '  display: inline-block !important;',
            '}',
            '.ubi-welcome-link::before {',
            '  content: "" !important;',
            '  position: absolute !important;',
            '  left: 0 !important;',
            '  top: 0.15em !important;',
            '  width: 0.9em !important;',
            '  height: 0.9em !important;',
            '  background-repeat: no-repeat !important;',
            '  background-size: contain !important;',
            '  background-image: url("data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\' fill=\'none\' stroke=\'%23232e58\' stroke-width=\'2\' stroke-linecap=\'round\' stroke-linejoin=\'round\'><path d=\'M10 13a5 5 0 0 1 0-7l2-2a5 5 0 1 1 7 7l-2 2\'/><path d=\'M14 11a5 5 0 0 1 0 7l-2 2a5 5 0 1 1-7-7l2-2\'/></svg>") !important;',
            '}',
            '.ubi-welcome-link--external::before {',
            '  background-image: url("data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\' fill=\'none\' stroke=\'%23232e58\' stroke-width=\'2\' stroke-linecap=\'round\' stroke-linejoin=\'round\'><path d=\'M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6\'/><path d=\'M15 3h6v6\'/><path d=\'M10 14 21 3\'/></svg>") !important;',
            '}',
            '.ubi-welcome-link:hover, .ubi-welcome-link:focus {',
            '  text-decoration-line: underline !important;',
            '  text-decoration-thickness: 2px !important;',
            '  text-decoration-style: solid !important;',
            '}'
            ,
            '.ubi-welcome-link:active, .ubi-welcome-link:visited {',
            '  text-decoration: none !important;',
            '}'
        ].join('\n');

        const inject = (root) => {
            if (!root) return;
            const existing = root.getElementById
                ? root.getElementById(styleId)
                : root.querySelector(`#${styleId}`);
            if (existing) return;
            const styleEl = document.createElement('style');
            styleEl.id = styleId;
            styleEl.textContent = css;
            if (root.head) {
                root.head.appendChild(styleEl);
            } else {
                root.appendChild(styleEl);
            }
        };

        inject(document);
        if (window.cl_shadowRootElement) {
            inject(window.cl_shadowRootElement);
        }
    }

    function applyPolicyLinkStyling() {
        const applyInRoot = (root) => {
            if (!root || !root.querySelectorAll) return;
            const headings = Array.from(root.querySelectorAll('h1, h2, h3'));
            const policyHeading = headings.find((heading) => {
                const text = heading.textContent || '';
                return text.toLowerCase().includes('nutzungsbedingungen');
            });
            if (!policyHeading) return;
            const container =
                policyHeading.closest('[role="dialog"]') ||
                policyHeading.closest('article') ||
                policyHeading.closest('section') ||
                policyHeading.parentElement;
            if (!container) return;
            container.querySelectorAll('a').forEach((link) => {
                link.classList.add('ubi-welcome-link');
                const href = link.getAttribute('href') || '';
                if (/^https?:\/\//i.test(href)) {
                    link.classList.add('ubi-welcome-link--external');
                }
            });
        };

        applyInRoot(document);
        if (window.cl_shadowRootElement) {
            applyInRoot(window.cl_shadowRootElement);
        }
    }

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
                    window.aimaConfig = config; // Expose config globally
                    updateWelcomeText(); // Update text if welcome screen is already visible
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

            // 7. Inject Header Logo if terms accepted
            injectHeaderLogo();

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
    // } // End of the main execution block (Moved to end of file)

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

    // --- Welcome Screen Customization ---

    function injectWelcomeStyles() {
        const styleId = 'welcome-screen-styles';
        if (document.getElementById(styleId)) return;

        const style = document.createElement('style');
        style.id = styleId;
        style.textContent = `
        .speech-bubble {
            display: inline-block;
            flex: 1;
            padding: 12px 12px;
            background: #e8e8e8;
            border-radius: 12px;
            font-family: system-ui, sans-serif;
            position: relative;
            color: #000;
            margin-left: 20px;
            margin-top: 40px;
        }

        .speech-bubble::after {
            content: "";
            position: absolute;
            left: -10px;
            top: 18px;
            width: 0;
            height: 0;
            border-top: 10px solid transparent;
            border-bottom: 10px solid transparent;
            border-right: 10px solid #e8e8e8;
        }

        .custom-welcome-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            gap: 20px;
        }

        .welcome-header {
            display: flex;
            align-items: flex-start;
            justify-content: center;
            width: 100%;
            animation: fadeIn 0.5s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }

        .avatar {
            transition: transform 0.3s ease-in-out;
        }

        .avatar:hover {
            animation: float 2s ease-in-out infinite;
            cursor: pointer;
        }
        .logo {
            display: none;
        }

        .header-logo {
            width: 10%;
            height: 98px;
            background-repeat: no-repeat;
            background-size: contain;
            margin-bottom: 20px;
            order: 0;
            position: absolute;
            top: 0;
            left: 0;
            z-index: 150;
            margin-top: 60px;
            margin-left: 5%;
        }

        /* Default (Light Mode) */
        .header-logo {
            background-image: url('/logo?theme=light');
        }

        /* Dark Mode */
        .dark .header-logo {
            background-image: url('/logo?theme=dark');
        }

        @media (max-width: 1250px) {
            .header-logo {
                height: 49px;
            }
        }

        @media (max-width: 400px) {
            .header-logo {
                height: 24px;
            }
        }
    `;
        document.head.appendChild(style);
    }

    function injectHeaderLogo() {
        // if (!checkTermsAccepted()) return; // checkTermsAccepted is now always true, but we want logo regardless or logic might need adjustment. 
        // Assuming we always want logo if it was previously conditional on terms. 
        // But original code said: "Inject Header Logo if terms accepted". So yes.

        const logoId = 'global-header-logo';
        if (document.getElementById(logoId)) return;

        injectWelcomeStyles(); // Ensure styles are loaded

        const link = document.createElement('a');
        link.href = 'https://www.bib.uni-mannheim.de/';
        link.target = '_blank';
        link.rel = 'noopener noreferrer';

        const logoDiv = document.createElement('div');
        logoDiv.id = logoId;
        logoDiv.className = 'header-logo';

        link.appendChild(logoDiv);
        document.body.appendChild(link);
    }

    function parseMarkdown(text) {
        if (!text) return "";
        let html = text
            // Bold (**text**)
            .replace(/\*\*(.*?)\*\*/g, '<b>$1</b>')
            // Italic (*text*)
            .replace(/\*(.*?)\*/g, '<i>$1</i>')
            // Link ([text](url))
            .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank">$1</a>')
            // Newlines
            .replace(/\n/g, '<br>');
        return html;
    }

    function updateWelcomeText() {
        const bubble = document.querySelector('.speech-bubble');
        if (bubble && window.aimaConfig && window.aimaConfig.welcome_message) {
            bubble.innerHTML = parseMarkdown(window.aimaConfig.welcome_message);
        }
    }

    function getWelcomeHTML() {
        let welcomeMessage = "Hello, i am UBi, the KI-Chatbot of the University Library Mannheim. How can i help you?";
        if (window.aimaConfig && window.aimaConfig.welcome_message) {
            welcomeMessage = parseMarkdown(window.aimaConfig.welcome_message);
        }

        return `
        <div class="custom-welcome-container">
            <div class="welcome-header">
                <div class="avatar-wrapper">
                    <img src="/avatars/assistant_big" alt="avatar" class="avatar w-[200px] mb-2">
                </div>
                <div class="speech-bubble">
                    ${welcomeMessage}
                </div>
            </div>
        </div>
    `;
    }

    // Handle Readme Link Clicks
    document.addEventListener('click', function (e) {
        // Check if the clicked element is a link with href="/readme"
        const target = e.target.closest('a');
        if (target && target.getAttribute('href') === '/readme') {
            e.preventDefault();
            const readmeBtn = document.getElementById('readme-button');
            if (readmeBtn) {
                readmeBtn.click();
            } else {
                console.warn('AIMA: readme-button not found.');
            }
        }
    });

    // ... existing observer code ...
    function customizeWelcomeScreen() {
        const allButtons = Array.from(document.querySelectorAll('button'));

        // Find the default starter button (Öffnungszeiten)
        // Since we are not replacing the container anymore, the default button will be present.
        const defaultStarter = allButtons.find(btn => btn.textContent.includes("Öffnungszeiten"));

        if (defaultStarter) {
            const startersContainer = defaultStarter.parentElement;
            if (startersContainer) {
                let targetContainer = startersContainer;
                // Traverse up to find the main container
                let depth = 0;
                while (targetContainer && targetContainer.parentElement && !targetContainer.classList.contains('flex-col') && depth < 5) {
                    targetContainer = targetContainer.parentElement;
                    depth++;
                }

                // The structure is usually: Button -> Div (Starters) -> Div (Welcome)
                const containerToModify = startersContainer.parentElement;

                if (containerToModify && !containerToModify.getAttribute('data-custom-welcome')) {
                    containerToModify.setAttribute('data-custom-welcome', 'true');
                    injectWelcomeStyles();
                    // Prepend the custom welcome header to the existing content
                    containerToModify.insertAdjacentHTML('afterbegin', getWelcomeHTML());

                    // We don't need setupWelcomeScreenInteractions anymore as we are using default items
                }
            }
        }
    }

    const welcomeObserver = new MutationObserver((mutations) => {
        customizeWelcomeScreen();
    });

    welcomeObserver.observe(document.body, {
        childList: true,
        subtree: true
    });
}
