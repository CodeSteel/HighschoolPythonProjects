import os, easymodule as em, subprocess, json
from terminalFunctions import *

user = "term"
computerName = "Emulator"
termColor1 = em.Color.GREEN
termColor2 = em.Color.BLUE

inputHistory = []

def printHeader():
	print("Steel's Terminal")

def getInput(cwd): # steel@Steel-HP:~/Desktop$ python3
	userInput = input("{}{}{}@{}{}:{}{}~{}{}$ ".format(em.Color.BOLD, termColor1, user, computerName, em.Color.END, em.Color.BOLD, termColor2, cwd, em.Color.END))
	inputHistory.append(userInput)
	return userInput

def acceptInput():
	while True:
		userInput = getInput(os.getcwd()).split(" ")

		with open("/home/steel/Desktop/Projects/Python/Terminal/config.json", "r") as config:
			data = json.load(config)

			if userInput[0] in data.keys():
				globals()[data[userInput[0]]](userInput)
			else:
				print("'" + userInput[0] + "' does not exist.")


if __name__ == "__main__":
	os.system("clear")
	printHeader()

	try:
		acceptInput()
	except KeyboardInterrupt:
		try:
			input("\nType 'CTRL + C' to Exit ")
			os.system("python3 terminalEmulator.py")
		except:
			os.system("clear")
