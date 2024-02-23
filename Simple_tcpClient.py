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
        r2 = int(clientSocket.recv(1024))
        k = (r2**x)%n
        print("k = ", k)
    else:
        rawSentence = input("Input lowercase sentence: ")
        if not rawSentence == "":
            sentence = ""
            for c in rawSentence:
                c = chr(ord(c) + k)
                sentence += c
            clientSocket.send(bytes(sentence, "utf-8"))
            print("Waiting for answer...")
            modifiedSentence = clientSocket.recv(1024)
            rawText = str(modifiedSentence,"utf-8")
            text = ""
            for c in rawText:
                c = chr(ord(c) - k)
                text += c
            print ("Received from \"Make Upper Case\" Server: ", text)
        else:
            clientSocket.detach()
            r2 = 0
            k = 0
            keySent = False
            break