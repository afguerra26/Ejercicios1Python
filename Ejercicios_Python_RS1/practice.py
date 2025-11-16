temp = int(input("ingrese temperatura: "))
unidad = input("ingrese K O F: " )

def converC(temp, unidad):
    if unidad == "f" or unidad == "F":
        # convertir de Celsius a Fahrenheit
        c = temp * 1.8 + 32
        return c

    elif unidad == "k" or unidad == "K":
        # convertir de Celsius a Kelvin
        c = temp + 273.15
        return c
    else:
        print("debes ingresar datos validos, intenta de nuevo")
        return None

c = converC(temp, unidad)
if c is not None:
    print("la temperatura de {} grados ".format(temp), "es equivalente a {}".format(c))