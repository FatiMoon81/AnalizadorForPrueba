import tkinter as tk
from tkinter import ttk

import lexico
from lexico import lexer

import sintactico
from sintactico import parser

data = '''fOr(int i=1 ; i<=10 ; i++){
    res = i*5;
    res = i*5;
    res = i*5;
    cout << res << i << "Hola" & 1for ;
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

#Crear pantalla
ventana = tk.Tk()
ventana.title("Analizador Léxico y Sintáctico")
ventana.geometry("1280x900")

ventana.mainloop()