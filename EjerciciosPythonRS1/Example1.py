##La panadería de Don Pancho vende pan a $300 cada uno.


##Si compra más de 20 panes → 10% descuento
##Si compra más de 50 panes → 20% descuento
##Si ingresa una cantidad negativa, mostrar "Cantidad inválida"
##Calcular y mostrar el total.

descuento = 0.0 
pan = 300
numero = int(input("ingrese cantidad: "))

if  numero >= 20 and numero <= 49 :
    descuento = (numero * pan) * 0.9
    print(f"Ha comprado {numero} panes con el 10% de descuento y su valor final es {descuento}")
elif numero >= 50 :
    descuento = (numero * pan) * 0.8
    print(f"Ha comprado {numero} panes con el 20% de descuento y su valor final es {descuento}")
elif numero <= 20 and numero > 0 :
    descuento = numero * pan
    print(f"Ha comprado {numero} panes sin descuento y su valor final es {descuento}")
else :
    print("Cantidad inválida, ingrese cantidad valida por favor.")