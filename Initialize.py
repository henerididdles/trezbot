import string
import requests
from pprint import pprint
from Settings import CHANNEL, NICK, HOST, PORT, PASS, CLIENT_ID
from Socket import sendMessage
#todo: make this into a class

def joinRoom(s):
	url = "https://api.twitch.tv/kraken/users?login=" + CHANNEL
	headers = {"Client-ID": CLIENT_ID, "Accept": "application/vnd.twitchtv.v5+json"}
	r = requests.get(url, headers = headers).json()
	channel_id = r['users'][0]['_id']
	pprint(r)
	
	readbuffer = ""
	Loading = True
	while Loading:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	sendMessage(s, "Successfully joined chat")
	return channel_id

def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	return True