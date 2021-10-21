import socket,sys,os


def port_connect(host,port):
    try:
        connection = socket.socket()
        connection.settimeout(0.5)
        connection.connect((host,port))
        print("The port ", port, " is opened")
    except:
        print("The port ", port, " is closed")

host = input("Enter the host:")
start_port = int(input("Enter the start port:"))
end_port = int(input("Enter the end port:"))

for port in range(start_port, end_port+1):
    port_connect(host,port)