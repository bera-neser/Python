import http.client

host = input("Enter the host/IP (e.g. google.com): ")
try:
    port = int(input("Enter the port (default:80): "))
except ValueError:
    port = 80
path = input("Enter the path (default:'/'): ")

if port == "":
    port = 80
if port is None or path == "":
    path = "/"

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request("GET", path)
    response = connection.getresponse()
    print("Server response:", response.status)
    connection.close()
except ConnectionRefusedError:
    print("Connection Error.")
