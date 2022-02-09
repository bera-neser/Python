import socket

TARGET_IP = input("Please enter the IP you want to scan: ")
PORT_RANGE = input("Please enter the port range yo want to scan (e.g. 5-200): ")

first_port = int(PORT_RANGE.split("-")[0])
last_port = int(PORT_RANGE.split("-")[1])

print(f"Scanning IP {TARGET_IP} for open ports from {first_port} to {last_port}...")

for port in range(first_port, last_port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	status = s.connect_ex((TARGET_IP, port))
	if (status == 0): print(f"port {port} is open.")
	s.close()
