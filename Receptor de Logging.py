import paramiko
import time
#Variables de Conexión SSH
host="192.168.0.192"
username="raspi"
password="raspi"

#Conexión por SSH
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, port=22, username=username, password=password)
sftp=client.open_sftp()

#Brazo transmisor/receptor de Archivos
hospe="/home/raspi/Desktop/mp2/log.txt"
clent2="C:/pisender/log.txt"
control=1
print("Archivo RECIBIDO exitosamente")
print("Ingrese un Comando: 'grafico', 'tabla', 'alerta', 'salir'")

opcion = str(input())
while control:
    sftp.get(hospe,clent2)
    time.sleep(2.0)
    if opcion=="salir":
        sftp.close()
        client.close()
        control=control-1
        print(control)
        print("programa terminado")