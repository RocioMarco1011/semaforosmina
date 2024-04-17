import RPi.GPIO as GPIO
import time

# Configuramos los pines GPIO para los colores del semáforo 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ROJO_1_PIN = 18
VERDE_1_PIN = 23
GPIO.setup(ROJO_1_PIN, GPIO.OUT)
GPIO.setup(VERDE_1_PIN, GPIO.OUT)

# Configuramos los pines GPIO para los colores del semáforo 2
ROJO_2_PIN = 24
VERDE_2_PIN = 25
GPIO.setup(ROJO_2_PIN, GPIO.OUT)
GPIO.setup(VERDE_2_PIN, GPIO.OUT)

# Funciones para cambiar el color del semáforo 1
def cambiar_a_rojo_1():
    GPIO.output(VERDE_1_PIN, GPIO.LOW)
    GPIO.output(ROJO_1_PIN, GPIO.HIGH)

def cambiar_a_verde_1():
    GPIO.output(ROJO_1_PIN, GPIO.LOW)
    GPIO.output(VERDE_1_PIN, GPIO.HIGH)

# Funciones para cambiar el color del semáforo 2
def cambiar_a_rojo_2():
    GPIO.output(VERDE_2_PIN, GPIO.LOW)
    GPIO.output(ROJO_2_PIN, GPIO.HIGH)

def cambiar_a_verde_2():
    GPIO.output(ROJO_2_PIN, GPIO.LOW)
    GPIO.output(VERDE_2_PIN, GPIO.HIGH)

# Programa principal
while True:
    semaforo = input("Seleccione el semáforo (1 o 2): ")
    if semaforo == "1":
        while True:
            tiempo_rojo = int(input("Ingrese el tiempo en segundos en el que el semáforo 1 debe estar en rojo: "))
            if tiempo_rojo >= 1:
                break
            else:
                print("El tiempo debe ser mayor o igual a 1 segundo.")
        cambiar_a_rojo_1()
        cambiar_a_verde_2() # Cambiar semáforo 2 a verde
        time.sleep(tiempo_rojo)
        cambiar_a_verde_1()
        cambiar_a_rojo_2() # Cambiar semáforo 2 a rojo
    elif semaforo == "2":
        while True:
            tiempo_rojo = int(input("Ingrese el tiempo en segundos en el que el semáforo 2 debe estar en rojo: "))
            if tiempo_rojo >= 1:
                break
            else:
                print("El tiempo debe ser mayor o igual a 1 segundo.")
        cambiar_a_rojo_2()
        cambiar_a_verde_1() # Cambiar semáforo 1 a verde
        time.sleep(tiempo_rojo)
        cambiar_a_verde_2()
        cambiar_a_rojo_1() # Cambiar semáforo 1 a rojo