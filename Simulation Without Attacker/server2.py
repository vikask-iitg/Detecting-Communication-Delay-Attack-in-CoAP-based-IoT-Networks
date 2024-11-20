import socket
from datetime import datetime

THRESHOLD = 60.0

def evaluate_temperature(packet_no, temperature):
    status = "DANGER" if temperature > THRESHOLD else "SAFE"
    print(f"{datetime.now()} - Packet {packet_no}: {status} (Temperature: {temperature}°C)")

def start_server(host='localhost', port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"{datetime.now()} - Server is listening for connections...")
        
        while True:
            client_socket, addr = server_socket.accept()
            with client_socket:
                print(f"{datetime.now()} - Connected to {addr}")
                data = client_socket.recv(1024).decode()
                if data:
                    packet_no, temperature = data.split(',')
                    temperature = float(temperature)
                    print(f"{datetime.now()} - Packet {packet_no} received with temperature {temperature}°C")
                    evaluate_temperature(packet_no, temperature)

if __name__ == "__main__":
    start_server()

