### This was written as a joke for my Highschool Reading teacher.
### I wanted to make a program that would help guess the answers to a test.

import os, pyfiglet, random
from pyfiglet import Figlet

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
	print(color.BOLD + "      Thompson is so " + color.END)
	print(color.RED + Figlet(font='slant').renderText('CUTE') + color.END)
	print(color.PURPLE + "Select one of the following: " + color.END)
	print(" 1. A,B,C,D")
	print(" 2. True/False")
	print(" 3. 1-10 A-J\n")
	print("This is the last time I am using this btw...")
	selection = input("")
	os.system("clear")
	print(color.BOLD + "      Thompson is so " + color.END)
	print(color.RED + Figlet(font='slant').renderText('CUTE') + color.END)
	questions = input("How many questions are there: ")
	if selection == "1":
		selOne(int(questions))
	elif selection == "2":
		selTwo(int(questions))
	elif selection == "3":
		selThree(int(questions), "")
	else:
		Direction()

def selOne(questions): # A,B,C,D
	choices = ["A", "B", "C", "D"]

	for i in range(questions):
		print(str(i+1).zfill(2) + ": " + random.choice(choices))

	a = input("Press [ENTER] to randomize more.")
	if a == "" or a == " ":
		selOne(questions)

def selTwo(questions): # True/False
	choices = ["True", "False"]

	for i in range(questions):
		print(str(i+1).zfill(2) + ": " + random.choice(choices))

	a = input("Press [ENTER] to randomize more.")
	if a == "" or a == " ":
		selTwo(questions)

def selThree(questions, answersRaw): # 1-10 A-J
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	answers = []
	answersRaw = questions

	for i in range(int(answersRaw)):
		answers.append(alphabet[i])

	usedAnswers = []
	
	for i in range(questions):
		while True:
			answer = random.choice(answers)
			if answer not in usedAnswers:
				usedAnswers.append(answer)
				print(str(i+1).zfill(2) + ": " + answer)
				break

	a = input("Press [ENTER] to randomize more.")
	if a == "" or a == " ":
		selThree(questions, answersRaw)

if __name__ == "__main__":
	Direction()