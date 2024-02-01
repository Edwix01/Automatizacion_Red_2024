#Script Para ejecutar Funciones de Prueba

import numpy as np

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import ARP, Ether, srp

def scan(ip):
    # Crear una solicitud ARP dirigida a la dirección IP proporcionada
    arp_request = ARP(pdst=ip)
    
    # Crear un paquete Ethernet para enviar la solicitud ARP
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Combinar el paquete Ethernet y la solicitud ARP
    packet = ether/arp_request
    
    # Enviar el paquete y recibir respuestas
    result = srp(packet, timeout=6, verbose=0)[0]
    
    # Analizar las respuestas
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

def main():
    # Especificar el rango de direcciones IP que deseas escanear
    target_ip = "192.168.20.1/24"
    
    # Realizar el escaneo
    devices = scan(target_ip)
    
    # Mostrar los dispositivos encontrados
    print("Dispositivos activos en la red:")
    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")

if __name__ == "__main__":
    main()
