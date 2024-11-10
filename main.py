import tkinter as tk
from fileinput import lineno
from tkinter import ttk
from lexico import lexer
from sintactico import parser

"""
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
"""

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# IMPLEMENTACION DE DISEÑO
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

#Crear pantalla principal
ventana = tk.Tk()
ventana.title("Analizador Léxico y Sintáctico")
ventana.geometry("1280x900")
ventana.config(bg= "PINK")

#BOTONES
def limpiar():
    entrada.delete("1.0", tk.END)

    for item in tabla.get_children():
        tabla.delete(item)
    print("limpiar")

def analisis_lexico():
    print("LEXICO")
    # Limpiar los resultados previos en la tabla
    for item in tabla.get_children():
        tabla.delete(item)

    lexer.lineno = 1  # Asegurarse de que la primera línea se cuente correctamente

    contenido = entrada.get("1.0", "end-1c")
    lexer.input(contenido)

    # Tokenize y vaciar los resultados en la tabla
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input

        # Insertar una nueva fila con los datos de cada token en la tabla
        tabla.insert("", "end", values=(lineas,tok.value, tok.type,tok.lineno, tok.lexpos))

def analisis_sintactico():
    print("SINTACTICO")

    # Limpiar los resultados previos en la tabla sintáctica
    for item in tablaSintactico.get_children():
        tablaSintactico.delete(item)

    # Reiniciar el contador de líneas del lexer
    lexer.lineno = 1

    # Obtener el contenido del cuadro de texto
    contenido = entrada.get("1.0", "end-1c")

    # Si el contenido está vacío, no hacer nada
    if not contenido.strip():
        print("No hay contenido para analizar.")
        return

    # Realizar el análisis sintáctico
    try:
        result = parser.parse(contenido)
        print(f"Resultado del análisis: {result}")

        # Verificar si result es válido antes de insertar en la tabla
        if result:
            tablaSintactico.insert("", "end", values=(result,))
        else:
            tablaSintactico.insert("", "end", values=("Análisis fallido",))
    except Exception as e:
        print(f"Error durante el análisis sintáctico: {e}")
        tablaSintactico.insert("", "end", values=(f"Error: {e}",))

def analisis_completo():
    print("COMPLETO")
    analisis_lexico()
    analisis_sintactico()

frame_botones = tk.Frame(ventana, bg='lightblue')
frame_botones.pack(pady=15)

boton_limpiar = tk.Button(frame_botones, text="Limpiar", width=15, height=5, command=limpiar)
boton_limpiar.grid(row=0, column=0, padx=15)

boton_lexico = tk.Button(frame_botones, text="Análisis Léxico", width=15, height=5, command=analisis_lexico)
boton_lexico.grid(row=0, column=1, padx=15)

boton_sintactico = tk.Button(frame_botones, text="Análisis Sintáctico", width=15, height=5, command=analisis_sintactico)
boton_sintactico.grid(row=0, column=2, padx=15)

boton_completo = tk.Button(frame_botones, text="Análisis Completo", width=15, height=5, command=analisis_completo)
boton_completo.grid(row=0, column=3, padx=15)

#TEXTO
def actualizar_lineas(event=None):
    lineas.config(state="normal")
    lineas.delete("1.0", tk.END)

    line_count = int(entrada.index("end-1c").split(".")[0])
    lines_content = "\n".join(str(i) for i in range(1, line_count + 1))
    lineas.insert("1.0", lines_content)

    lineas.config(state="disabled")

    contenido = entrada.get("1.0", "end-1c")
    print(contenido)

# Sincronizar el desplazamiento de líneas con el desplazamiento de entrada
def sync_line_numbers(event):
    # Sincroniza la vista de `lineas` con `entrada`
    lineas.yview_moveto(entrada.yview()[0])
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
entrada = tk.Text(frame, wrap="word", width=200, height=20, bg="#c9c9c9", fg="black", insertbackground="PURPLE",
                  font=("Courier", 14), yscrollcommand=scrollbar.set)
entrada.tag_configure("palabraReservada", foreground="blue")
entrada.tag_configure("operador", foreground="red")
entrada.tag_configure("numero", foreground="purple")
entrada.tag_configure("identificador", foreground="black")
entrada.tag_configure("invalido", foreground="black", underline=True)
entrada.pack(side="left", fill="both", expand=True)

# Configurar scrollbar para entrada y sincronizar con líneas
scrollbar.config(command=entrada.yview)
entrada.bind("<<Scroll>>", sync_line_numbers)
entrada.bind("<KeyRelease>", lambda event: ( actualizar_lineas()))

# Asignar eventos
entrada.bind("<KeyRelease>", lambda event: (actualizar_lineas()))

# Llamada inicial para actualizar las líneas
actualizar_lineas()

# TABLA LEXICO
# Crear un frame contenedor para la tabla léxica
frame_tabla = tk.Frame(ventana, bg="BLACK")
frame_tabla.pack(pady=10, fill="x", expand=False)  # Usar 'pack' para la posición

# Definir las columnas de la tabla léxica
columnas_lexico = ("fila", "lexema", "token", "linea", "posicion")
tabla = ttk.Treeview(frame_tabla, columns=columnas_lexico, show="headings", height=10)

# Configurar encabezados para la tabla léxica
tabla.heading("fila", text="Fila")
tabla.heading("lexema", text="Lexema")
tabla.heading("token", text="Token")
tabla.heading("linea", text="Línea")
tabla.heading("posicion", text="Posición")

# Usar 'pack' para la tabla léxica
tabla.pack(pady=5, fill="x", expand=True)

# Ajustar el tamaño del frame para que ocupe un 80% del ancho de la ventana
ventana.update_idletasks()  # Asegurarse de que la ventana tenga un tamaño válido antes
frame_tabla.config(width=int(ventana.winfo_width() * 0.8))

# Centrar la tabla léxica respecto a la ventana
frame_tabla.place(relx=0.5, rely=0.60, anchor="center")

# TABLA SINTACTICO
# Crear un frame contenedor para la tabla sintáctica
frame_tablaSintactico = tk.Frame(ventana, bg="BLACK")
frame_tablaSintactico.pack(pady=5, fill="x", expand=True)

# Definir las columnas de la tabla sintáctica
columnas_sintactico = ("resultado",)
tablaSintactico = ttk.Treeview(frame_tablaSintactico, columns=columnas_sintactico, show="headings", height=4)

# Configurar encabezados para la tabla sintáctica
tablaSintactico.heading("resultado", text="Resultado")

# Usar 'pack' para la tabla sintáctica
tablaSintactico.pack(pady=5, fill="x", expand=True)

# Ajustar el tamaño del frame para que ocupe un 80% del ancho de la ventana
frame_tablaSintactico.config(width=int(ventana.winfo_width() * 0.8))

# Centrar la tabla sintáctica respecto a la ventana
frame_tablaSintactico.place(relx=0.5, rely=.82, anchor="center")

try:
    ventana.mainloop()
except KeyboardInterrupt:
    print("Interrupción recibida, cerrando la ventana.")