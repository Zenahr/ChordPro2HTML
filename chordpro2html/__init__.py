class Parser:
    def __init__(self):
        pass

    def to_html(self, input):
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
                html += f'<ruby>{pair[1]}<rt>{pair[0]}</rt><div style="margin-left: 4px;"></div></ruby>'
            html += '<br>'
            result += (html)
        print(result)
        return result


if __name__ == "__main__":
    parser = Parser()
    parser.to_html('[G7]hello [C]world. [G7]hello [C]world.')