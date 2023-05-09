### A small script I made while in engineering class that tells you your age in 10, 20, 30, years.

import requests
from bs4 import BeautifulSoup 

print("Hello, welcome to Life Statistics. \nLet's start with a couple of questions.")

def GetWorldPopulation():
	url = "https://countrymeters.info/en/World"
	resp = requests.get(url)
	if resp.status_code == 200: # IF WE CONNECTED
		soup = BeautifulSoup(resp.text, 'html.parser') # Start PARSER
		count = soup.find("div", {"id":"cp1"})
		for i in count.findAll(isdigit()):
			count = i
	return count

def GetInformation():
	global name
	global age
	global agei
	global sex

	name = input("What is your name?: ")
	age = input("Okay, " + name + ", What is your birth year?: ")
	agei = -5
	while agei == -5:
		try:
			agei = int(age)
		except:
			age = input("Must be an integer. What is your birth year?")

	sex = input("Are you male or female? (M or F): ")
	while sex.lower() != "m" and sex.lower() != "f":
		sex = input("Are you male or female? (M or F): ")
	if sex.lower() == "m":
		sex = "Male"
	else:
		sex = "Female"
	Results()

def Results():
	print("Okay, so your name is " + name + ". You are " + str(2019 - int(age)) + " years old. And you are a " + sex + ".")
	a = input("Everything look correct? (Y or N): ")
	if a.lower() == "n":
		GetInformation()
	elif a.lower() != "y":
		Results()
	elif a.lower() == "y":
		print("You will be " + str(2020 - int(agei)) + " in 2020.")
		print("You will be " + str(2025 - int(agei)) + " in 2025.")
		print("You will be " + str(2030 - int(agei)) + " in 2030.")
		print("You will be " + str(2035 - int(agei)) + " in 2035.")
		print("You will be " + str(2040 - int(agei)) + " in 2040.")
		print("You will be " + str(2045 - int(agei)) + " in 2045.")
		print("You will be " + str(2050 - int(agei)) + " in 2050.")
		print("You will be " + str(2055 - int(agei)) + " in 2055.")
		print("You will be " + str(2060 - int(agei)) + " in 2060.")
		print("You will be " + str(2065 - int(agei)) + " in 2065.")
		print("You will be " + str(2070 - int(agei)) + " in 2070.")
		print("You will be " + str(2075 - int(agei)) + " in 2075.")
		print("You will be " + str(2080 - int(agei)) + " in 2080.")
		print("You will be " + str(2085 - int(agei)) + " in 2085.")
		print("You will be " + str(2090 - int(agei)) + " in 2090.")
		print("You will be " + str(2095 - int(agei)) + " in 2095.")
		print("You will be " + str(2100 - int(agei)) + " in 2100.")
		if (2100 - int(agei)) >= 80:
			print("You will probably be dead by then...")
		# print(GetWorldPopulation())

if __name__ == "__main__":
	GetInformation()

input("")
