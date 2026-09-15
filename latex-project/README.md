# Zhejiang University of Technology master's thesis LaTeX scaffold

This modular XeLaTeX project reconstructs the structure and principal layout
rules of the supplied 2019 Zhejiang University of Technology graduate-thesis
format specification. It is a replaceable manuscript scaffold rather than a
word-for-word transcription of the specification document.

## Build

Compile `main.tex` with XeLaTeX and BibTeX. On Overleaf, use XeLaTeX.

## Replace before thesis submission

1. Fill all metadata fields in `frontmatter/metadata.tex`.
2. Replace the placeholder abstracts and chapter text.
3. Replace the sample bibliography entry with verified sources.
4. Confirm any college-specific additions against the current official rules.

The global table column spacing is controlled by `\tabcolsep`; individual
tables are not reduced to a smaller font. The reconstructed page margins are
2.54 cm top/bottom and 3.17 cm left/right, matching the supplied specification.
