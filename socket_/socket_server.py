import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_socket(server_socket, client_address):
    """"""
    while True:
        receive_data = server_socket.recv(1024)
        print(receive_data.decode('utf8'))
        if receive_data.decode('utf8') == 'exit':
            print('exit')
            break
        return_data = input()
        server_socket.send(return_data.encode('utf8'))
    server_socket.close()


# get data from client
while True:
    sock, address = server.accept()

    # use thread to handle new connection to client
    client_thread = threading.Thread(target=handle_socket, args=(sock, address))
    client_thread.start()

    # data = sock.recv(1024)  # get 1k
    # print(data.decode('utf8'))
    # return_data = input()
    # sock.send(return_data.encode('utf8'))
    # server.close()
    # sock.close()
