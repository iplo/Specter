import os

def appname():
	cwd = os.getcwd()
	array = cwd.split('/')
	arraylen = len(array)
	return array[arraylen - 1]