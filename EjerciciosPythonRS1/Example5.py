#5. Librería “El Saber” — Descuento estudiante + cupón
#Libro cuesta $25.000.

#Si es estudiante → 15% descuento
#Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado
#Validar:

#Si no es estudiante, el cupón no aplica.
#Si ingresa cupón incorrecto, ignorarlo.
#Mostrar total.

print('bienvenido a la libreria el saber')

libro = 25000
Estudiante = input("¿Es usted estudiante? S/N: ").lower()
total = libro 
if Estudiante == "s":
    total = libro * 0.85
    cupon = input("Ingrese su cupón si tiene uno: ").upper()
    if cupon == "LIBRO10":
        total = total * 0.90
        print(f"Su valor a pagar con descuento de estudiante y cupón es de: {total}")
    else:
        print(f"Su valor a pagar con descuento de estudiante es de: {total}")
elif Estudiante == "n":
    print(f"Su valor a pagar es de: {libro}")
    cupon = input("Ingrese su cupón si tiene uno: ").upper()
    if cupon == "LIBRO10":
        total = libro * 0.90
        print(f"Su valor a pagar con descuento de estudiante y cupón es de: {total}")
    else:
        print(f"Su valor a pagar con descuento de estudiante es de: {total}")



