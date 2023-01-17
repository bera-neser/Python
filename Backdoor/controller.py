import socket


def print_menu():
    print(
        """
0) Close the connection
1) Get system info
2) List directory contents
"""
    )


SRV_ADDR = input("IP (default is 127.0.0.1): ")
SRV_PORT = input("Port (default is 4444): ")

if not SRV_ADDR.strip():
    SRV_ADDR = "127.0.0.1"
if not SRV_PORT:
    SRV_PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((SRV_ADDR, SRV_PORT))
    print("Connection established!")

    print_menu()

    while True:
        option = input("Select an option: ")
        if option == "0":
            s.sendall(option.encode())
            break
        elif option == "1":
            s.sendall(option.encode())
            data = s.recv(1024)
            if not data:
                break
            print("\n" + "*" * 40)
            print(data.decode("utf-8"))
            print("*" * 40)
        elif option == "2":
            s.sendall(option.encode())
            path = input("Insert the path: ")
            s.sendall(path.encode())
            data = s.recv(1024)
            data = data.decode("utf-8").split(",")
            print("\n" + "*" * 40)
            for x in data:
                print(x)
            print("*" * 40)
        print_menu()
except Exception as e:
    print(e)

s.close()
