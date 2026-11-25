"""Export both live CV layouts for local visual testing; never rewrite index.html."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        try:
            for language in ("de", "en"):
                page = browser.new_page(locale=language, viewport={"width": 1440, "height": 900})
                errors = []
                page.on("pageerror", lambda error: errors.append(str(error)))
                page.goto((ROOT / "index.html").as_uri() + "?lang=" + language)
                assert page.locator("html").get_attribute("lang") == language
                with page.expect_download() as download:
                    page.locator("header [data-pdf]").click()
                target = ROOT / f"Christoph_Grossklaus_CV_{language.upper()}.pdf"
                download.value.save_as(target)
                assert target.read_bytes().startswith(b"%PDF-")
                assert not errors, errors
                print(f"Generated {target.name}: {target.stat().st_size:,} bytes")
                page.close()
        finally:
            browser.close()


if __name__ == "__main__":
    main()
