edad_pc = int(input("¿cuantos años tiene tu computador?: "))

if edad_pc > 0 and edad_pc < 2:
    print("Tu computador es nuevo")
elif edad_pc >= 2 and edad_pc <= 5:
    print("Tu computador tiene algunos años")
elif  edad_pc <= 0:
    print("Error: La edad del computador no puede ser negativa o cero")
else:
    print("Tu computador es viejo")
