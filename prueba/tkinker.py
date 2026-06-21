import tkinter as tk

# Función para calcular
def calcular():
    try:
        numero1 = float(entrada_numero1.get())
        operacion = entrada_operacion.get()

        if operacion == "√":
            if numero1 < 0:
                resultado_label.config(text="Error: raíz negativa")
            else:
                resultado = numero1 ** 0.5
                resultado_label.config(text="Resultado: " + str(resultado))

        else:
            numero2 = float(entrada_numero2.get())

            if operacion == "+":
                resultado = numero1 + numero2

            elif operacion == "-":
                resultado = numero1 - numero2

            elif operacion == "*":
                resultado = numero1 * numero2

            elif operacion == "/":
                if numero2 == 0:
                    resultado_label.config(text="Error: división por cero")
                    return
                resultado = numero1 / numero2

            elif operacion == "^":
                resultado = numero1 ** numero2

            else:
                resultado_label.config(text="Operación no válida")
                return

            resultado_label.config(text="Resultado: " + str(resultado))

    except:
        resultado_label.config(text="Error: ingrese números válidos")


# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora en Python")
ventana.geometry("350x300")

# Título
titulo = tk.Label(ventana, text="CALCULADORA BÁSICA", font=("Arial", 16))
titulo.pack(pady=10)

# Entrada primer número
tk.Label(ventana, text="Primer número:").pack()
entrada_numero1 = tk.Entry(ventana)
entrada_numero1.pack()

# Entrada operación
tk.Label(ventana, text="Operación (+, -, *, /, ^, √):").pack()
entrada_operacion = tk.Entry(ventana)
entrada_operacion.pack()

# Entrada segundo número
tk.Label(ventana, text="Segundo número:").pack()
entrada_numero2 = tk.Entry(ventana)
entrada_numero2.pack()

# Botón calcular
boton = tk.Button(ventana, text="Calcular", command=calcular)
boton.pack(pady=10)

# Resultado
resultado_label = tk.Label(ventana, text="Resultado:", font=("Arial", 12))
resultado_label.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()