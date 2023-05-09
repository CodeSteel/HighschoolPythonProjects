import math
import os

items = []

def Start(items):
	print("STEEL's Register")
	print("Type in the item's prices then type '-' when finished.")
	price = input("Add a price: ")
	if price != "-":
		items.append(float(price))
	while price != "-":
		price = input("Add a price: ")
		if price != "-":
			items.append(float(price))
		if price == "":
			items.pop()

	total = TotalOut(items)
	total = float(total)
	print("Total: $" + str(format(total, ".2f")))
	money = input("Given Money: ")
	money = float(money)
	if money >= total:
		change = format(money - total, ".2f")
		print("Transaction complete. \nChange: $" + str(change) + ".")
		changeJar = ChangeOut(change)
		print(Results(changeJar))

		input("")
	else:
		print("Transaction canceled.\nMissing: $" + str(format(total - money, ".2f")) + ".")
		option = input("Try Again? (Y or N): ")
		if option.lower() == "y" or option.lower() == "yes":
			Start()

def TotalOut(ls):
	return format(sum(ls), '.2f') # Gets the SUM of the list then formats it to add 2 Zeros

def ChangeOut(change):
# - changeJar = [100, 50, 20, 10, 5, 1] - #
	changeJar = [0, 0 ,0, 0, 0, 0]
	change = float(change) # Turns Change to Float

	if change / 100 >= 1: # if change % 100 == 0
		o = change / 100
		p = math.floor(o)
		change = change - (p * 100)
		changeJar[0] = p
	if change / 50 >= 1:
		o = change / 50
		p = math.floor(o)
		change = change - (p * 50)
		changeJar[1] = p
	if change / 20 >= 1:
		o = change / 20
		p = math.floor(o)
		change = change - (p * 20)
		changeJar[2] = p
	if change / 10 >= 1:
		o = change / 10
		p = math.floor(o)
		change = change - (p * 10)
		changeJar[3] = p
	if change / 5 >= 1:
		o = change / 5
		p = math.floor(o)
		change = change - (p * 5)
		changeJar[4] = p
	if change / 1 >= 1:
		o = change / 1
		p = math.floor(o)
		change = change - (p * 1)
		changeJar[5] = p
	return changeJar

def Results(changeJar):
	moneyJar = []
	if changeJar[0] > 0:
		moneyJar.append("$100: " + str(changeJar[0]))
	if changeJar[1] > 0:
		moneyJar.append("$50: " + str(changeJar[1]))
	if changeJar[2] > 0:
		moneyJar.append("$20: " + str(changeJar[2]))
	if changeJar[3] > 0:
		moneyJar.append("$10: " + str(changeJar[3]))
	if changeJar[4] > 0:
		moneyJar.append("$5: " + str(changeJar[4]))
	if changeJar[5] > 0:
		moneyJar.append("$1: " + str(changeJar[5]))
	p = ""
	for i in moneyJar:
		p = p + i + "\n"
	return "- Bills - \n" + p

if __name__ == "__main__":
	Start(items)