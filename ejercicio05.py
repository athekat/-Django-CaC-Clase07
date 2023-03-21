def get_int():  # iterativa
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            print("Numero entero ingresado con éxito.")
            return numero
        except ValueError:
            print("No ha ingresado un número entero.")


def get_int_r():  # recursiva
    try:
        numero = int(input("Ingrese un número entero: "))
        print("Numero entero ingresado con éxito.")
        return numero
    except ValueError:
        print("No ha ingresado un número entero.")
        return get_int_r()


# print(get_int_())
print(get_int_r())
