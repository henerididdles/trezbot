import string
import requests
import socket
from pprint import pprint
from Settings import HOST, PORT
#todo: make this into a class

class TwitchBot(object):
	
	def __init__(self, username, client_id, oauth, channel):
		self.username = username
		self.client_id = client_id
		self.oauth = oauth
		self.channel = channel
		
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((HOST, PORT))
		self.s.send(bytes("PASS " + oauth + "\r\n", "UTF-8"))
		self.s.send(bytes("NICK " + username + "\r\n", "UTF-8"))
		self.s.send(bytes("JOIN #" + channel + "\r\n", "UTF-8"))
		
		url = "https://api.twitch.tv/kraken/users?login=" + channel
		headers = {"Client-ID": client_id, "Accept": "application/vnd.twitchtv.v5+json"}
		r = requests.get(url, headers = headers).json()
		self.channel_id = r['users'][0]['_id']
		pprint(r)
		
		readbuffer = ""
		Loading = True
		while Loading:
			readbuffer = readbuffer + self.s.recv(1024).decode("UTF-8")
			temp = readbuffer.split("\n")
			readbuffer = temp.pop()
			
			for line in temp:
				print(line)
				Loading = self.loadingComplete(line)
		self.sendMessage("Successfully joined chat")
		
	def loadingComplete(self, line):
		if("End of /NAMES list" in line):
			return False
		return True
	
	def sendMessage(self, message):
		messageTemp = "PRIVMSG #" + self.channel + " :" + message
		self.s.send(bytes(messageTemp + "\r\n", "UTF-8"))
		print("Sent: " + messageTemp)

	def ping(self):
		self.s.send(bytes("PONG\r\n", "UTF-8"))
		print("PONG")