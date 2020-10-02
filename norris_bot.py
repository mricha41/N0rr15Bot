#http://t.me/N0rr15Bot
#a Telegram bot featuring Chuck Norris facts

#if you don't whish to set this
#just copy the file to the top-level
#folder and run it there w/out this
import sys
sys.path.append(".")
sys.path.append("dokkaebi")
print(sys.path)

import random
from dokkaebi import dokkaebi
from configparser import ConfigParser
import csv

#appending to sys.path allows
#config to be read relative to that path
#even though this file is in the examples folder
config = ConfigParser()
config.read('norris.ini')

#be sure to cast anything that shouldn't
#be a string - reading the .ini file
#seems to result in strings for every item read.
hook_data = {
	'hostname': config["Telegram"]["HOSTNAME"], 
	'port': int(config["Telegram"]["PORT"]), 
	'token': config["Telegram"]["BOT_TOKEN"], 
	'url': config["Telegram"]["WEBHOOK_URL"],
	'environment': config["Telegram"]["ENVIRONMENT"]
}

bot_commands = {
	"commands": [
		{'command': 'start', 'description': 'Starts @N0rr15Bot.'},
		{'command': 'facts', 'description': 'Retrieves a Chuck Norris fact and delivers it piping hot to your chat.'}
	]
}

norris = [
	"https://tumbleroot.files.wordpress.com/2013/04/walker-texas-ranger.jpg",
	"https://external-content.duckduckgo.com/iu/?u=https://mediadc.brightspotcdn.com/dims4/default/4f87e48/2147483647/strip/true/crop/808x808+0+0/resize/808x808!/quality/90/?url=https%3A%2F%2Fmediadc.brightspotcdn.c",
	"https://external-content.duckduckgo.com/iu/?u=https://texashillcountry.com/wp-content/uploads/norris-tex-e1548371046876-660x400.jpg&f=1&nofb=1",
	"https://external-content.duckduckgo.com/iu/?u=https://cdn.flickeringmyth.com/wp-content/uploads/2020/03/chuck-norris.jpg&f=1&nofb=1",
	"https://external-content.duckduckgo.com/iu/?u=https://www.celebsfacts.com/wp-content/uploads/2017/09/Chuck-Norris.jpg&f=1&nofb=1",
	"https://external-content.duckduckgo.com/iu/?u=https://tse3.mm.bing.net/th?id=OIP.Xu7BL6cAPWdEtgDnd6d80gHaFW&pid=Api&f=1",
	"https://external-content.duckduckgo.com/iu/?u=https://v6q9s5t8.ssl.hwcdn.net/wp-content/uploads/2019/04/Full-Auto-Friday-Chuck-Norris-Edition-VIDEOS-696x392.jpg&f=1&nofb=1",
	"https://external-content.duckduckgo.com/iu/?u=https://blog.centurymartialarts.com/hs-fs/hubfs/CENTURION+-+resize/chuck+norris/chuck-3.jpg?width=309&name=chuck-3.jpg&f=1&nofb=1",
	"https://external-content.duckduckgo.com/iu/?u=https://cdn3.whatculture.com/images/2017/10/6a3786ac40ddcbf2-600x338.jpg&f=1&nofb=1",
	"https://external-content.duckduckgo.com/iu/?u=https://www.celebrity-cutouts.co.uk/wp-content/uploads/2018/01/chuck-norris-celebrity-mask.png&f=1&nofb=1"
] 

class Bot(dokkaebi.Dokkaebi):
	def handleData(self, data):
		print(data)
		if "message" in data:
			if "text" in data["message"]:
				command = data["message"]["text"]
			else:
				command = ""

			chat_id = data["message"]["chat"]["id"]
			user_first_name = data["message"]["from"]["first_name"]

			if command in ["/start", "/start@" + self.bot_info["username"]]:
				msg = {
					"chat_id": chat_id,
					"photo": "https://external-content.duckduckgo.com/iu/?u=https://cdn3.whatculture.com/images/2017/10/6a3786ac40ddcbf2-600x338.jpg&f=1&nofb=1",
					"caption": "Thanks for using @"  + self.bot_info["username"] + ", @" + user_first_name + "!",
					"parse_mode": "html"
				}
				print(self.sendPhoto(msg).json())
			elif command in ["/facts", "/facts@" + self.bot_info["username"]]:
				#read in the data
				facts = []
				with open('data/chuck_facts.csv', newline='') as csvfile:
					r = csv.reader(csvfile, delimiter=';', quotechar="'")
					for row in r:
						facts.append(row[1])

				msg = {
					"chat_id": chat_id,
					"photo": random.choice(norris),
					"caption": "- Carlos Ray \"Chuck\" Norris",
					"parse_mode": "html"
				}
				print(self.sendMessage({"chat_id": chat_id, "text": "{}".format(random.choice(facts)), "parse_mode": "html"}).json())
				print(self.sendPhoto(msg).json())
			else:
				msg = {
					"chat_id": chat_id,
					"text": "Chuck Norris is not amused. Please try a valid command @" + user_first_name + ", your life depends on it."
				}
				self.sendMessage(msg)
		
	def onInit(self):
		self.setMyCommands(bot_commands)
		self.getMyCommands()

newBot = Bot(hook_data)