---
name: readable-copy
description: Turn an uploaded document (PDF, Word, PowerPoint, scanned image, screenshot of a page) into a clean, easy-to-read Word document that keeps the headings, lists and tables but strips the layout clutter, columns, page furniture and images (each image replaced by a short description). Use this skill whenever the user uploads a document and asks to make it readable, easier to read, cleaner, simpler, "just the text", "strip the formatting", "reflow it", or complains that a newsletter, report, flyer, slide deck, brochure, form or magazine is hard to follow. Trigger even when the request is casual or partial, like "can you make this readable" or "this is a mess, tidy it up", and even if the user does not say "Word document". Do not use for summarizing, editing the original file in place, or when the user wants the images kept.
---

# Readable copy

The user reads documents on screen and finds the original layouts hard to follow: multi-column newsletters, sidebars, pull quotes, decorative headers, and pages of photos between paragraphs. The job is to hand back the same content as one clean Word document that reads top to bottom in the right order, with real headings and nothing visual in the way.

Two things make this skill worth having rather than just running a text extractor:

1. **Reading order.** Extractors interleave columns and sidebars, so an article turns to nonsense halfway through. Reconstructing the logical order is the core of the work.
2. **A real check before delivery.** Every source page must be accounted for and every article must read start to finish. The user should never discover a missing section or a broken paragraph themselves.

The user dictates with voice-to-text, so the request may contain odd words. Read for intent. If something in the request is unclear (for example which of two uploaded files to process), ask before starting.

## Workflow

### 1. Inventory the source

Find the upload under `/mnt/user-data/uploads/` and work out what you are dealing with before extracting anything.

| Source type | How to inventory |
|---|---|
| PDF | Read `/mnt/skills/public/pdf-reading/SKILL.md`. Run `pdfinfo`, `pdffonts`, and a one-page `pdftotext` sample. No fonts means it is scanned: use OCR (step 2). |
| Word (.docx) | `pandoc -t markdown file.docx` gives structure-preserving text. Legacy .doc: convert with soffice first (see docx skill). |
| PowerPoint (.pptx) | `markitdown file.pptx` gives one section per slide with titles and notes. |
| Image or scan (.png, .jpg, .heic, photographed page) | Look at the image directly, then OCR with `tesseract image.png out` for the text. |

Note the page or slide count. You will need it for the coverage check at the end.

### 2. Look at every page before trusting the text

Render PDF pages to images (`pdftoppm -jpeg -r 80 file.pdf page`) and view them. For Word and PowerPoint, convert to PDF first with `python /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf file.docx` and render that.

This step is not optional for anything with a designed layout. Looking at the page is the only reliable way to see:

- How many columns there are and where each article starts and ends
- Sidebars, pull quotes, callout boxes and captions that sit inside or beside the main text
- "Continued on page 8" jumps, so the two halves of an article can be rejoined
- Mastheads, page numbers, running headers and footers that repeat on every page
- Which images carry meaning (a chart, an event poster, a photo with a caption) and which are decoration

Make a rough page map as you go: page number, what is on it, and where each piece belongs in the final reading order. This map drives steps 3 and 6.

### 3. Extract and reorder

Pull the text with a method that respects layout. For PDFs, `pdftotext -layout` or `pdfplumber` cropped column by column both work; pick whichever gives clean column separation for that document. For scans, run OCR per page and clean obvious OCR errors that the page image makes unambiguous.

Then rebuild the logical order using the page map:

- Each article or section runs start to finish in one place, with any "continued on" portion pulled back to where it belongs.
- Sidebars and callout boxes become their own short section placed right after the article they relate to, with a heading that says what they are (for example "Sidebar: How to register").
- Pull quotes are dropped if the same sentence already appears in the body. If it does not, keep it as a normal paragraph.
- Join lines that were broken by column width and remove end-of-line hyphenation. A paragraph is one paragraph.

### 4. Strip the page furniture

Remove anything that exists only because of the printed page:

- Page numbers, running headers and footers, repeated mastheads and taglines
- Decorative text, ornaments, "photo by" credits that are not part of a caption
- Ads, unless they carry real information the user might act on (an event date, a contact, a price). In that case keep one plain sentence with the facts and mark it as an ad.
- Table-of-contents pages from the source (you will build a fresh one)
- Blank pages and "this page intentionally left blank"

### 5. Keep the structure

Preserve the things that help the eye:

