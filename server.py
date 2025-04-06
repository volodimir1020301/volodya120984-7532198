import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345 ))

server_socket.listen(1)
print('Сервер очікує підключення')

connection, address = server_socket.accept()
print(f'Підключення клієнта:  {address}')

data = connection.recv(1024).decode()
print(f'Отримано повідомлення від клієнта: {data}')
if data == 'help':
    connection.send('Привіт доступні команди , HELP,INFO'.encode())
elif data == 'info':
    connection.send('Привіт це сервер логіка'.encode())
elif data == 'напиши інформацію про роблокс':
    connection.send('Roblox — безплатна онлайн-платформа для створення ігор. Користувачі можуть створювати власні ігри в Roblox Studio, грати в ігри, створені іншими користувачами, а також створювати та вигадувати одяг для свого персонажа. Деякі товари в каталозі можна купити за ігрову валюту — Robux'.encode())
elif data == 'напиши інформацію про пабг':
    connection.send('PlayerUnknowns Battlegrounds — багатокористувацька відеогра, що розробляється корейською студією PUBG Corp. Доступна для Windows у сервісі Steam, iOS і Android, Xbox One і PlayStation 4'.encode())
else:
    connection.send('Невідома команда'.encode())



connection.close()
server_socket.close()