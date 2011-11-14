import time, sys, const

_name = "Default/Built-in Plugin"
_author = "B1naryth1ef"
_version = 0.1

def cmdHelp(obj): pass
	#format should be !command : Info \n
def cmdList(obj): pass
	#Format should be !command, !othercommand, !otherothercommand, etc
def cmdSlap(obj): pass
	#Format should be !slap int or !slap name/partial name (Use regex?)
def cmdSet(obj): pass
	#Format should be !set variable value
def cmdMap(obj): pass
	#format should be !map map gamemode(Or none)
def cmdStop(obj): pass
	#format should be !stop
def cmdRestart(obj): pass
	#format should be !restart (Both bot/server)
def cmdLoadout(obj): pass
	#format should be !loadout int, or playername (regex?)
def cmdTester(obj):
	api.say('Testing! This is just a test! Stay clam!')
def testEvent(obj):
	time.sleep(5)
	api.say('TESTING 1... 2... 3...')
def cmdTime(obj):
	if obj.data['msg'].startswith('!tstart'):
		time = time.time()
	elif obj.data['msg'].startswith('!tstop'):
		time2 = time.time()
		api.say('Timer: %s%s' % (api.BLUE, time2-time))
		time = None
		time2 = None

def testPlugin(obj):
	if obj == 'init':
		pass #setup stuff
	elif obj.type == "GAME_FLAGPICKUP":
		pass
	elif obj.type == "GAME_FLAGDROP":
		pass
	elif obj.type == "GAME_FLAGRETURN":
		pass
	

def init(A):
	global api
	api = A
	api.addCmd('!help', cmdHelp, "List all commands")
	api.addCmd('!list', cmdList, "List all users (with UID's)")
	api.addCmd('!slap', cmdSlap, "Slap a player")
	api.addCmd('!set', cmdSet, "Set a Q3 Variable")
	api.addCmd('!map', cmdMap, "Load a map")
	api.addCmd('!stop', cmdStop, "Stop the server/bot")
	api.addCmd('!restart', cmdRestart, "Restart the server/bot")
	api.addCmd('!loadout', cmdLoadout, "See a players loadout")
	api.addCmd('!test', cmdTester, ">:D")
	api.addCmd('!tstart', cmdTime, "Start the timer")
	api.addCmd('!tstop', cmdTime, "Stop the timer")
	api.addEvent('CLIENT_CONNECT', testEvent)

def die(): pass #Called when we should disable/shutdown