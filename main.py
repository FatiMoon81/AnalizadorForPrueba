import lexico
from lexico import lexer

import sintactico
from sintactico import parser

data = '''fOr(i=1 ; i<=10 ; i++){
    res = i*5;
    res = i*6;
    res = i#8;
}'''

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

result = parser.parse(data)
print(result)