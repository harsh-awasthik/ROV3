import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip = "169.254.242.160" #Replace this with the BS IP (Get IP by hostname -I)
server_port = 7777 #Check the Port and allow it via firewall.
s.bind((server_ip, server_port))
