import socket

server_address = ('172.19.0.2', 54632)

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
