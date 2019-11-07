#!/usr/bin/python3

print (' _______  _______ .______   .______      __   __       _______ ')
print ('|   ____||   ____||   _  \  |   _  \    |  | |  |     |   ____|')
print ('|  |__   |  |__   |  |_)  | |  |_)  |   |  | |  |     |  |__   ')
print ('|   __|  |   __|  |   _  <  |      /    |  | |  |     |   __|  ')
print ('|  |     |  |____ |  |_)  | |  |\  \----|  | |  `----.|  |____ ')
print ('|__|     |_______||______/  | _| `._____|__| |_______||_______|')
print ('                         PORT SCANNER                 BY FRANK0T')






import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)
