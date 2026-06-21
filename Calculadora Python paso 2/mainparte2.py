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
    print("5. Potencia (^)")
    print("6. Raíz cuadrada (√)")
    
    # Solicitar y validar el primer numero  
    
    try:
        numero1 = float(input("Ingrese el primer número: "))
    except:
        print("Error: Debe ingresar un número válido.")
        continue

    # Solicitar operación
    operacion = input("Ingrese la operación (+, -, *, /, ^, √): ")

    # Validar operación
    if operacion not in ["+", "-", "*", "/", "^", "√"]:
        print("Error: Debe ingresar una operación válida.")
        continue

    # Operación de raíz cuadrada
    if operacion == "√":

        if numero1 < 0:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        else:
            resultado = numero1 ** 0.5
            print("Resultado:", resultado)

    else:

        # Validar segundo número
        try:
            numero2 = float(input("Ingrese el segundo número: "))
        except:
            print("Error: Debe ingresar un número válido.")
            continue

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

        elif operacion == "^":
            resultado = numero1 ** numero2
            print("Resultado:", resultado)

    continuar = input("¿Desea realizar otra operación? (s/n): ").lower()

print("Gracias por usar la calculadora.")