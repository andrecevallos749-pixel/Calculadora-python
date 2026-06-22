print("CALCULADORA BÁSICA")
print("por Andre Cevallos")

# Ingresar primer número
numero1 = float(input("Ingrese el primer número: "))

# Elegir operación
operacion = input("Seleccione una operación (+ o -): ")

# Ingresar segundo número
numero2 = float(input("Ingrese el segundo número: "))

# Realizar operación seleccionada
if operacion == "+":
    resultado = numero1 + numero2

elif operacion == "-":
    resultado = numero1 - numero2

# Mostrar resultado
print("Resultado:", resultado)

# Fin del programa
print("Fin")