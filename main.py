from tika import parser
import creditcard

def parsePDF(path):
    file_data = parser.from_file(path)
    text = file_data['content']
    return text

def execute(category, text):
    # if(category == 'Airlines'):
    #     airline_parse()
    if(category == 'Credit Card'):
        creditcard.credit_parse(text)


if __name__ == '__main__':
    text = parsePDF("wellsfargo.pdf")
    execute("Credit Card", text)