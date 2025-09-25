import tkinter as tk

# Clase de la Calculadora
class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora en Python")
        self.root.geometry("400x500")
        self.root.configure(bg="#222")

        # Variable para mostrar la operación y el resultado
        self.operacion = ""
        self.result_var = tk.StringVar()

        # Pantalla de resultados
        pantalla = tk.Entry(root, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2,
                            width=15, borderwidth=4, bg="#eee", justify="right")
        pantalla.grid(row=0, column=0, columnspan=4, pady=20)

        # Botones
        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0)
        ]

        for (texto, fila, columna) in botones:
            if texto == "=":
                boton = tk.Button(root, text=texto, padx=80, pady=20, font=("Arial", 18), bg="#4CAF50", fg="white",
                                  command=self.calcular)
                boton.grid(row=fila, column=columna, columnspan=4, pady=10)
            else:
                boton = tk.Button(root, text=texto, padx=20, pady=20, font=("Arial", 18), bg="#333", fg="white",
                                  command=lambda t=texto: self.presionar(t))
                boton.grid(row=fila, column=columna, pady=5)

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
