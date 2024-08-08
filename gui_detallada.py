import tkinter as tk  # Importa la biblioteca tkinter para la creación de interfaces gráficas
from tkinter import ttk, messagebox  # Importa ttk para widgets temáticos y messagebox para cuadros de diálogo
from PIL import ImageTk, Image  # Importa PIL (Pillow) para manejar y mostrar imágenes
import csv  # Importa csv para manipular archivos CSV
import os  # Importa os para interactuar con el sistema operativo

# Función para calcular el índice de masa corporal (IMC)
def calcular_imc():
    try:
        # Obtiene los valores de las entradas de texto
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        edad = int(entry_edad.get())
        sexo = var_sexo.get()
        nombre = entry_nombre.get()

        # Verifica que el nombre esté ingresado
        if not nombre:
            messagebox.showerror("Error", "Por favor ingrese el nombre del paciente.")
            return

        # Calcula factores ks y ka según el sexo y la edad
        ks = 1.0 if sexo == "Hombre" else 1.1
        ka = 1 + 0.01 * (edad - 25)
        # Calcula el IMC ajustado
        imc = (peso / (altura ** 2)) * ks * ka

        # Muestra el resultado del IMC en la etiqueta correspondiente
        label_resultado.config(text=f"IMC: {imc:.2f}")

    except ValueError:
        # Muestra un mensaje de error si los valores ingresados no son válidos
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

# Función para guardar los datos del paciente en un archivo CSV
def guardar_datos():
    nombre = entry_nombre.get()
    # Verifica que el nombre esté ingresado
    if not nombre:
        messagebox.showerror("Error", "Por favor ingrese el nombre del paciente.")
        return

    # Crea un diccionario con los datos del paciente
    datos = {
        "Nombre": entry_nombre.get(),
        "Peso (kg)": entry_peso.get(),
        "Altura (m)": entry_altura.get(),
        "Edad": entry_edad.get(),
        "Sexo": var_sexo.get(),
        "IMC": label_resultado.cget("text").split(": ")[1]
    }

    archivo = f"{nombre}.csv"  # Nombre del archivo CSV
    archivo_existe = os.path.isfile(archivo)  # Verifica si el archivo ya existe

    # Abre el archivo en modo append y escribe los datos
    with open(archivo, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=datos.keys())
        if not archivo_existe:
            writer.writeheader()  # Escribe el encabezado si el archivo no existe
        writer.writerow(datos)  # Escribe los datos del paciente

    # Muestra un mensaje de confirmación
    messagebox.showinfo("Guardado", f"Datos guardados en el archivo {archivo}")

# Función para configurar el cursor como hand2 cuando el ratón entra en un botón
def configurar_cursor_hand2(event):
    event.widget.config(cursor="hand2")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de IMC")  # Título de la ventana

# Crear un canvas con la imagen de fondo
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# Cargar la imagen de fondo
imagen_fondo = ImageTk.PhotoImage(Image.open("imss.png"))
canvas.create_image(0, 0, anchor=tk.NW, image=imagen_fondo)

# Variable para el sexo biológico
var_sexo = tk.StringVar(value="Hombre")

# Estilo para los botones redondeados
estilo = ttk.Style()
estilo.configure('BotonRedondo.TButton', borderwidth=5, bordercolor="#EA899A", background="#00FF00",
                 foreground="black", padx=20, pady=20, relief=tk.RAISED,
                 font=("Arial", 14, "bold"))

# Widgets sobre el canvas
tk.Label(canvas, text="Nombre del paciente:", font=("Arial", 12)).place(x=50, y=50)
entry_nombre = tk.Entry(canvas, width=30, font=("Arial", 12))
entry_nombre.place(x=200, y=50)

tk.Label(canvas, text="Peso (kg):", font=("Arial", 12)).place(x=50, y=100)
entry_peso = tk.Entry(canvas, width=30, font=("Arial", 12))
entry_peso.place(x=200, y=100)

tk.Label(canvas, text="Altura (m):", font=("Arial", 12)).place(x=50, y=150)
entry_altura = tk.Entry(canvas, width=30, font=("Arial", 12))
entry_altura.place(x=200, y=150)

tk.Label(canvas, text="Edad:", font=("Arial", 12)).place(x=50, y=200)
entry_edad = tk.Entry(canvas, width=30, font=("Arial", 12))
entry_edad.place(x=200, y=200)

tk.Label(canvas, text="Sexo biológico:", font=("Arial", 12)).place(x=50, y=250)
tk.Radiobutton(canvas, text="Hombre", variable=var_sexo, value="Hombre", font=("Arial", 12)).place(x=200, y=250)
tk.Radiobutton(canvas, text="Mujer", variable=var_sexo, value="Mujer", font=("Arial", 12)).place(x=270, y=250)

# Cargar la imagen para el botón de calcular IMC
image_calcular_imc = Image.open("calcular_imc.png")
image_calcular_imc = image_calcular_imc.resize((110, 23), Image.LANCZOS)
image_calcular_imc = ImageTk.PhotoImage(image_calcular_imc)

# Crear el botón con la imagen y configurar el cursor hand2
btn_calcular_imc = ttk.Button(canvas, image=image_calcular_imc, style='BotonRedondo.TButton', command=calcular_imc)
btn_calcular_imc.place(x=50, y=300)
btn_calcular_imc.bind("<Enter>", configurar_cursor_hand2)  # Cambia el cursor a hand2 al pasar el ratón
btn_calcular_imc.bind("<Leave>", lambda e: btn_calcular_imc.config(cursor=""))

# Crear el botón "Guardar Datos" y configurar el cursor hand2
btn_guardar_datos = ttk.Button(canvas, text="Guardar Datos", style='BotonRedondo.TButton', command=guardar_datos)
btn_guardar_datos.place(x=250, y=300)
btn_guardar_datos.bind("<Enter>", configurar_cursor_hand2)  # Cambia el cursor a hand2 al pasar el ratón
btn_guardar_datos.bind("<Leave>", lambda e: btn_guardar_datos.config(cursor=""))

# Etiqueta para mostrar el resultado del IMC
label_resultado = tk.Label(canvas, text="IMC: ", font=("Arial", 12))
label_resultado.place(x=50, y=350)

# Ejecutar la aplicación
root.mainloop()


