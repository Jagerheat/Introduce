import socket
import datetime

START = datetime.datetime.now()
MESS = 0


def uptime():
    return str(datetime.datetime.now() - START)


def num_mess():
    return str(MESS)


def logg(addr, comman):
    with open("text.txt", 'a') as f:
        f.write(f"{datetime.datetime.now()} \t {addr[0]}:{addr[1]} \t {comman} \n")


if __name__ == '__main__':

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 4545)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)
    tt_time = datetime.datetime.now()

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        MESS += 1
        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024)
                print('received {!r}'.format(data))
                if data:
                    text = data.decode()
                    logg(addr=client_address, comman=text)
                    if text == "stat":
                        message = uptime()
                    elif text == "fet":
                        message = num_mess()
                    elif text == "Q":
                        quit()


                    else:
                        message = "Услышал тебя"
                    connection.send(message.encode())


                else:
                    print('sta', client_address)
                    break

        finally:
            # Clean up the connection
            connection.close()

