"""
7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA
Menú: $12.000

Opciones bebida:

sí → $3.000
no → $0
Luego aplicar IVA del 8% al total final.
Mostrar valor con IVA incluido.
"""
print(" ***bienvenido al restaurante 'El Sabor Colombiano*** ")
print(" El menú del día tiene un valor de $12.000." )
print("¿desea agregar bebida por un valor de $3.000 ?")
bebida = input(" Responda sí o no: ").lower()

while True:
        bebida = input(" Responda sí o no: ").lower()
        if bebida == "si":
            print(" El valor total a pagar con IVA incluido es de $16.200")
            print(" gracias por su compra, vuelva pronto ")
        elif bebida == "no":
            print(" El valor total a pagar con IVA incluido es de $12.960")
            print(" gracias por su compra, vuelva pronto ")
        else:
            print(" respuesta no válida, intente de nuevo ")
            input(" Responda sí o no: ").lower()








