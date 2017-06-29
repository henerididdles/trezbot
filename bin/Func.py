import requests
import json
import datetime
from pprint import pprint
from Settings import CHANNEL, CLIENT_ID

def uptime(s, channel_id):
	url = 'https://api.twitch.tv/kraken/streams/' + channel_id
	headers = {'Client-ID': CLIENT_ID, 'Accept': 'application/vnd.twitchtv.v5+json'}
	r = requests.get(url, headers = headers).json()
	#pprint(r)
	
	if r['stream'] is None:
		return "Sorry, the stream isn't online!"
	
	start_time = r['stream']['created_at']
	current_time = datetime.datetime.utcnow()
	
	#datetime conversion + get delta of the start_time and current_time
	start_convert = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
	utime = current_time - start_convert
	uptime = ":".join(str(utime).split(":", 2)[:2])
	
	return "Stream has been live for " + uptime

#todo
def help(s):
	return 'go here to see all the commands   _____'