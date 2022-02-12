import socket

SRV_ADDR = input("Please enter the server IP address (default is 127.0.0.1): ")
SRV_PORT = input("Please enter the server Port (default is 1337): ")

if not SRV_ADDR.strip(): SRV_ADDR = "127.0.0.1"
if not SRV_PORT: SRV_PORT = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, int(SRV_PORT)))
s.listen(1)
print("Server started! Waiting for connections...")

connection, address = s.accept()
print("Client connected with address:", address)

while True:
	data = connection.recv(1024)
	if not data: break
	connection.sendall(b"-- Message Received --\n")
	print("client:", data.decode("utf-8"))

connection.close()
print("Connection terminated.")