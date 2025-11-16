##La panadería de Don Pancho vende pan a $300 cada uno.


##Si compra más de 20 panes → 10% descuento
##Si compra más de 50 panes → 20% descuento
##Si ingresa una cantidad negativa, mostrar "Cantidad inválida"
##Calcular y mostrar el total.

bread = 300

quantity = int(input("Ingrese la cantidad de panes que desea llevar: "))

if quantity <= 0:
    print("Valor ingresado es incorrecto")
elif quantity <= 19:
    print(f"Su valor a pagar es de ${quantity*bread}")
elif quantity >= 20:
    print(f"Su total a pagar es de ${(quantity*bread)*0.90} ")
elif quantity >= 50:
    print(f"Su total a pagar es de ${(quantity*bread)*0.80} ")