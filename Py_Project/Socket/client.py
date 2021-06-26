import server2
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4545  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    val = input("What we do")
    while val != "x":
        s.sendall(val.encode())
        data = s.recv(1024)
        print(data.decode())
        val = input("What we do")
