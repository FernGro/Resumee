# Christoph Grossklaus — CV & Portfolio

Bilingual, responsive CV website (DE / EN). The self-contained `index.html` includes all photos and both PDF downloads. No external runtime libraries or build step required. The separate print action generates the CV from the currently displayed language.

## GitHub Pages

1. Open **Settings → General**. A public repository supports GitHub Pages with GitHub Free; private repository support depends on the GitHub plan.
2. Open **Settings → Pages**.
3. Select **Deploy from a branch**, branch `main`, folder `/ (root)`, then **Save**.
4. After the Pages deployment succeeds, open https://ferngro.github.io/Resumee/.

The repository contains a personal portfolio. The public version intentionally contains email and LinkedIn but no phone number. Review all personal and professional information before making it public.

## Updating content and PDF downloads

The English HTML and German translations are in `index.html`. Update both when changing CV data. To regenerate both PDF downloads from the current site:

```bash
python -m pip install playwright
python -m playwright install chromium
python tools/build_pdfs.py
```

Commit the updated `index.html`. The generator also creates two standalone PDFs locally. The PDFs are snapshots; the Print / PDF control renders the current website directly.

## Verification

Local Chromium / Playwright checks: desktop and mobile navigation, keyboard tab navigation, German/English toggle, light/dark theme, image loading and gallery navigation, responsive widths (320, 390, 768, 921, 1024, 1151, 1440 px), both actual PDF downloads compared byte-for-byte against the generated files, and three-page print output in both languages. Native Safari/iOS and the actual public Pages URL require separate verification after activation. The PDF build script was run successfully on a temporary copy.
