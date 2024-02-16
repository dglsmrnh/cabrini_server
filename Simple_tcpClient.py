from socket import *

g = 125
n = 98
x = 200

serverName = "10.1.70.32"
serverPort = 15200
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:
    sentence = input("Input lowercase sentence: ")
    if not sentence == "":
        clientSocket.send(bytes(sentence, "utf-8"))
        modifiedSentence = clientSocket.recv(1024)
        text = str(modifiedSentence,"utf-8")
        print ("Received from Make Upper Case Server: ", text)
        if text == "EXIT":
            clientSocket.detach()
            break