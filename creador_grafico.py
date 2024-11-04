import paramiko
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Variables Conexión SSH
host = "192.168.3.228"
username = "raspi"
password = "tic1"

#SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname = host, port = 22, username = username, password = password)
    sftp = client.open_sftp()

    #Archivos
    hospe = "/home/raspi/Desktop/mp2/log.csv"
    clent2 = "C:\\Raspi\\log.csv"

    def descargar_log():
        sftp.get(hospe, clent2)
        print("Archivo recibido exitosamente")

    def mostrar_grafico():
        descargar_log()
        data = pd.read_csv(clent2, on_bad_lines = "skip", delimiter = ",")
        if "timestamp" in data.columns and "temperature_c" in data.columns and "humidity" in data.columns:
            plt.figure(figsize=(10, 5))
            plt.subplot(2, 1, 1)
            plt.plot(data["timestamp"], data["temperature_c"], label = "Temperatura (°C)", color = "red")
            plt.plot(data["timestamp"], data["humidity"], label = "Humedad (%)", color = "blue")
            plt.title("Temperatura y Humedad")
            plt.xlabel("Tiempo")
            plt.ylabel("Valor")
            plt.legend()
        else:
            print("Faltan columnas necesarias para el gráfico de Temperatura y Humedad.")
        if "timestamp" in data.columns and "distance_cm" in data.columns:
            plt.subplot(2, 1, 2)
            plt.plot(data["timestamp"], data["distance_cm"], label = "Distancia (cm)", color = "green")
            plt.title("Distancia Medida")
            plt.xlabel("Tiempo")
            plt.ylabel("Distancia (cm)")
            plt.legend()
        else:
            print("Faltan columnas necesarias para el gráfico de Distancia.")
        plt.tight_layout()
        plt.show()

    def mostrar_tabla():
        descargar_log()
        data = pd.read_csv(clent2, on_bad_lines = "skip", delimiter = ",")
        if "distance_cm" in data.columns and "temperature_c" in data.columns and "humidity" in data.columns:
            datos_tabla = {
                "Variables": ["Distancia", "Temperatura", "Humedad"],
                "Maximo": [np.max(data["distance_cm"]), np.max(data["temperature_c"]), np.max(data["humidity"])],
                "Minimo": [np.min(data["distance_cm"]), np.min(data["temperature_c"]), np.min(data["humidity"])],
                "Promedio": [np.mean(data["distance_cm"]), np.mean(data["temperature_c"]), np.mean(data["humidity"])]
            }
            tabla = pd.DataFrame(datos_tabla)
            print(tabla)
        else:
            print("Faltan columnas necesarias para calcular la tabla de datos.")

    #Main
    print("Ingrese un Comando (grafico, tabla o salir): ")
    while True:
        opcion = input().lower()
        if opcion == "grafico":
            mostrar_grafico()
        elif opcion == "tabla":
            mostrar_tabla()
        elif opcion == "salir":
            print("Cerrando conexión...")
            sftp.close()
            client.close()
            print("Programa terminado")
            break
        else:
            print("Comando no reconocido, intente nuevamente")
        time.sleep(2.0)

except Exception as e:
    print(f"Se produjo un error: {e}")
finally:
    if 'sftp' in locals():
        sftp.close()
    if 'client' in locals():
        client.close()