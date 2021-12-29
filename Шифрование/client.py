import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

print('Чтобы завершить передачу сообщений, введите exit')
while True:
    s = input('Введите числа a g p через пробел: ')
    if s == 'exit':
        break
    else:
        a, g, p = map(int, s.split())
    if p == 0:
        break
    A = (g ** a) % p
    data = str(g) + ' ' + str(p) + ' ' + str(A)
    sock.send(data.encode())
    data = sock.recv(1024).decode()
    K = (int(data) ** a) % p
    print('Закодированное число: ', K)
sock.close()
