import ply.yacc as yacc
from lexico import tokens

#Prueba de push

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTI', 'DIVI'),
)

def p_expression_binop(p):
    '''expression : expression MAS expression
                  | expression MENOS expression
                  | expression MULTI expression
                  | expression DIVI expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_number(p):
    'expression : NUM'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_expression_parentheses(p):
    'expression : PARENIZQ expression PARENDER'
    p[0] = p[2]

def p_logical_statement(p):
    '''logical_statement : expression MAYORIGUAL expression
                         | expression MENORIGUAL expression
                         | expression EQUIVALENTE expression
                         | expression DIFERENTE expression
                         | expression MAYOR expression
                         | expression MENOR expression'''

def p_increment_operator(p):
    '''increment_operator : ID INCREMENT
                          | ID DECREMENT'''

def p_assigment(p):
    'assigment : ID IGUAL expression SEMICOLON'
    p[1] = p[3]

def p_declaration_int(p):
    'declaration_int : palabraReservadaINT ID IGUAL expression SEMICOLON'

def p_statement(p):
    '''statement : assigment'''

def p_statement_list_1(t):
    'statement_list : statement'

def p_statement_list_2(t):
    'statement_list : statement_list statement'

def p_for_statement_1(p):
    'expression : palabraReservadaFOR PARENIZQ assigment logical_statement SEMICOLON increment_operator PARENDER LLAVEIZQ statement_list LLAVEDER'

def p_for_statement_2(p):
    'expression : palabraReservadaFOR PARENIZQ declaration_int logical_statement SEMICOLON increment_operator PARENDER LLAVEIZQ statement_list LLAVEDER'

def p_error(p):
    print("Error de sintaxis en la entrada:", p)

parser = yacc.yacc()