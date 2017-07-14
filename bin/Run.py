import string
import os
from Read import parseLine, parsedata
from TwitchBot import TwitchBot
from Settings import CHANNEL, NICK, HOST, PORT, PASS, CLIENT_ID

try:
	with open("../data/data.dat", "r") as datafile:
		dat = parsedata(datafile)
	if len(dat) == 0:
		dat["niceCount"] = 0
except FileNotFoundError:
	dat = {}
	dat["niceCount"] = 0
	f = open("../data/data.dat", "w+")

tbot = TwitchBot(NICK, CLIENT_ID, PASS, CHANNEL)
readbuffer = ""

while True:
	readbuffer = readbuffer + tbot.s.recv(1024).decode("UTF-8")
	temp = readbuffer.split("\n")
	readbuffer = temp.pop()
	
	for line in temp:
		print(line)
		if line == "PING :tmi.twitch.tv\r":
			tbot.ping()
		else:
			user, message = parseLine(tbot.s, line)
			if message == "quit":
				tbot.sendMessage("Quitting")
				with open("../data/data.dat", "w+") as datafile:
					for key in dat:
						datafile.write(key + "=" + str(dat[key]))
				quit()
			elif "nice" in message.lower():
				dat["niceCount"] = tbot.niceCounter(dat["niceCount"])
			elif message == "!uptime":
				tbot.uptime()
			elif message == "!help":
				tbot.help()