import os
env = open(os.getcwd()+"/.env")
env = env.read()
if env == "default":
	import sys
	import os
	import envirementcontroller as controller
	if sys.argv[1] == "server":
		PORT = input("What port is your server on? ")

		import webbrowser

		appname = controller.appname()

		filename = "index.php"

		url = "localhost:"+PORT+"/"+appname+'/'+filename

		webbrowser.open('file:///Developer/specter/open.script.html?url='+url+'&new=window&width=800&height=600&appname='+appname,new=2)
	pass
	if sys.argv[1] == "app":
		filedir = os.getcwd()+'/package.json';

		details = open(filedir, "r");

		obj = details.read()

		print("Starting app...")

		import webbrowser

		appname = controller.appname()

		filename = open(os.getcwd()+'/.envname', "r")
		filename = filename.read()

		url = os.getcwd()+'/'+filename

		webbrowser.open('file:///Developer/specter/open.script.html?url='+url+'&new=window&width=800&height=600&appname='+appname,new=2)
	pass
else:
	import subprocess
	subprocess.Popen(env+' '+argv)
	pass