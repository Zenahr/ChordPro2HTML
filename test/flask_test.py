from flask import Flask
import sys
sys.path.append('../chordpro2html')
from chordpro2html import Parser
from songs import TWINKLE, LEAVES, TENSHI

p    = Parser()
song = TWINKLE

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return p.to_html(LEAVES) + p.to_html(TWINKLE) + p.to_html(TENSHI)

if __name__ == '__main__':
    app.run(debug=True)