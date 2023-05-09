import os, math, simpleLib as sl, pyfiglet
from pyfiglet import Figlet

global items
items = []

def Direction():
	os.system("clear")

	print(sl.Color.BLUE + sl.figText("Register 2.0", "slant") + sl.Color.END)
	print(sl.boldText("[StoreClerk]") + " Welcome to my register.")
	print(sl.boldText("[StoreClerk]") + " Please give me the prices of all of your items.")

	userInput = input(sl.boldText("        [Me] "))
	while sl.isInt(userInput):
		items.append(float(userInput))
		userInput = input(sl.boldText("        [Me] "))

	calculateMoney()

def calculateMoney():
	print(sl.boldText("[StoreClerk]") + " How much money do you have?: ")

	moneyGiven 	= input(sl.boldText("        [Me] "))
	total 		= sum(items)
	change 		= int(moneyGiven) - int(total)

	if change > 0:
		finalizeChange(float(change))
	elif change == 0:
		print("[StoreClerk] Your change is 0. Have a nice day!")
	else:
		print("[StoreClerk] I'm sorry, I am going to need more money.")

def finalizeChange(change):
	print(change)

if __name__ == "__main__":
	Direction()