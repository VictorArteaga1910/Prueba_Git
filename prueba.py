import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Moderna")
        self.root.geometry("400x500")
        self.root.configure(bg="#1e1e1e")

        # Variable para mostrar la operación y el resultado
        self.operacion = ""
        self.result_var = tk.StringVar()

        # Estilo moderno con ttk
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton",
                        font=("Arial", 18, "bold"),
                        padding=10,
                        relief="flat")
        style.map("TButton",
                  foreground=[("pressed", "white"), ("active", "white")],
                  background=[("pressed", "#444"), ("active", "#666")])

        # Pantalla de resultados
        pantalla = tk.Entry(root, textvariable=self.result_var, font=("Arial", 26, "bold"),
                            bd=0, bg="#2d2d2d", fg="white", justify="right")
        pantalla.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=15, padx=10, sticky="we")

        # Configurar filas y columnas para expandirse
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

        # Botones con colores personalizados
        botones = [
            ("7", 1, 0, "#3a3a3a"), ("8", 1, 1, "#3a3a3a"), ("9", 1, 2, "#3a3a3a"), ("/", 1, 3, "#f57c00"),
            ("4", 2, 0, "#3a3a3a"), ("5", 2, 1, "#3a3a3a"), ("6", 2, 2, "#3a3a3a"), ("*", 2, 3, "#f57c00"),
            ("1", 3, 0, "#3a3a3a"), ("2", 3, 1, "#3a3a3a"), ("3", 3, 2, "#3a3a3a"), ("-", 3, 3, "#f57c00"),
            ("0", 4, 0, "#3a3a3a"), (".", 4, 1, "#3a3a3a"), ("C", 4, 2, "#d32f2f"), ("+", 4, 3, "#f57c00"),
            ("=", 5, 0, "#388e3c"),
        ]

        for (texto, fila, columna, color) in botones:
            if texto == "=":
                boton = tk.Button(root, text=texto, bg=color, fg="white", font=("Arial", 20, "bold"),
                                  bd=0, relief="flat",
                                  command=self.calcular)
                boton.grid(row=fila, column=columna, columnspan=4, sticky="nsew", padx=5, pady=5)
            else:
                boton = tk.Button(root, text=texto, bg=color, fg="white", font=("Arial", 20, "bold"),
                                  bd=0, relief="flat",
                                  command=lambda t=texto: self.presionar(t))
                boton.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)

    def presionar(self, tecla):
        if tecla == "C":
            self.operacion = ""
            self.result_var.set("")
        else:
            self.operacion += str(tecla)
            self.result_var.set(self.operacion)

    def calcular(self):
        try:
            resultado = str(eval(self.operacion))
            self.result_var.set(resultado)
            self.operacion = resultado
        except:
            self.result_var.set("Error")
            self.operacion = ""

# Ejecutar la calculadora
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()

