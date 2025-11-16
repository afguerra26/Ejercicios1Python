##3. Gimnasio “Solo Leveling Fit” — Motivación + Bono
##Pedir cuántos días entrenó esta semana.

## 4 días → "¡Excelente disciplina!" + gana 1 punto de energía
## 2 o 3 → "Bien, pero puedes dar más"
## 0 o 1 → "No aflojes, tú puedes mejorar"
## Mostrar mensaje y si aplica, los puntos ganados.

dias = (int(input("¿Cuantos dias entrenaste esta semana?: ")))


if dias <=0:
    print("No te rindas, tu puedes mejorar ")
elif dias >= 4:
    print('¡Excelente disciplina! gana 1 punto de energía')
elif dias <= 3:
    print("Bien, pero puedes dar más")
elif dias != 1:
    print("No aflojes, tú puedes mejorar")        
elif dias <=0:
    print("No te rindas, tu puedes mejorar ")


