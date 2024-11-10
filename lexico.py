# ------------------------------------------------------------
# Analizador lexico de estructura FOR
# ------------------------------------------------------------
import ply.lex as lex

reservadas = {
   'for': 'palabraReservadaFOR',
   'int': 'palabraReservadaINT',
   'cout' : 'palabraReservadaCOUT'
}

# Lista de tokens
tokens = [
    'ID', 'NUM',
    'LEFTSHIFT',
    'MAYORIGUAL', 'MENORIGUAL', 'EQUIVALENTE', 'DIFERENTE', 'MAYOR', 'MENOR',
    'INCREMENT', 'DECREMENT',
    'MAS', 'MENOS', 'MULTI', 'DIVI', 'IGUAL',
    'SEMICOLON', 'COMILLAS', 'PARENIZQ', 'PARENDER', 'LLAVEIZQ', 'LLAVEDER',
    'INVALIDO', 'CADENA'  # Token para palabras no permitidas
] + list(reservadas.values())

# Expresiones regulares para tokens simples
t_LEFTSHIFT = r'<<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_EQUIVALENTE = r'=='
t_DIFERENTE = r'!='
t_MAYOR = r'>'
t_MENOR = r'<'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTI = r'\*'
t_DIVI = r'/'
t_IGUAL = r'='
t_SEMICOLON = r';'
t_COMILLAS = r'"'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Eliminar las comillas del principio y el final
    return t

def t_palabraReservada(t):
    r'[a-zA-Z_]\w*'
    t_lower = t.value.lower()
    t.type = reservadas.get(t_lower, 'ID')
    return t

# Nueva regla para capturar palabras reservadas no válidas (como 1for, 6int)
def t_invalid_reserved(t):
    r'\d+[a-zA-Z_]\w*'
    t.type = 'INVALIDO'
    print(f"Palabra reservada no válida: '{t.value}'")
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_saltoLinea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

# Regla para manejar errores generales
def t_error(t):
    print("Error lexico: Caracter inválido '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()