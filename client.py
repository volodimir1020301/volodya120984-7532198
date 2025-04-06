import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 12345 ))
msg = input('Введіть повідомленя')
client_socket.send(msg.encode() )

response = client_socket.recv(1024).decode()
print(f'Відповідь від сервера:  {response}')

client_socket.close()

