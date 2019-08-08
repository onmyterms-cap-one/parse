from tika import parser

def parsePDF(path="C://Users//HHS//Desktop//AlaskaAirlines.pdf"):
    file_data = parser.from_file(path)
    text = file_data['content']
    return text

def execute(category, text):
    if(category == 'Airlines'):
        airline_parse()
    if(category == 'Credit Card'):
        creditcard_parse()


if __name__ == '__main__':
    text = parsePDF()
    execute("Airlines", text)