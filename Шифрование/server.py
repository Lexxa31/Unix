import socket
import os
 
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
 
print('connected:', addr)
print('Чтобы завершить передачу сообщений, введите exit')
while True:
    data = []
    i = -1
    b = input('Введите число b: ')
    if b == 'exit':
        break
    else:
        b = int(b)
    data = list(map(int, (conn.recv(1024).decode()).split()))
    if len(data) < 3:
        break
    B = (int(data[0]) ** b) % int(data[1])
    conn.send(str(B).encode())
    K = (int(data[2]) ** b) % int(data[1])
    print('Закодированное число: ', K)
conn.close()
