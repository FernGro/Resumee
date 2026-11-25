# Christoph Grossklaus — CV & Portfolio

Bilingual, responsive CV website (DE / EN), hosted on GitHub Pages. All images are embedded; no runtime dependency or build step.

## Live site

https://ferngro.github.io/Resumee/

Select a language via the toolbar or `?lang=de` / `?lang=en`. The theme follows the OS unless changed manually.

## Interactive terminal

On entry to the overview, the same terminal element initially fills the viewport, types `cd Resumee` letter by letter, acknowledges Enter and animates to its measured dock below the header. The full sequence takes about 2.5 seconds. Escape or Skip dismisses it. Section changes animate the corresponding `cd` command; reduced-motion preferences and direct section links avoid the full intro.

Type `help` or open the searchable command palette with Ctrl/Cmd+K. Supported commands include `ls`, `cd projects`, `open Resumee`, `whoami`, `cat profile`, `status`, `contact`, `pdf`, `timeline`, `git status`, `run security-analysis`, `recruiter` and `clear`. All commands are explicitly handled; no arbitrary shell or eval is exposed.

- `git status`: fetches public metadata for three selected repositories only when requested; no token, fallback on API failure.
- `run security-analysis`: interactive deterministic example using synthetic firmware versions, not a real advisory or LLM.
- `timeline`: reads the current education and experience entries.
- `?view=recruiter`: opens a quiet version without the intro or motion. The terminal command toggles quiet mode during the current visit.

The terminal stays compact; output is shown on demand and dismissible.

## CV and PDF export

- PDF buttons generate a searchable, text-based A4 PDF in the browser when clicked. No embedded snapshots or server-side PDF service.
- The print action uses a dedicated HTML print layout populated from the same current content.
- Export reads the currently selected language directly from the website DOM: experience, education, skills, projects, motivation, creative experience, contact and languages.
- Additional entries in the existing sections are automatically included; pagination adds pages rather than reducing font size. The first PDF page has a restrained terminal title bar, separated name/contact and portrait areas; the body uses numbered section headings and a timeline rail. The portrait is converted locally to JPEG and embedded into the searchable PDF; the gallery is intentionally omitted. The browser print fallback also includes the portrait.
- Date and earliest availability are evaluated in Europe/Berlin. Availability uses the current month plus five months, on the first day (one application lead month plus three full notice months after that lead month; e.g. November 2026 → April 1, 2027). Review this policy if notice terms change.
- The PDF date is the generation date, not a claim that the biographical content was reviewed on that date.

## Updating content

Edit the English HTML in `index.html` and its corresponding German entries in the translation groups. For added records, keep translation arrays in the same order as the matched elements. Missing translations fall back to English and log a warning. The export automatically reads the updated text; no manual PDF rebuild is required.

When adding an entirely new panel, use a section with a heading and article/card elements with h3 and p/li content. Review its exported layout.

The previous static PDF build workflow is obsolete. `tools/build_pdfs.py` now exports both live print layouts locally for testing, without changing the HTML.

## Verification

Runtime date boundary cases and simulated lossless pagination were checked when implementing the generator. The terminal redesign was checked with the actual PDF drawing function, representative German text, cross-reference offsets, and synthetic image-resource wiring. Live browser rendering, actual portrait conversion, Safari/iOS downloads, and visual print layout still need regression testing.

Terminal v5 verification: all inline scripts parsed; stub-DOM tests exercised initial typing, measured dock target, cleanup, route changes, replay, skip and help. Real-browser CSS animation, Safari/iOS and the public deployment still require visual end-to-end verification.
