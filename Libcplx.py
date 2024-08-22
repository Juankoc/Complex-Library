import math


def cplx_sum(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cplx_sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def cplx_product(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    imag = (a[0] * b[1]) + (b[0] * a[1])
    return (real, imag)


def cplx_modulo(num):
    return math.sqrt(num[0] ** 2 + num[1] ** 2)


def cplx_div(a, b):
    b_mod_squared = cplx_modulo(b) ** 2
    if b_mod_squared == 0:
        raise ValueError("Division by zero is undefined.")

    real = ((a[0] * b[0]) + (a[1] * b[1])) / b_mod_squared
    imag = ((b[0] * a[1]) - (a[0] * b[1])) / b_mod_squared
    return (real, imag)


def cplx_conjugate(num):
    return (num[0], -num[1])


def cplx_phase(num):
    return math.atan2(num[1], num[0])


def cplx_convert(num, option):
    if option == 1:
        modulo = cplx_modulo(num)
        phase = cplx_phase(num)
        return (modulo, phase)
    elif option == 2:
        real = num[0] * math.cos(num[1])
        imag = num[0] * math.sin(num[1])
        return (real, imag)
    else:
        raise ValueError("Invalid option")


def main():
    while True:
        print("\nMenú de Operaciones con Números Complejos")
        print("1. Sumar dos números complejos")
        print("2. Restar dos números complejos")
        print("3. Multiplicar dos números complejos")
        print("4. Dividir dos números complejos")
        print("5. Calcular el módulo de un número complejo")
        print("6. Obtener el conjugado de un número complejo")
        print("7. Calcular la fase de un número complejo")
        print("8. Convertir de Cartesiano a Polar")
        print("9. Convertir de Polar a Cartesiano")
        print("10. Salir")

        try:
            option = int(input("Seleccione una opción: "))
        except ValueError:
            print("Opción no válida. Intente de nuevo.")
            continue

        if option == 10:
            print("Saliendo del programa.")
            break

        if option in range(1, 5):
            try:
                real1 = float(input("Ingrese la parte real del primer número: "))
                imag1 = float(input("Ingrese la parte imaginaria del primer número: "))
                real2 = float(input("Ingrese la parte real del segundo número: "))
                imag2 = float(input("Ingrese la parte imaginaria del segundo número: "))
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números.")
                continue

            num1 = (real1, imag1)
            num2 = (real2, imag2)

            if option == 1:
                result = cplx_sum(num1, num2)
            elif option == 2:
                result = cplx_sub(num1, num2)
            elif option == 3:
                result = cplx_product(num1, num2)
            elif option == 4:
                try:
                    result = cplx_div(num1, num2)
                except ValueError as e:
                    print(e)
                    continue

            print(f"Resultado: {result}")

        elif option in [5, 6, 7, 8, 9]:
            try:
                if option in [5, 6, 7, 8]:
                    real = float(input("Ingrese la parte real: "))
                    imag = float(input("Ingrese la parte imaginaria: "))
                    num = (real, imag)
                else:
                    modulo = float(input("Ingrese el módulo: "))
                    fase = float(input("Ingrese la fase (en radianes): "))
                    num = (modulo, fase)

            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números.")
                continue

            if option == 5:
                result = cplx_modulo(num)
            elif option == 6:
                result = cplx_conjugate(num)
            elif option == 7:
                result = cplx_phase(num)
            elif option == 8:
                result = cplx_convert(num, 1)
            elif option == 9:
                result = cplx_convert(num, 2)

            print(f"Resultado: {result}")

        else:
            print("Opción no válida. Intente de nuevo.")


main()
