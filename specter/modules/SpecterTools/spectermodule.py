def openwindow(fullscreen, url):
	import webbrowser
	if fullscreen == False:
		width = 800
		height = 600
		webbrowser.open('file:///Developer/specter/open.script.html?url='+url+'&new=window&width='+width+'&height='+height+'&appname=Window',new=2)
	else:
		webbrowser.open('file:///Developer/specter/open.script.html?url='+url+'&new=window&appname=Window',new=2)
	
def getFileContents(filename):
	filereader = open(filename, "r")
	return filereader.read()
