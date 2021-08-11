import sys
sys.path.append('../chordpro2html')
from chordpro2html import Parser
from songs import TWINKLE

p = Parser()

html = p.to_html()

print(html)