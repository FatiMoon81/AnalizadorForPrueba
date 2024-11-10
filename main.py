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

#Ingreso de texto
# Frame para entrada de texto y conteo de líneas con scroll
frame = tk.Frame(ventana)
frame.place(relwidth=0.80, relheight=0.25, relx=0.5, rely=0.30, anchor="center")

# Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# Widget de conteo de líneas
lineas = tk.Text(frame, width=4, height=20, bg="#333333", fg="white", font=("Courier", 14), state="disabled")
lineas.pack(side="left", fill="y")

# Configuración de entrada de texto
entrada = tk.Text(frame, wrap="word", width=200, height=20, bg="#c9c9c9", fg="black", insertbackground="white",
                  font=("Courier", 14), yscrollcommand=scrollbar.set)
entrada.tag_configure("palabraReservada", foreground="blue")
entrada.tag_configure("operador", foreground="red")
entrada.tag_configure("numero", foreground="purple")
entrada.tag_configure("identificador", foreground="black")
entrada.tag_configure("invalido", foreground="black", underline=True)
entrada.pack(side="left", fill="both", expand=True)

# Configurar scrollbar para entrada y sincronizar con líneas
scrollbar.config(command=entrada.yview)

ventana.mainloop()