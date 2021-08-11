from flask import Flask
import sys
sys.path.append('../chordpro2html')
from chordpro2html import Parser
from songs import TWINKLE

p    = Parser()
song = TWINKLE

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return p.to_html(TWINKLE)

if __name__ == '__main__':
    app.run(debug=True)