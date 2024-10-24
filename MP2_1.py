#Bibliotecas necesarias
import logging
#import datetime
import time
import board
import adafruit_dht
import subprocess
logging.basicConfig(filename='/home/raspi/Desktop/mp2/log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
script_path = '/home/raspi/Desktop/mp2/correct_sensor.sh'
result = subprocess.run([script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text = True)
from gpiozero import DistanceSensor
#sensor de humedad y temperatura
dhtDevice = adafruit_dht.DHT11(board.D4)
#sensor de proximidad
sensor = DistanceSensor(echo= 23, trigger=18, max_distance=3)
while True:
    try:
        # Measures the distance and outputs it
        distance = sensor.distance * 100  # Conversion from meters to centimeters
        if distance < 2 or distance > 300:
            print("ERROR, NO SE PUEDE MEDIR DISTANCIA: SENSOR FUERA DE RANGO")
            print("------------------------------")
        else:
            # The spacing is formatted to two decimal places
            print(f"Distancia Medida: {distance:.2f} cm")
            
#Leer valores y realizar acciones
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temperatura Registrada: {:.1f}C Humedad Registrada:{}%".format(temperature_c, humidity))
        logging.info("Temperatura Registrada: {:.1f}C Humedad Registrada:{}%".format(temperature_c, humidity))
        logging.info(f"Distancia Medida: {distance:.2f} cm")
    except OSError as error:
        print(error.args[0])
    except RuntimeError as error:
        # Errores durante la lectura del sensor
        print(error.args[0])
        time.sleep(2)
    except Exception as error:
        # Otras excepciones
        raise error
    time.sleep(2.0)
    logging.debug("mensaje de depuración")
if dhtDevice:
    dhtDevice.exit()
    
    