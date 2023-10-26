import socket
import threading
import re

def thread_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024).decode()

            if not data:
                break

            match = re.match(r'^([0-9]+)([+\-*/])([0-9]+)$', data)
            if match:
                num1, operator, num2 = match.groups()
                num1, num2 = int(num1), int(num2)
                if operator == '+':
                    result = num1 + num2
                    print(f"{num1} + {num2} = {result}")
                elif operator == '-':
                    result = num1 - num2
                    print(f"{num1} - {num2} = {result}")
                elif operator == '*':
                    result = num1 * num2
                    print(f"{num1} * {num2} = {result}")
                elif operator == '/':
                    if num2 != 0:
                        result = num1 / num2
                        print(f"{num1} / {num2} = {result}")
                    else:
                        client_socket.send("Zero division error".encode())
                        continue
                else:
                    client_socket.send("Invalid operator".encode())
                    continue
                
                client_socket.send(str(result).encode())
            else:
                client_socket.send("Invalid operation".encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 54632)
server_socket.bind(server_address)
server_socket.listen(5)
print("Server is listening...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"{client_address} connected.")

    client_handler = threading.Thread(target=thread_client, args=(client_socket,))
    client_handler.start()
    