# Proyecto: Calculadora Básica
# Autor: André Cevallos

continuar = "s"

while continuar == "s":

    print("===== MENU CALCULADORA =====")
    print(0,1,2,3,4,5,6,7,8,9)
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")

    numero1 = float(input("Ingrese el primer número: "))

    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == "+" or operacion == "-" or operacion == "*" or operacion == "/":

        numero2 = float(input("Ingrese el segundo número: "))

        if operacion == "+":
            resultado = numero1 + numero2
            print("Resultado:", resultado)

        elif operacion == "-":
            resultado = numero1 - numero2
            print("Resultado:", resultado)

        elif operacion == "*":
            resultado = numero1 * numero2
            print("Resultado:", resultado)

        elif operacion == "/":

            if numero2 == 0:
                print("Error: No se puede dividir para cero.")

            else:
                resultado = numero1 / numero2
                print("Resultado:", resultado)

    else:
        print("Operación no válida.")

    continuar = input("¿Desea realizar otra operación? (s/n): ")

print("Gracias por usar la calculadora.")