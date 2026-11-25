# Christoph Grossklaus — CV & Portfolio

Bilingual, responsive CV website (DE / EN), hosted on GitHub Pages. All images are embedded; no runtime dependency or build step.

## Live site

https://ferngro.github.io/Resumee/

Select a language via the toolbar or `?lang=de` / `?lang=en`. The theme follows the OS unless changed manually. Intro motion respects reduced-motion preferences.

## CV and PDF export

- PDF buttons generate a searchable, text-based A4 PDF in the browser when clicked. No embedded snapshots or server-side PDF service.
- The print action uses a dedicated HTML print layout populated from the same current content.
- Export reads the currently selected language directly from the website DOM: experience, education, skills, projects, motivation, creative experience, contact and languages.
- Additional entries in the existing sections are automatically included; pagination adds pages rather than reducing font size. Photos and gallery images are intentionally omitted from the application PDF.
- Date and earliest availability are evaluated in Europe/Berlin. Availability uses the current month plus five months, on the first day (one application lead month plus three full notice months after that lead month; e.g. November 2026 → April 1, 2027). Review this policy if notice terms change.
- The PDF date is the generation date, not a claim that the biographical content was reviewed on that date.

## Updating content

Edit the English HTML in `index.html` and its corresponding German entries in the translation groups. For added records, keep translation arrays in the same order as the matched elements. Missing translations fall back to English and log a warning. The export automatically reads the updated text; no manual PDF rebuild is required.

When adding an entirely new panel, use a section with a heading and article/card elements with h3 and p/li content. Review its exported layout.

The previous static PDF build workflow is obsolete. `tools/build_pdfs.py` now exports both live print layouts locally for testing, without changing the HTML.

## Verification

Runtime date boundary cases and simulated lossless pagination were checked when implementing the generator; PDF object/xref offsets and two-page structure were checked on the initial generator. Live browser rendering, accessibility, Safari/iOS downloads and visual print layout need separate regression testing.
