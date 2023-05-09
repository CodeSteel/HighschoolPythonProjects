import os, subprocess

def changeCWD(userInput):
	if len(userInput) != 1:
		os.chdir(userInput[1])
	else:
		os.chdir("/home/steel")

def listDir(userInput):
	if len(userInput) == 1:
		os.system("ls")
	else:
		os.system("ls " + userInput[1])

def clearTerminal(userInput):
	os.system("clear")

def nano(userInput):
	os.system(" ".join(userInput))

def removeFile(userInput):
	os.system("rm -rf " + userInput[1])

def runPython3(userInput):
	os.system("python3 " + userInput[1])

def runPython(userInput):
	os.system("python " + userInput[1])

def makeDirectory(userInput):
	os.system("mkdir " + userInput[1])

def printHistory(userInput):
	print(inputHistory)