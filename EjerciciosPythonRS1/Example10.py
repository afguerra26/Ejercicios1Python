"""10. Club “Noche Estelar” — Acceso + validación documento
Pedir edad y documento.

Reglas:

Edad ≥ 18 → puede entrar solo si tiene documento.
Si la edad < 18 → "Entrada denegada"
Si tiene 18 o más pero no tiene documento → "Debe presentar documento"""

print(" ***bienvenido al club 'Noche Estelar'*** ")
edad = int(input("Ingrese su edad: "))
if edad < 0:
    print("Error: La edad no puede ser negativa.")
elif edad <= 17:
    print("Entrada denegada. Debe ser mayor de edad para entrar al club.")
elif edad >= 18:
    tiene_documento = input("¿Tiene documento? Responda sí o no: ").lower()
    if tiene_documento == "si":
        print("Puede entrar al club. ¡Disfrute la noche!")
    elif tiene_documento == "no":
        print("Debe presentar documento para entrar.")
    else:
        print("Respuesta no válida. Por favor responda sí o no.")
else:
    print("Entrada denegada. Debe ser mayor de edad para entrar al club.")
