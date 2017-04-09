import os

def acc():
	package = open(os.getcwd()+"/package.json", "w")
	package.write("{")
	package.write("\n")
	package.write("    \"name\": \""+project+"\",")
	package.write("\n")
	package.write("    \"description\": \""+description+"\",")
	package.write("\n")
	package.write("    \"author\": \""+author+"\",")
	package.write("\n")
	package.write("    \"width\": 800,")
	package.write("\n")
	package.write("    \"height\": 600")
	package.write("\n")
	package.write("}")
	print("Wrote 7 lines.")

author = input("Author: ")
project = input("Project Name: ")
description = input("Description: ")

print("package.json: ")
print("{")
print("    \"name\": \""+project+"\",")
print("    \"description\": \""+description+"\",")
print("    \"author\": \""+author+"\",")
print("    \"width\": 800,")
print("    \"height\": 600")
print("}")

accept = input("Are you Happy with this? (Y/N) ")
if accept == "Y":
	acc()

	pass
elif accept == "y":
	acc()

	pass