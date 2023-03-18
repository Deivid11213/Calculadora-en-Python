import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")

        # Creamos la caja de entrada
        self.entry = tk.Entry(self, width=20)
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Creamos los botones
        self.crear_botones()

    def crear_botones(self):
        # Lista de botones y sus posiciones
        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("/", 4, 3),
        ]

        # Creamos los botones
        for boton in botones:
            texto, fila, columna = boton
            comando = lambda texto=texto: self.click_boton(texto)
            tk.Button(self, text=texto, width=5, command=comando).grid(row=fila, column=columna, padx=5, pady=5)

    def click_boton(self, texto):
        if texto == "C":
            # Limpiamos la caja de entrada
            self.entry.delete(0, tk.END)
        elif texto == "=":
            # Obtenemos la expresión y la evaluamos
            expresion = self.entry.get()
            resultado = eval(expresion)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(resultado))
        else:
            # Agregamos el texto del botón a la caja de entrada
            self.entry.insert(tk.END, texto)

# Creamos la instancia de la calculadora y la iniciamos
calculadora = Calculadora()
calculadora.mainloop()
