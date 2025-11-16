"""8. Empresa “TecnoPlus” — Evaluación compuesta
El usuario ingresa dos notas (0.0 - 5.0):

Prueba técnica (70%)
Prueba lógica (30%)
Cálculo: nota_final = (tecnica * 0.7) + (logica * 0.3)

Condiciones:

nota_final ≥ 3 → “Aprobado”
2 ≤ nota_final < 3 → “Revisión”
< 2 → “Reprobado”
Validar que las notas estén en rango.
"""
nota_tecnica = float(input("Ingrese la nota de la prueba técnica (0.0 - 5.0): "))
nota_logica = float(input("Ingrese la nota de la prueba lógica (0.0 - 5.0): "))
if 0.0 <= nota_tecnica <= 5.0 and 0.0 <= nota_logica <= 5.0:
    nota_final = (nota_tecnica * 0.7) + (nota_logica * 0.3)
    
    if nota_final >= 3.0:
        print("Aprobado")
    elif 2.0 <= nota_final < 3.0:
        print("Revisión")
    else:
        print("Reprobado")
else:
    print("Error: Las notas deben estar en el rango de 0.0 a 5.0")
    