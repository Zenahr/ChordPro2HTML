# pythonping
PowerChord2HTML 

## Basic Usage
convert powerchord lyrics into HTML-based songsheets.

## Syntax for writing songsheets

Example: [C]Twinkle, twinkle [F]little [C]star.
Translates to:
C                F      C
Twinkle, twinkle little star.

```python
from powerchord2html import Parser as p

p.to_html("""[C]Twinkle, twinkle [F]little [C]star.
           [F]How I [C]wonder [G7]what you [C]are.
           [C]Up [F]above the [C]world so [G7]high,
           [C]Like a [F]diamond [C]in the [G7]sky.
           [C]Twinkle, twinkle [F]little [C]star.
           [F]How I [C]wonder [G7]what you [C]are.""")
>>> HTML

```

## Limitations

Currently only the chord notation is supported when importing PowerChord text. It is advisable to remove any other directives before processing with PowerChord2HTML.

## Planned

- export as HTML file
- export as PDF file