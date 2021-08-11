class Parser:
    def __init__(self):
        pass

    def to_html(self, input):
        # TODO: handle songs that start with lyrics but no chords (e. g. "I love you. do you love me to?[Am7]")
        lines = input.splitlines()
        result = ''
        for line in lines:
            n = 2
            tokens = line.split('[')
            pairs = []
            for token in tokens:
                temp = token.split(']')
                pairs.append(tuple(temp))
            print(pairs[1:])
            html = ''
            html += '<ruby>'
            for pair in pairs[1:]:
                html += f'<ruby  style="margin-right: 4px;">{pair[1][:1]}<rt>{pair[0]}</rt>{pair[1][1:]}</ruby>'
            html += '<br>'
            result += (html)
        print(result)
        return result
# <ruby>FIRST CHARACTER<rt>CHORD</rt>REST OF TOKEN

if __name__ == "__main__":
    parser = Parser()
    parser.to_html('[G7]hello [C]world. [G7]hello [C]world.')