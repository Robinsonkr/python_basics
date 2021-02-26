#pyttsx3 is a text to speech coversion library in python
import pyttsx3


def text_to_speech(mytext):
	txt_spc = pyttsx3.init()  #initialize pyttsx3 in our function
	#convert string to speech
	txt_spc.say("{}".format(mytext))
	txt_spc.runAndWait()


mytext="Hello robinson"

text_to_speech(mytext)