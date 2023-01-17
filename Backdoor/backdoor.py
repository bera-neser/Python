import socket, os, platform

SRV_ADDR = "127.0.0.1"
SRV_PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
connection, address = s.accept()

while True:
    try:
        request = connection.recv(1024)
    except:
        continue

    if request.decode("utf-8") == "1":
        tosend = platform.platform() + " " + platform.machine()
        connection.sendall(tosend.encode())
    elif request.decode("utf-8") == "2":
        request = connection.recv(1024)
        try:
            filelist = os.listdir(request.decode("utf-8"))
            tosend = ""
            for x in filelist:
                tosend += "," + x
        except:
            tosend = "Wrong path"
        connection.sendall(tosend.encode())
    elif request.decode("utf-8") == "0":
        break

connection.close()
