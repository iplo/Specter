def startserver(port, filename, app):
	import webbrowser

	appname = app

	url = "localhost:"+port+"/"+appname+'/'+filename

	webbrowser.open('file:///Developer/specter/open.script.html?url='+url+'&new=window&width=800&height=600&appname='+appname,new=2)