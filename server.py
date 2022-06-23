import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 1379
server.bind((ip, port))
server.listen(1)


while True:
    print("Search///")
    user, adres = server.accept()

    while True:
        data = user.recv(512).decode()
        if data == "connected":
            print(f"Connected from {adres[0]}")
        elif data == "disconnected":
            print(f"Disconnected from {adres[0]}")
            user.close()
            break
            break
        elif data == None or data == "":
            pass
        else:
            print(data)

server.close()