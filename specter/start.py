import sys
import os

filedir = os.getcwd()+'/package.json';

details = open(filedir, "r");

obj = details.read()

print(obj)

import webbrowser

appname = "MyApp"

filename = "index.html"

url = os.getcwd()+'/'+filename

webbrowser.open('file:///Developer/specter/open.script.html?url='+url+'&new=window&width=800&height=600&appname='+appname,new=2)