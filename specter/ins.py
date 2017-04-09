import sys

repos = {
"chromium": "./modules/chromium"
}

passin = sys.argv[1]
print("installing "+passin+"...")
urlbase = "./modules/"+passin
print(urlbase)
i = 0

while i<10:
	print(i+1)

	i += 1
	pass