from simpleOSC import initOSCServer, startOSCServer, closeOSC, setOSCHandler
import OSC
from array import array

ip = "127.0.0.1"
port = 9125
NUMBER_OF_LIGHTS = 25
DEFAULT_COLOR = [130, 130, 130]

def stuff():
	import time

	a = []
	a.len
	
	initOSCServer(ip, port)
	
	setOSCHandler('/collision', collision)

	startOSCServer()
	print "server is running, listening at " + str(ip) + ":" + str(port)

	try:
		while(1):
			time.sleep(1000)
	except KeyboardInterrupt:
		print "closing all OSC connections... and exit"
		closeOSC() # finally close the connection before exiting or program.

def collision(addr, tags, data, source):
	print "HEY I GOT A THING!!!"
	print "addr = " + str(addr) # /collision
	print "tags = " + str(tags) # is
	print "data = " + str(data) # [444, 'stuff']
	print "sour = " + str(source) # (network info)
	
stuff()
