#!/usr/bin/env python3

import socket
import json

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

#Creating an Dictionarie
data = {'Zustand_Robo':1 , 'Fehler_Robo': False}

#Sequenzing the dictionarie in preparation to transmit it via Socket
data_stream = json.dumps(data)

#Creating a Socket an transmitting Data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(data_stream,encoding="utf-8"))  #It's requiered to encode the Data
    data = s.recv(1024)                             #Data is beeing received from (echo)server in 1024 bit strings
    data_json = data.decode("utf-8")                #It's requiered to dencode the Data
    robo = json.loads(data_json)                    #String is beeing transfaierd back into dictionarie

print('Received "repr"', repr(data))
print('Received "decode"', robo['Fehler_Robo'])