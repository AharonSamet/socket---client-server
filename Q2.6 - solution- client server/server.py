import datetime
import random
import socket

# name of the server
SERVER_NAME = "Hi, i'm a server, and my name is 'Server' "
# host and port by the server
IP = '0.0.0.0'
PORT = 1729
# Define how many clients can wait for connection
LISTEN = 1


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(LISTEN)

    # loop until user requested to exit
    while True:
        (client_socket, address) = server_socket.accept()
        data = client_socket.recv(4)

        if data.decode().lower() == 'name':
            client_socket.send(SERVER_NAME.encode())
        elif data.decode().lower() == 'rand':
            client_socket.send(str(random.randint(0, 9)).encode())
        elif data.decode().lower() == 'time':
            client_socket.send(str(datetime.datetime.now()).encode())
        elif data.decode().lower() == 'exit':
            client_socket.send('exit'.encode())
            client_socket.close()
            server_socket.close()
            break
        else:
            client_socket.send(("'" + data.decode() + "' is not recognized as an internal or external command\n try again").encode())
        client_socket.close()


if __name__ == '__main__':
    main()
