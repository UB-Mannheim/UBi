#!/usr/bin/env python3
"""
HTML Template Modifier for Chainlit
Replaces external resources with local assets in Chainlit's HTML template.
"""

import importlib.util
import shutil
from pathlib import Path


def get_chainlit_frontend_path():
    """Find the Chainlit frontend directory in the current Python environment."""
    # Method 1: Use importlib.util to find chainlit without importing
    spec = importlib.util.find_spec("chainlit")
    if spec and spec.origin:
        chainlit_path = Path(spec.origin).parent
        frontend_path = chainlit_path / "frontend/dist/"
        if frontend_path.exists():
            return frontend_path

    # Method 2: Search in common virtual environment locations
    import sys

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    ):
        # We're in a virtual environment
        site_packages = Path(sys.prefix) / "lib"

        # Look for site-packages in common locations
        for python_dir in site_packages.glob("python*"):
            chainlit_path = python_dir / "site-packages" / "chainlit"
            if chainlit_path.exists():
                return chainlit_path / "frontend"

    # Method 3: Search in system site-packages
    for site_package in sys.path:
        if "site-packages" in site_package:
            chainlit_path = Path(site_package) / "chainlit"
            if chainlit_path.exists():
                return chainlit_path / "frontend"

    # Method 4: Fallback - try to import and get path
    try:
        import chainlit

        return Path(chainlit.__file__).parent / "frontend"
    except ImportError:
        raise FileNotFoundError("Could not find Chainlit installation")


def backup_original_template(frontend_path):
    """Create a backup of the original index.html."""
    index_html = frontend_path / "index.html"
    backup_path = frontend_path / "index.html.backup"

    if index_html.exists() and not backup_path.exists():
        shutil.copy2(index_html, backup_path)


def create_modified_template(frontend_path):
    """Create a modified version of index.html with local assets."""
    index_html = frontend_path / "index.html"

    # Read the original template
    with open(index_html, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace external resources with local ones
    font_start = (
        "<!-- FONT START -->\n    <link\n      "
        'href="https://fonts.googleapis.com/css2?family=Inter:'
        'wght@400;500;700&display=swap"\n      rel="stylesheet"\n    />\n    '
        "<!-- FONT END -->"
    )
    font_replacement = (
        "<!-- LOCAL FONTS START -->\n    "
        '<link rel="stylesheet" href="/public/css/fonts.css" />\n    '
        "<!-- LOCAL FONTS END -->"
    )
    modified_content = content.replace(font_start, font_replacement)

    katex_original = (
        '<link\n      rel="stylesheet"\n      '
        'href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/'
        'katex.min.css"\n    />'
    )
    katex_replacement = (
        '<link rel="stylesheet" href="/public/css/katex.min.css" />'
    )
    modified_content = modified_content.replace(
        katex_original, katex_replacement
    )

    # Remove preconnect links to external domains
    preconnect_links = (
        '<link rel="preconnect" href="https://fonts.googleapis.com" />\n    '
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />'
    )
    modified_content = modified_content.replace(
        preconnect_links, "<!-- External preconnect links removed -->"
    )

    # Write the modified template
    with open(index_html, "w", encoding="utf-8") as f:
        f.write(modified_content)


def restore_original_template(frontend_path):
    """Restore the original template from backup."""
    index_html = frontend_path / "index.html"
    backup_path = frontend_path / "index.html.backup"

    if backup_path.exists():
        shutil.copy2(backup_path, index_html)
        print(f"✅ Restored original template: {index_html}")
    else:
        print("❌ No backup found to restore")


def main():
    """Main function to modify the HTML template."""

    # Find Chainlit frontend path
    frontend_path = get_chainlit_frontend_path()
    if not frontend_path.exists():
        return False

    backup = frontend_path / "index.html.backup"
    if backup.exists():
        return

    # Check if we have our local assets
    local_css_path = Path("public/css")
    if not local_css_path.exists():
        print(f"❌ Local CSS directory not found: {local_css_path}")
        return False

    required_files = ["fonts.css", "katex.min.css"]
    missing_files = [
        f for f in required_files if not (local_css_path / f).exists()
    ]

    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False

    # Create backup and modify template
    backup_original_template(frontend_path)
    create_modified_template(frontend_path)

    print("\n🎉 Template modification completed!")

    return True


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
