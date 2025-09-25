# Calculadora simple en Python

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

def calculadora():
    print("=== Calculadora en Python ===")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    while True:
        opcion = input("\nElige una opción (1-5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Por favor ingresa valores numéricos.")
                continue

            if opcion == "1":
                print(f"Resultado: {suma(num1, num2)}")
            elif opcion == "2":
                print(f"Resultado: {resta(num1, num2)}")
            elif opcion == "3":
                print(f"Resultado: {multiplicacion(num1, num2)}")
            elif opcion == "4":
                print(f"Resultado: {division(num1, num2)}")
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()
