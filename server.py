import socket
import threading

HEADER = 64
PORT = 5050
#SERVER = "10.19.15.125" #i want to run on my local network
SERVER = socket.gethostbyname(socket.gethostname())
#print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_lenth = conn.recv(HEADER).decode(FORMAT)
        msg_lenth = int(msg_lenth)
        msg = conn.recv(msg_lenth).decode(FORMAT)
        print(f"[{addr}] {msg}")

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()