# TEAM AUDIT SYSTEMS EMPLOYEE MONITORING SYSTEM SERVER CONNECTOR

### IMPORTS ###
import socket, os
from threading import *

### VARIABLES ###
matchingKey = "deneme123"
clientOrder = 0

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

### SERVER CONFIG ###
ServerPort = 10808

### THREADING ###

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.clientSocket = socket
        self.clientAddress = address
        self.start()

    def run(self):
        while True:
            global clientOrder
            clientOrder += 1
            print(f" [*] [{clientaddress[0]}:{clientaddress[1]}] Trying to Connect as Client [{clientOrder}]...")
            while True:
                if self.clientSocket.recv(1024).decode("utf-8") == matchingKey:
                    print(f" [*] [{clientaddress[0]}:{clientaddress[1]}] Successfully Connected as [{clientOrder}].")
                    self.clientSocket.send(bytes("10808", "utf-8"))
                    operationType = self.clientSocket.recv(1024).decode("utf-8")
                    if operationType == "SQL":
                        self.clientSocket.send(bytes("sql_approved", "utf-8"))
                        print(f" [{clientOrder}] Approved For Sending SQL.")
                        SQLcode = ""
                        while True:
                            clientFeedback = self.clientSocket.recv(1024)
                            if len(clientFeedback) <= 0:
                                break
                            SQLcode += clientFeedback.decode("utf-8")
                        print(f" [{clientOrder}] SQL: {SQLcode}")
                        # SQL import codes comes here!
                        clientsocket.close()
                        print(f" [{clientOrder}] Client Disconnected!")
                        break
                    elif operationType == "OCR":
                        # OCR image import codes comes here!
                        break
                    else:
                        clientsocket.close()
                        print(f" [{clientOrder}] Connection Aborted. Unknown Operation!")
                        break
                else:
                    clientsocket.close()
                    print(f" [*] [{clientaddress[0]}:{clientaddress[1]}] as [{clientOrder}] Connection Aborted. Unknown Client!")
                    break
            break

### MAIN ###
os.system('clear')
print("""
  ______                        ___             ___ __ 
 /_  __/__  ____ _____ ___     /   | __  ______/ (_) /_
  / / / _ \/ __ `/ __ `__ \   / /| |/ / / / __  / / __/
 / / /  __/ /_/ / / / / / /  / ___ / /_/ / /_/ / / /_  
/_/  \___/\__,_/_/ /_/ /_/  /_/  |_\__,_/\__,_/_/\__/  
                                                       
Team Audit Employee Tracking System Server-side Script
""")
print("Server Started!\n")


serverSocket.bind((socket.gethostname(), ServerPort))
serverSocket.listen(8)

while True:
    clientsocket, clientaddress = serverSocket.accept()
    client(clientsocket, clientaddress)