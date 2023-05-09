import os, hashlib, time, pyfiglet
from pyfiglet import Figlet

""" TEST PASSWORD
password = 5f4dcc3b5aa765d61d8327deb882cf99
qwerty = d8578edf8458ce06fbc5bb76a58c5ca4
123456 = e10adc3949ba59abbe56e057f20f883e
5f4dcc3b5aa765d61d8327deb882cf99,d8578edf8458ce06fbc5bb76a58c5ca4,e10adc3949ba59abbe56e057f20f883e
"""

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def Direction():
	os.system("clear")
	print(color.BLUE + Figlet(font='slant').renderText('Decrypter') + color.END)
	decryptText = input(color.BOLD + "Hash(es) to decrypt: " + color.END)
	passList = input(color.BOLD + "Password List (pList.txt): " + color.END)

	if passList == "" or passList == " ":
		passList = "pList.txt"

	singleHash(decryptText, passList)

def singleHash(decryptText, passList):
	try:
		with open(passList) as pList:
			print("-Single Hash-")
			startTime = time.time()
			for line, text in enumerate(pList): 
				text = text.rstrip("\n")
				textHash = hashText(text)

				if textHash.hexdigest() == decryptText:
					endTime = time.time()
					input(color.GREEN + "[FOUND]" + color.END + " The password is: '" + text + "'\nTime: " + str(endTime - startTime) + "\n")
					break
				else:
					print(color.RED + "[FAIL]" + color.END + " The password is not: '" + text + "' " + str(line))
					print(hashText(text).hexdigest() + "\n")
	except:
		print(color.BOLD + "[ERROR] " + color.END + "File '{}' not found.".format(passList))

def hashText(text):
	return hashlib.md5(text.encode())

if __name__ == "__main__":
	Direction()
