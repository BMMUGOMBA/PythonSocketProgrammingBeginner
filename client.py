import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.5.59.91" #i want to run on my local network
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Hello World!")
send("Hello World!")
send("Hello World!")
send("Hello World!")
send("Hello World!")
send("Hello World!")
send("Hello World!")
send("Hello World!")

send(DISCONNECT_MESSAGE)
