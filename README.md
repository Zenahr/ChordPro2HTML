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

## Motivation

I'm planning on creating a public website where users can submit their own songsheets and add various translations. Why? Because no good website exists for songsheets for J-POP/K-POP songs that support smooth transition between hiragana, kanji, romaji and hangui. PowerChord2HTML is the base parser for needed for that.