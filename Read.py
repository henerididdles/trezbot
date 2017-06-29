import string

def parseLine(s, line):
	separate = line.split(":", 2)
	if len(separate) == 2:
		if line == "PING :tmi.twitch.tv":
			ping(s)
		return (separate[0], separate[1])
	else:
		user = separate[1].split("!", 1)[0]
		message = separate[2][:-1]
		return (user, message)

def parsedata(datafile):
	dat = {}
	
	for s in datafile:
		kvcombo = s.split("=", 1)
		try:
			dat[kvcombo[0]] = int(kvcombo[1])
		except ValueError:
			dat[kvcombo[0]] = 0

	return dat