- **Headings** mapped to a real hierarchy. Document title is the document title. Each article or section is Heading 1. Subsections within an article are Heading 2. Go to Heading 3 only if the source actually nests that deep. Never invent structure the source does not have, and never flatten it either.
- **Lists** stay lists. Numbered stays numbered, bulleted stays bulleted.
- **Tables** are rebuilt as real Word tables with the header row. If a table is too wide or complex to reproduce cleanly, turn each row into a short labelled paragraph instead and say so in the delivery note.
- **Links** are kept as working hyperlinks on the visible text.
- **Contact details, dates, times, addresses, prices, names** are kept exactly as written. These are usually the reason someone reads a newsletter.
- **Captions** are kept, attached to the image description they belong to.

### 6. Replace images with short descriptions

Every meaningful image becomes one italic paragraph in square brackets, one to two sentences, placed where the image sat in the reading order:

- Photo: what or who is in it, what is happening, plus the original caption if there was one. `[Photo: Three volunteers at an outdoor information booth, holding a banner. Caption: "The regional team at the spring fair."]`
- Chart or graph: what it measures and the takeaway, including the key numbers. `[Chart: Bar chart of monthly volunteer calls, January to June. Calls rose from 42 in January to 118 in June, the highest month on record.]`
- Poster, flyer or infographic with text on it: transcribe the text as content, because it usually is content. Then add a one-line description of the design.
- Logos, stock art, decorative photos with no caption and no information: drop silently.

Write descriptions as a plain observer. Do not guess names or identities of people who are not identified in the source.

### 7. Build the Word document

Read `/mnt/skills/public/docx/SKILL.md` and follow it. Structure the file like this:

```
[Document title from the source]
Source line: original filename, page count, and the date or issue if the source shows one
Contents: a plain list of the Heading 1 sections
--- page break ---
Heading 1: first section
  body text, lists, tables, image descriptions
Heading 1: next section
...
```

Formatting choices that matter for on-screen reading:

- Single column, letter size, 1 inch margins
- Body text 12 pt in a clean sans-serif (Calibri or Arial), 1.15 line spacing, space after each paragraph
- Headings clearly larger and bold, with space above them
- No text boxes, no floating elements, no columns, no colour backgrounds
- Table borders on, header row bold

Save the file to `/mnt/user-data/outputs/` named after the source, for example `Spring-Newsletter-readable.docx`.

### 8. Check it before delivering

Do all of these. Fix what you find, then check again.

**Coverage.** Walk the page map from step 2 and confirm every page or slide is represented somewhere in the output, or was deliberately stripped as furniture. Write a one-line reason for anything you dropped.

**Volume.** Compare the word count of the raw extracted text with the word count of the output body. The output should be close to the source minus what you stripped. A drop of more than roughly 15 percent that you cannot explain means something went missing. Find it.

**Continuity.** Read the output from top to bottom looking for:
- Sentences that stop mid-thought or start mid-sentence (a column merge went wrong)
- Paragraphs that change topic halfway through (a sidebar got stitched into an article)
- The same paragraph appearing twice (a pull quote or a "continued" portion was kept in both places)
- Headings with no body under them, or body text with no heading above it

**Appearance.** Render the .docx to images (the docx skill shows how) and look at the pages. Confirm headings look like headings, lists look like lists, and nothing overflows the page.

### 9. Deliver

Present the file with `present_files`. Keep the note short, in plain language, no bullet-point dump:

- One sentence on what it is (source name, page count in, section count out)
- What was stripped, in a phrase
- Anything you were unsure about and how you handled it, so the user can check that one spot instead of the whole document. For example: "The box on page 5 did not clearly belong to either article next to it; I placed it after the second article."

If a source was scanned and OCR quality was poor in places, say which sections to read with more care.

## Edge cases

- **Forms.** Keep the field labels as a list with a blank or the filled-in value beside each. Do not try to reproduce the boxes.
- **Slide decks.** One Heading 1 per slide using the slide title. Speaker notes go under a "Notes" Heading 2 on that slide's section. Drop slide numbers and footers.
- **Very long documents (more than about 40 pages).** Build the Word document in sections, checking each batch of pages before moving on, so an early mistake does not repeat through the whole file.
- **Multiple files uploaded.** Ask which to process, or whether to make one document per file. Do not merge them unless asked.
- **Reading order is unclear.** Make your best call, keep the content, and flag it in the delivery note. Never silently drop something because you could not place it.
- **The user asks for a different output format.** Their instruction wins over the Word default in this skill.
