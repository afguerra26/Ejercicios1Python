
Edad = (int(input( "Ingrese su edad: ")))

while Edad<=0:
    print("error")
    Edad = (int(input( "Ingrese su edad: ")))


if Edad <= 5:
    print("su entra es totalmente gratis")
elif Edad >= 6:
        print("su valor a pagar es de 5000")
elif Edad >= 12:
        print("su valor a pagar es de 8000")
elif Edad >= 60:
        print("su valor a pagar es de 4000 (descuento por adulto mayor)")    

