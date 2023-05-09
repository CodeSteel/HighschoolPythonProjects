# This was my favorite project, the Google Image Lyric Generator. The idea was to give it a .mp3 file and it return a music video filled with google images. It works, sorta.
# May come back to this in the future, most likely with C# though...

import os, json, urllib.request, ssl, pyfiglet, io, requests, shutil, audioread
from bs4 import BeautifulSoup, SoupStrainer
from pyfiglet import Figlet
from scipy.io import wavfile
from PIL import Image

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums, types

lyrics = []
startLyrics = []
videos = []

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

def getSoup(url):
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
	r = requests.get(url, headers=header)
	return BeautifulSoup(r.text, 'lxml')
	
def Direction():
	os.system("cls")
	print(color.BOLD + Figlet(font='big').renderText('GILG') + color.END)
	print(color.BOLD + " Google Image Lyric Generator".upper() + color.END)
	print(color.GREEN + "       Made by SteelZK\n" + color.END)

	global audioFileRaw
	audioFileRaw = input(color.BLUE + "Audio File (wav): " + color.END)
	folderName = input(color.BLUE + "Folder name to save files to: " + color.END)
	
	if not os.path.isdir(folderName): # If folderName hasn't already been created, create one.
		os.system("mkdir " + folderName) # Create folderName Directory

	print("\nSplitting WAV audio channels...")

	audioFile = wavSplitter(audioFileRaw, folderName) # Split audio into 2 channels
	audioParser(audioFile, folderName)

def wavSplitter(audioFileRaw, folderName):
	fs, data = wavfile.read(audioFileRaw)
	audioFileRaw = audioFileRaw[:-4]
	wavfile.write(folderName + "/" + audioFileRaw + "EDIT.wav", fs, data[:, 0])
	return folderName + "/" + audioFileRaw + "EDIT.wav"

def getWavDuration(audioFile):
	with audioread.audio_open(audioFile) as f:
		return f.duration

def audioParser(audioFile, folderName):
	client = speech.SpeechClient()

	with io.open(audioFile, 'rb') as audio_file:
		content = audio_file.read()
		audio = types.RecognitionAudio(content=content)

	config = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16, language_code='en-US', enable_word_time_offsets=True)
	operation = client.long_running_recognize(config, audio)

	print('Waiting for operation to complete...')
	result = operation.result(timeout=90)

	for result in result.results:
		alternative = result.alternatives[0]
		for word_info in alternative.words:
			word = word_info.word
			start_time = word_info.start_time.seconds + word_info.start_time.nanos * 1e-9
			# end_time = word_info.end_time.seconds + word_info.end_time.nanos * 1e-9

			lyrics.append(word)
			startLyrics.append((word, start_time))

	imageParser(lyrics, folderName, startLyrics, getWavDuration(audioFile))

def imageParser(lyrics, folderName, startLyrics, mp4Length):
	fileIncrement = 0 # For every word in lyrics.
	dlImages = []
	lyricDuration = getLyricDuration(startLyrics, mp4Length)

	print("Duration: " + str(lyricDuration))

	for word in lyrics:
		url = "https://www.google.com/search?q=" + word + "&source=lnms&tbm=isch" # Search for word in Google Images
		soup = getSoup(url) # Get the Soup of the google search.
		fileIncrement += 1
		gate = True 

		for a in soup.find_all("div", {"class":"rg_meta"}): # Find all pictures
			try:
				if gate == True:
					url = json.loads(a.text)["ou"] 
					Type = json.loads(a.text)["ity"] # The picture type
					fileName = word + "." + Type

					if word not in dlImages:
						downloadImage(url, fileName, folderName, word)

					for i in range(len(lyricDuration)):
						if word == lyricDuration[i][0]:
							if i == (fileIncrement - 1):
								makeVideo(fileName, folderName, lyricDuration[i][1], fileIncrement)
								break
					
					dlImages.append(word)
					gate = False
			except urllib.request.HTTPError as error:
				print("[Error] " + str(error.code))
				gate = True
				continue
	readyFiles(folderName)

def downloadImage(url, fileName, folderName, word):
	print("\n'" + word + "'")
	print("Downloading: " + folderName + "/" + fileName)
	
	with urllib.request.urlopen(url) as u: # Open a URL request to download
		image = open(fileName.zfill(3),'wb') # Open image
		image.write(u.read()) # Download image
		image.close()

	print(url)
	shutil.move(fileName, folderName) # Move image into directory.

def getLyricDuration(tupTable, mp4Length):
	sub = []
	for i in range(len(tupTable)):
		if i == 0:
			sub.append((tupTable[i][0], tupTable[1][1]))
		elif i < len(tupTable) - 1:
			sub.append((tupTable[i][0], tupTable[i+1][1] - tupTable[i][1]))
		else:
			sub.append((tupTable[i][0], int(mp4Length) - tupTable[i][1]))
	return sub

def makeVideo(fileName, folderName, duration, name):
	duration = round(duration, 3)
	name = str(name).zfill(3)
	os.system("C:\\Users\\Ghost\\Desktop\\Projects\\Python\\GoogleCloud\\GILG\\ffmpeg\\bin\\ffmpeg.exe -hide_banner -loop 1 -i {} -t {} -s:v 1280x720 -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p {}.mp4".format(folderName + "/" + fileName, duration, name))
	os.system("move {}.mp4 {}".format(name, folderName))

def readyFiles(folderName):
	files = os.listdir(folderName)
	fileCount = input("FileCount?: ")
	textFile = open(folderName + "/" + folderName + ".txt", 'w+')
	for count, filename in enumerate(sorted(files), start=1):
		if count < int(fileCount) + 1:
			textFile.write("file " + filename + "\n")
	textFile.close()
	makeMovie(folderName)

def makeMovie(folderName):
	os.system("C:\\Users\\Ghost\\Desktop\\Projects\\Python\\GoogleCloud\\GILG\\ffmpeg\\bin\\ffmpeg.exe -hide_banner -f concat -safe 0 -i {}/{}.txt -i {} {}.mp4".format(folderName, folderName, audioFileRaw, folderName))
	shutil.move(folderName + ".mp4", folderName)

if __name__ == "__main__":
	Direction()
