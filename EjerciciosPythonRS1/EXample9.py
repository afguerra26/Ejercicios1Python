""" 9. Supermercado “AhorroMax” — Descuentos y envío
Cada producto cuesta $2.000.

Reglas:

30 unidades → 15% descuento

10 unidades → 5% descuento

Si el total después del descuento es < $50.000 → agregar $5.000 de envío
Calcular total final"""

print(" ***bienvenido al supermercado 'AhorroMax'*** ")
print(" Todos los productos tienen un valor de $2.000." )
cantidad_productos = int(input("Ingrese la cantidad de productos que desea comprar: "))
precio_unitario = 2000
envio = 5000
descuento15 = 0.15
descuento5 = 0.05
total_sin_descuento = cantidad_productos * precio_unitario
if cantidad_productos >= 30:
    total_con_descuento = total_sin_descuento * (1 - descuento15)
    print(f"Se aplicó un descuento del 15%. Total con descuento: ${total_con_descuento}")
elif cantidad_productos >= 10:
    total_con_descuento = total_sin_descuento * (1 - descuento5)
    print(f"Se aplicó un descuento del 5%. Total con descuento: ${total_con_descuento}")
else:
    total_con_descuento = total_sin_descuento
    print(f"No se aplicó ningún descuento. Total: ${total_con_descuento}")
if total_con_descuento < 50000:
    total_final = total_con_descuento + envio
    print(f"Se agregó un costo de envío de ${envio}. Total final: ${total_final}")
else:
    total_final = total_con_descuento
    print(f"No se agregó costo de envío. Total final: ${total_final}")

        
