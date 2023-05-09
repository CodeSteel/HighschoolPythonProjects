import os, pyaudio, wave, io, time
from scipy.io import wavfile

# Imports the Google Cloud client library
from google.cloud import speech, translate
from google.cloud.speech import enums, types

class color:
   BOLD = '\033[1m'
   END = '\033[0m'

def Direction():
	print("STEEL's Real Time Translator")
	optOut = input("Press [ENTER] when ready...")

	while optOut == "":
		try:
			print("Recording...")
			recordAudio()
			print("Finished...")
			audioFile = getAudio("audio.wav")
			audioSpeech = getSpeech(audioFile)
			for i in audioSpeech:
				print("What I think you said: " + i)
				print("Translated: " + transText(i, "es"))
		except KeyboardInterrupt as e:
			print("Quitting...")
			time.sleep(.5)
			break

def recordAudio():
	wavOutFile = "audio.wav"
	rate = 44100
	duration = 3	
	 
	audio = pyaudio.PyAudio()

	stream = audio.open(format=pyaudio.paInt16, channels=2, rate=rate, input=True, frames_per_buffer=1024)
	frames = []
	 
	for i in range(int(rate / 1024 * duration)):
		data = stream.read(1024)
		frames.append(data)

	stream.stop_stream()
	stream.close()
	audio.terminate()
	 
	waveFile = wave.open(wavOutFile, 'wb')
	waveFile.setnchannels(2)
	waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
	waveFile.setframerate(rate)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()

def getAudio(audioFileRaw):
	fs, data = wavfile.read(audioFileRaw)
	audioFileRaw = audioFileRaw[:-4]
	wavfile.write(audioFileRaw + "EDIT.wav", fs, data[:, 0])
	return audioFileRaw + "EDIT.wav"

def getSpeech(audioFile):
	text = []
	client = speech.SpeechClient()

	with io.open(audioFile, 'rb') as audio_file:
		content = audio_file.read()
		audio = types.RecognitionAudio(content=content)

	config = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16, language_code='en-US')
	operation = client.long_running_recognize(config, audio)

	print('Waiting for operation to complete...')
	result = operation.result(timeout=90)

	for result in result.results:
		alternative = result.alternatives[0]
		text.append(alternative.transcript)

	return text

def transText(text, targetLang):
	translateClient = translate.Client()
	translation = translateClient.translate(text, target_language=targetLang)
	return translation['translatedText']

if __name__ == "__main__":
	Direction()
