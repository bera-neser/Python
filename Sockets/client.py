import socket

SRV_ADDR = input("Type the server IP address (default is 127.0.0.1): ")
SRV_PORT = input("Type the server Port (default is 1337): ")

if not SRV_ADDR.strip():
    SRV_ADDR = "127.0.0.1"
if not SRV_PORT:
    SRV_PORT = 1337

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((SRV_ADDR, int(SRV_PORT)))
print("Connection established")

while True:
    message = input("send: ")
    if message == "avokado":
        break
    my_socket.sendall(message.encode())

print("Terminating connection...")
my_socket.close()
