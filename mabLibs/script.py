import tkinter as tk
from tkinter import messagebox
import random

historias = ["Un día muy {}, decidí {} mientras {} un/a {}."]

# Función para crear una nueva historia
def crearHistoria():
    def guardarHistoria():
        historia = historia_text.get("1.0", tk.END).strip()
        if not historia:
            messagebox.showerror("Error", "La historia no puede estar vacía. 🤦‍♂️")
            return
        if "{}" not in historia:
            messagebox.showerror("Error", "La historia debe incluir '{}' para los espacios de preguntas. 😐")
            return
        historias.append(historia)
        messagebox.showinfo("Guardado", "¡Historia guardada exitosamente!😉")
        ventanaCrear.destroy()  

    ventanaCrear = tk.Toplevel()
    ventanaCrear.title("Crear Historia")
    ventanaCrear.configure(bg="#F0F0F0")
    ventanaCrear.minsize(500, 300)
    
    tk.Label(ventanaCrear, text="Escribe una historia🤫 con campos vacios usando '{}':", font=("Arial", 12), wraplength=450, bg="#F0F0F0").pack(pady=10)
    historia_text = tk.Text(ventanaCrear, width=50, height=10, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    historia_text.pack(pady=10)
    
    tk.Button(ventanaCrear, text="Guardar Historia", command=guardarHistoria, bg="#8BC34A", fg="#FFFFFF", font=("Arial", 12)).pack(pady=10)

# Función para jugar con una historia
def jugarHistoria():
    if not historias:
        messagebox.showerror("Error", "No hay historias guardadas. ¡Crea una primero!🤦‍♂️")
        return

    historia_actual = random.choice(historias)

    def generarHistoria():
        palabras = [entry.get() for entry in inputs]
        if not all(palabras):
            messagebox.showerror("Error", "Por favor, completa todos los campos.😐")
            return
        historia_completa = historia_actual.format(*palabras)
        messagebox.showinfo("Tu Historia 🤣", historia_completa)
        jugar_ventana.destroy()

    jugar_ventana = tk.Toplevel()
    jugar_ventana.title("Jugar Historia")
    jugar_ventana.configure(bg="#F0F0F0")
    jugar_ventana.minsize(500, 400)
    
    tk.Label(jugar_ventana, text="Completa los espacios para esta historia:", font=("Arial", 12), bg="#F0F0F0").pack(pady=10)
    tk.Label(jugar_ventana, text=historia_actual.replace("{}", "_____"), font=("Arial", 12), wraplength=450, bg="#F0F0F0").pack(pady=10)

    inputs = []
    for i in range(historia_actual.count("{}")):
        tk.Label(jugar_ventana, text=f"Palabra {i + 1}: ", font=("Arial", 10), bg="#F0F0F0").pack()
        entry = tk.Entry(jugar_ventana, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
        entry.pack(pady=5)
        inputs.append(entry)

    tk.Button(jugar_ventana, text="Generar Historia", command=generarHistoria, bg="#03A9F4", fg="#FFFFFF", font=("Arial", 12)).pack(pady=20)

ventana = tk.Tk()
ventana.title("MadLibs Interactivo")
ventana.configure(bg="#FAFAFA")
ventana.minsize(400, 300)

tk.Label(ventana, text="¡Bienvenido al juego de MadLibs! 🎉", font=("Arial", 14), pady=10, bg="#FAFAFA").pack()
tk.Button(ventana, text="¡Crear Historia!", command=crearHistoria, font=("Arial", 12), bg="#FFEB3B").pack(pady=10)
tk.Button(ventana, text="¡Jugar con las historias guardadas!", command=jugarHistoria, font=("Arial", 12), bg="#2196F3", fg="#FFFFFF").pack(pady=10)

ventana.mainloop()
