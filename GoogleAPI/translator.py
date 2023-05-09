import os, time, pyfiglet
from google.cloud import translate
from pyfiglet import Figlet

class Color:
	BLUE = '\033[94m'
	END = '\033[0m'

def Direction():
	printHeader()

	text = input("[Google] What to translate?: ")
	transTo = input("[Google] Translate To?: ")

	print("Translating...")

	client = translate.Client()
	translated = client.translate(text, target_language=transTo)
	time.sleep(.6)

	printHeader()
	print("[Google] Translated '{}' to:".format(text))
	print("[Google] " + translated["translatedText"])

	try:
		print("\n" * 8)
		userInput = input("Press [ENTER] to restart.")
		Direction()
	except:
		print("\nQuitting...")

def printHeader():
	os.system("clear")
	print(Color.BLUE + figText("Translator", "big") + Color.END)

def figText(text, font):
	return Figlet(font=font).renderText(text)

if __name__ == "__main__":
	Direction()