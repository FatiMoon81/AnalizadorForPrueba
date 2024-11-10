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

# ------------------------------------------------------------
# IMPLEMENTACION DE DISEÑO
# ------------------------------------------------------------

#Crear pantalla principal
ventana = tk.Tk()
ventana.title("Analizador Léxico y Sintáctico")
ventana.geometry("1280x900")
ventana.config(bg= "PINK");

#Botones
frame_botones = tk.Frame(ventana, bg='lightblue')
frame_botones.pack(pady=15)

boton_limpiar = tk.Button(frame_botones, text="Limpiar", width=15, height=5)
boton_limpiar.grid(row=0, column=0, padx=15)

boton_lexico = tk.Button(frame_botones, text="Análisis Léxico", width=15, height=5)
boton_lexico.grid(row=0, column=1, padx=15)

boton_sintactico = tk.Button(frame_botones, text="Análisis Sintáctico", width=15, height=5)
boton_sintactico.grid(row=0, column=2, padx=15)

boton_completo = tk.Button(frame_botones, text="Análisis Completo", width=15, height=5)
boton_completo.grid(row=0, column=3, padx=15)

ventana.mainloop()