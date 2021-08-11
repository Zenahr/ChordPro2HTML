import sys
sys.path.append('../chordpro2html')
from chordpro2html import Parser

p = Parser()

html = p.to_html("""
[C]Twinkle, twinkle [F]little [C]star.
[F]How I [C]wonder [G7]what you [C]are.
[C]Up [F]above the [C]world so [G7]high,
[C]Like a [F]diamond [C]in the [G7]sky.
[C]Twinkle, twinkle [F]little [C]star.
[F]How I [C]wonder [G7]what you [C]are.""")

print(html)