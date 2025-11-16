##4. Heladería “Frosty” — Sabor y topping
##Sabores y precios:

##chocolate → $4.000
##vainilla → $3.500
##Opcional: topping cuesta $1.000.

##Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
##Si el sabor es válido, preguntar si quiere topping y calcular total.

chocolate = 4000
vainilla = 3500
topping = 1000
canTopping=0


print('')
print ("Bienvenido a heladeria frosty ¿que sabor desea llevar? Chocolate o Vainilla: ")
helado = input('Chocolate o vainilla: ').lower()

if  helado == "chocolate":
    tp =  input("¿Desea agregar topping? S/N: ").lower()
    if tp == "s":
        canTopping=int(input("cuantos toppings desea agregar: "))
        print(f"el valor a pagar es de {chocolate+(canTopping*topping)}")
    else:
        print ("su valor a pagar es de 4000")


elif helado == "vainilla":
    tp =  input("¿Desea agregar topping? S/N: ").lower()
    if tp == "s":
        canTopping=int(input("cuantos toppings desea agregar: "))
        print(f"el valor a pagar es de {vainilla+(canTopping*topping)}")
    else:
        print ("su valor a pagar es de 3500")
else:
    print(f"el sabor {helado}  no esta disponible en el inventario")







