import sys

passin = sys.argv[1]

dirname = "/Developer/specter/modules/"+passin+".py"
moduledir = "/Developer/specter/modules/"+passin+"module.py"

contents = open(dirname, "r")
#print(contents.read())

modcontents = open(moduledir, "r")
#print(modcontents.read())
import os
os.system("python3 "+dirname)