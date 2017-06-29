import string
import os
from Read import parseLine, parsedata
from Socket import openSocket, sendMessage, ping
from Initialize import joinRoom
from Func import uptime


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

s = openSocket()
channel_id = joinRoom(s)
readbuffer = ""

while True:
	readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
	temp = readbuffer.split("\n")
	readbuffer = temp.pop()
	
	for line in temp:
		print(line)
		if line == "PING :tmi.twitch.tv\r":
			ping(s)
		else:
			user, message = parseLine(s, line)
			if message == "quit":
				quit()
			elif "nice" in message.lower():
				niceCount += 1
				if niceCount % 100 == 0:
					sendMessage(s, "Nice Count: " + str(niceCount) + " PogChamp")
				else:
					sendMessage(s, "Nice Count: " + str(niceCount))
					
				# this is where I save over the current niceCount in data.dat
				dat["niceCount"] = niceCount
				with open("../data/data.dat", "w+") as datafile:
					for key in dat:
						datafile.write(key + "=" + str(dat[key]))
			elif message == "!uptime":
				sendMessage(s, uptime(s, channel_id))
			elif message == "!help":
				pass