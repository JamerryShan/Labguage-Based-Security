import socket
import threading
import pickle
import password

class Token():
    def __init__(self, id, token):
        self.id = id
        self.token = token
    def __eq__(self, other):
        return type(other) is Token and self.id == other.id and self.token == other.token

def check_data(data):
    if b'R' in data:
        return True
    return False

def tcp_link(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    while True:
        data = sock.recv(1024)
        if(check_data(data)):
            sock.sendall(pickle.dumps("Do not use reduce function!",protocol=3))
            print("reduce function detected!")
        else:
            data_de = pickle.loads(data)
            if(data_de == Token(password.id, password.token)):
                sock.sendall(pickle.dumps("OK!",protocol=3))
                print('login succeed!')
            else:
                sock.sendall(pickle.dumps("Wrong!",protocol=3))
                print('login failed!')
            print("current id is: " + password.id)
            print("current token is: " + password.token)
            print()

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8080))
    s.listen(5)
    print('Waiting for connection...')
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcp_link, args=(sock, addr))
        t.start()

if __name__ == '__main__':
    start_server()
    pass
