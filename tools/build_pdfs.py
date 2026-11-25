"""Regenerate both embedded PDF downloads from the current bilingual HTML."""
import base64
import os
import re
import textwrap
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'index.html'


def main():
    source = INDEX.read_text(encoding='utf-8')
    pdfs = {}
    with sync_playwright() as playwright:
        executable = os.environ.get('CHROMIUM_PATH')
        browser = playwright.chromium.launch(**({'executable_path': executable} if executable else {}))
        try:
            for language in ('de', 'en'):
                page = browser.new_page(locale='en-US', viewport={'width': 1440, 'height': 900}, color_scheme='light')
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.set_content(source, wait_until='load')
                if page.locator('html').get_attribute('lang') != language:
                    page.locator('#langBtn').click()
                assert page.locator('html').get_attribute('lang') == language
                assert not errors, errors
                pdfs[language] = page.pdf(print_background=True, prefer_css_page_size=True)
                page.close()
        finally:
            browser.close()
    for language, pdf in pdfs.items():
        assert pdf.startswith(b'%PDF-')
        encoded = '\n'.join(textwrap.wrap(base64.b64encode(pdf).decode('ascii'), 120))
        pattern = rf'(<script type="text/plain" id="pdf-{language}">).*?(</script>)'
        source, count = re.subn(pattern, lambda match: match[1] + '\n' + encoded + '\n' + match[2], source, flags=re.S)
        if count != 1:
            raise RuntimeError(f'Expected one embedded PDF block for {language}; got {count}')
    INDEX.write_text(source, encoding='utf-8')
    for language, pdf in pdfs.items():
        (ROOT / f'Christoph_Grossklaus_CV_{language.upper()}.pdf').write_bytes(pdf)
        print(f'Generated {language.upper()}: {len(pdf):,} bytes')


if __name__ == '__main__':
    main()
