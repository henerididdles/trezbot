import string
import os
from Read import parseLine, parsedata
from Initialize import TwitchBot
from Func import uptime
from Settings import CHANNEL, NICK, HOST, PORT, PASS, CLIENT_ID


try:
	with open("../data/data.dat", "r") as datafile:
		dat = parsedata(datafile)
		if len(dat) == 0:
			niceCount = 0
		else:
			niceCount = dat['niceCount']
except FileNotFoundError:
	dat = {}
	niceCount = 0
	dat["niceCount"] = niceCount
	with open("../data/data.dat", "w+") as datafile:
		for key in dat:
			datafile.write(key + "=" + str(dat[key]))

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
				quit()
			elif "nice" in message.lower():
				niceCount += 1
				if niceCount % 100 == 0:
					tbot.sendMessage("Nice Count: " + str(niceCount) + " PogChamp")
				else:
					tbot.sendMessage("Nice Count: " + str(niceCount))
					
				# this is where I save over the current niceCount in data.dat
				dat["niceCount"] = niceCount
				with open("../data/data.dat", "w+") as datafile:
					for key in dat:
						datafile.write(key + "=" + str(dat[key]))
			elif message == "!uptime":
				tbot.sendMessage(uptime(tbot.s, tbot.channel_id))
			elif message == "!help":
				pass