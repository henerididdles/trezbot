import socket
from Settings import HOST, PORT, PASS, NICK, CHANNEL

def openSocket():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, 6667))
	s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
	s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
	s.send(bytes("JOIN #" + CHANNEL + "\r\n", "UTF-8"))
	return s

	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(bytes(messageTemp + "\r\n", "UTF-8"))
	print("Sent: " + messageTemp)

def ping(s):
	s.send(bytes("PONG\r\n", "UTF-8"))
	print("PONG")