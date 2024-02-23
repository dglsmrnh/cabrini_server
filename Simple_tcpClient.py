from socket import *

g = 11
n = 33
r1 = 0
r2 = 0
k = 0
keySent = False

serverName = "10.1.70.32"
serverPort = 15200
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:

    if not keySent:
        x = input("Define a personal key for this connection: ")
        r1 = (g**x)%n
        keySent = True
        clientSocket.send(bytes(r1, "utf-8"))
        print("Waiting for server key...")
        r2 = clientSocket.recv(1024)
        k = (r2**x)%n
    else:
        sentence = input("Input lowercase sentence: ")
        if not sentence == "":
            clientSocket.send(bytes(sentence, "utf-8"))
            print("Waiting for answer...")
            modifiedSentence = clientSocket.recv(1024)
            rawText = str(modifiedSentence,"utf-8")
            for c in rawText:
                c = ord(c) + k
            print ("Received from \"Make Upper Case\" Server: ", rawText)
            if rawText == "EXIT":
                clientSocket.detach()
                r2 = 0
                k = 0
                keySent = False
                break