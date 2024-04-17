import RPi.GPIO as GPIO
import time

# Configuramos los pines GPIO para los colores del semáforo
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ROJO_PIN = 18
VERDE_PIN = 23
GPIO.setup(ROJO_PIN, GPIO.OUT)
GPIO.setup(VERDE_PIN, GPIO.OUT)

# Funciones para cambiar el color del semáforo
def cambiar_a_rojo():
    GPIO.output(VERDE_PIN, GPIO.LOW)
    GPIO.output(ROJO_PIN, GPIO.HIGH)

def cambiar_a_verde():
    GPIO.output(ROJO_PIN, GPIO.LOW)
    GPIO.output(VERDE_PIN, GPIO.HIGH)

# Programa principal
while True:
    print("Seleccione el color del semáforo:")
    print("1. Rojo")
    print("2. Verde")
    opcion = input("Ingrese el número de la opción que desea: ")
    if opcion == "1":
        cambiar_a_rojo()
    elif opcion == "2":
        cambiar_a_verde()
    else:
        print("Opción no válida")

    time.sleep(1) # Esperamos 1 segundo antes de volver a preguntar