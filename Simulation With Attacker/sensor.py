# sensor.py
import socket
import random
import time
from datetime import datetime

def send_temperature(packet_no, temperature, host='localhost', port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sensor_socket:
        sensor_socket.connect((host, port))
        print(f"{datetime.now()} - Sent Packet {packet_no} with temperature {temperature}°C")
        sensor_socket.sendall(f"{packet_no},{temperature}".encode())

packet_no = 1

while True:
    temperature = random.uniform(20.0, 100.0)
    send_temperature(packet_no, temperature)
    packet_no += 1
    time.sleep(1)
