import socket
import time

server_address = ('172.17.0.1', 54632)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:
    calculation = input("Enter calculation or exit: ")

    if calculation == "exit":
        break

    client_socket.send(calculation.encode())

    result = client_socket.recv(1024).decode()
    print(f"Sonuç: {result}")

client_socket.close()
