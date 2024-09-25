
import random

numero_secreto = random.randint(1, 30)# Generar un número secreto aleatorio entre 1 y 100

#Solicita la entrada del jugador
intentos = 0
adivinado = False

#Es el bucle principal del juego
while not adivinado:
    suposicion = input("Ingresa tu suposicion (entre 1 y 30): ")
    
    #Validación de entrada
    if not suposicion.isdigit():
        print("Por favor, ingresa un número dentro del rango xdd.")
        continue
    
    suposicion = int(suposicion)
    
    #Validación de rango
    if suposicion < 1 or suposicion > 30:
        print("El número debe estar en el rango de 1 a 30.")
        continue
    intentos += 1

    #Comparación y retroalimentación
    if suposicion < numero_secreto:
        print("Demasiado cerca, pero no ")
    elif suposicion > numero_secreto:
        print("Demasiado lejos! Estas cerca xdd")
    else:
        print(f"Waos lo lograste, lo hiciste en {intentos} intentos!")
        adivinado = True

    #Contador de intentos
    print(f"Intentos realizados: {intentos}")

#Finalización del juego

print(f"Waos lo lograste, lo hiciste en {intentos} intentos!")
adivinado = True

jugar_nuevamente = input("¿Jugamos de nuevo owo? (shi/ño): ")

if jugar_nuevamente.lower() == 'shi':
    numero_secreto = random.randint(1, 30)
    intentos = 0
    adivinado = False
    print("¡WAOS VAMOS A JUGAR DE NUEVO XD!")
else:
    print("Naco, al cabo que ni queria jugar >:v!")