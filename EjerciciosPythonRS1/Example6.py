tiempo =float(input("ingrseel numero de horas de servicio: "))
hora = 2000
multa = 5000
if tiempo <= 4.9 :
    total = tiempo * hora
    print(f"el valor a pagar es de: {total}")
elif tiempo >=5 :
    total = (tiempo * hora) + multa
    print(f"el valor a pagar es de: {total}")    