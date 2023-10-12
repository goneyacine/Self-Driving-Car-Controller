import socket
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),2183))

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break  # If the client disconnects, exit the loop
        message = data.decode('utf-8')
        client_socket.send(bytes('Hello','utf-8'))
        print(f"Received message from client: {message}")

s.listen(1)
while True:
     client_socket, client_address = s.accept()
     print(f"Accepted connection from {client_address}") 
     client_handler = threading.Thread(target=handle_client, args=(client_socket,))
     client_handler.start()