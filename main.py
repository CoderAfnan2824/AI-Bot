import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib
import os
from openai import OpenAI

engine=pyttsx3.init()

client = OpenAI(
    # This is the default and can be omitted
    api_key="0FlCC5Vxci9ixgcglbnrVprxbRfjhxpGrX7TgRWdvYlrTsSkOfyoRbfS4OiJjsm2zTxNAA",
)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(c):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
                {"role": "system", "content": "You are a virtual assistant like Google and Alexa. Process the input and Generate an Output."},
                {"role": "user", "content": c}
            ]
)
    return completion.choices[0].message.content


def processCommand(c):
   print("processing command")
   if("open google" in c.lower()):
       webbrowser.open("https://google.com")
   elif("open youtube" in c.lower()):
       webbrowser.open("https://youtube.com")

   elif(c.lower().startswith("play")):
       print("hello world")
       song=c.lower().split(" ")[1]
       link=musicLib.music[song]
       webbrowser.open(link)
   else:
       output=aiprocess(c)
       speak(output)
       

if __name__ =="__main__":
    speak("JARVIS Initializing.....")
    
    while True:

        # obtain audio from the microphone
        r = sr.Recognizer()
        
        # recognize speech using Google Speech Recognition
        print("Google recognizing Audio")
        try:
            with sr.Microphone() as source:
               print("Google Listening..!!")
               audio = r.listen(source, timeout=3,phrase_time_limit=2)
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            word=r.recognize_google(audio)
            print(word)

            if(word.lower()=="jarvis"):
                speak("Ya")
                with sr.Microphone() as source:
                   print("JARVIS ACTIVE..!!")
                   audio = r.listen(source, timeout=3,phrase_time_limit=2)

                command=r.recognize_google(audio)
                print(command)
                processCommand(command)

        except Exception as e:
            print("Error: {0}".format(e))


