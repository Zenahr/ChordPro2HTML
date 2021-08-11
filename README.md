# pythonping
ChordPro2HTML 

## Basic Usage
convert chordpro lyrics into HTML-based songsheets.

## Syntax for writing songsheets

Example: [C]Twinkle, twinkle [F]little [C]star.
Translates to:
C                F      C
Twinkle, twinkle little star.

```python
from chordpro2html import Parser as p

p.to_html("""[C]Twinkle, twinkle [F]little [C]star.
           [F]How I [C]wonder [G7]what you [C]are.
           [C]Up [F]above the [C]world so [G7]high,
           [C]Like a [F]diamond [C]in the [G7]sky.
           [C]Twinkle, twinkle [F]little [C]star.
           [F]How I [C]wonder [G7]what you [C]are.""")
>>> HTML

```

## Limitations

Currently only the chord notation is supported when importing ChordPro text. It is advisable to remove any other directives before processing with ChordPro2HTML.

## Planned

- export as HTML file
- export as PDF file