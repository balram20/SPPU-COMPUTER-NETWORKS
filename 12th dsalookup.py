import socket

hostname = input("Enter the host name or DNS address: ")
print(socket.gethostbyaddr(hostname))