import speech_recognition as sr # recognise speech
import playsound # to play an audio files
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
import os # to remove created audio files
import subprocess
import pyttsx3
import bs4 as bs
import urllib.request
import ezgmail
import pywhatkit
import subprocess
import wolframalpha
import requests
import json
import datetime
import pyjokes
import pvporcupine

client = wolframalpha.Client("LVATP4-5RLRA9YLTT")

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 10, 10)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(asis_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine_speak('good morning sir')
    elif hour>=12 and hour<18:
        engine_speak('Good afternoon sir')
    else:
        engine_speak('Good evening sir')

def respond(voice_data):
    
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        wishMe()
        greetings = ["vanakam, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)
    
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        wishMe()
        greetings = ["vanakam, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)
    
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            engine_speak("my name is zuzak, i'm your medical virtual assistant... ")
        else:
            engine_speak("i dont know my name . what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object

    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)

    if there_exists(["aids"]):
        engine_speak("tamil or english")
        ask = record_audio()
        if ask == "tamil": 
            search_term=voice_data.split("for")[-1]
            url="https://www.medlife.com/blog/hiv-aids-symptoms-prevention-methods-arigurigal-sikichai/?lang=ta"
            webbrowser.get().open(url)
            engine_speak("information about aids in tamil")
        if ask == "english":
            search_term=voice_data.split("for")[-1]
            url="https://www.mayoclinic.org/diseases-conditions/hiv-aids/symptoms-causes/syc-20373524#:~:text=Acquired%20immunodeficiency%20syndrome%20(AIDS)%20is,to%20fight%20infection%20and%20disease"
            webbrowser.get().open(url)
            engine_speak("information about aids in english")

    if there_exists(["chicken pox"]):
        engine_speak("tamil or english")
        ask = record_audio()
        if ask == "tamil":
            search_term=voice_data.split("for")[-1]
            url="https://tamil.samayam.com/photogallery/health/chicken-pox-symptoms-causes-and-prevention/photoshow/61300806.cms"
            webbrowser.get().open(url)
            engine_speak("information about chicken pox in tamil")
        if ask == "english":
            search_term=voice_data.split("for")[-1]
            url="https://www.mayoclinic.org/diseases-conditions/chickenpox/symptoms-causes/syc-20351282"
            webbrowser.get().open(url)
            engine_speak("information about chicken pox in english")

    if there_exists(["cholera"]):
        engine_speak("tamil or english")
        ask = record_audio()
        if ask == "tamil":
            search_term=voice_data.split("for")[-1]
            url="https://www.myupchar.com/ta/disease/cholera"
            webbrowser.get().open(url)
            engine_speak("information about cholera in tamil")
        if ask == "english":
            search_term=voice_data.split("for")[-1]
            url="https://www.mayoclinic.org/diseases-conditions/cholera/symptoms-causes/syc-20355287#:~:text=Cholera%20is%20a%20bacterial%20disease,eliminated%20cholera%20in%20industrialized%20countries"
            webbrowser.get().open(url)
            engine_speak("information about cholera in english")

    if there_exists(["dengue fever","mosquito fever"]):
        engine_speak("tamil or english")
        ask = record_audio()
        if ask == "tamil":
            search_term=voice_data.split("for")[-1]
            url="https://tamil.samayam.com/lifestyle/home-remedies/prevention-and-symptoms-of-dengue-fever/articleshow/71502562.cms"
            webbrowser.get().open(url)
            engine_speak("information about  in tamil")
        if ask == "english":
            search_term=voice_data.split("for")[-1]
            url="https://www.mayoclinic.org/diseases-conditions/dengue-fever/symptoms-causes/syc-20353078#:~:text=Mild%20dengue%20fever%20causes%20a,pressure%20(shock)%20and%20death"
            webbrowser.get().open(url)
            engine_speak("information dengue fever in english")

    if there_exists(["diptheria"]):
        engine_speak("tamil or english")
        ask = record_audio()
        if ask == "tamil":
            search_term=voice_data.split("for")[-1]
            url="https://www.myupchar.com/ta/disease/diphtheria"
            webbrowser.get().open(url)
            engine_speak("information about diptheria in tamil")
        if ask == "english":
            search_term=voice_data.split("for")[-1]
            url="https://www.healthline.com/health/diphtheria"
            webbrowser.get().open(url)
            engine_speak("information diptheria in english")

    if there_exists(["hepatitis"]):
        engine_speak("tamil or english")
        ask = record_audio()
        if ask == "tamil":
            search_term=voice_data.split("for")[-1]
            url="https://tamil.samayam.com/lifestyle/health/causes-symptoms-and-vaccines-for-hepatitis-a-b-types-in-tamil/articleshow/74524291.cms"
            webbrowser.get().open(url)
            engine_speak("information about  in tamil")
        if ask == "english":
            engine_speak("which type ?")
            type = record_audio()
            if type =="a":
                search_term=voice_data.split("for")[-1]
                url="https://www.mayoclinic.org/diseases-conditions/hepatitis-a/symptoms-causes/syc-20367007#:~:text=Hepatitis%20A%20is%20a%20highly,your%20liver's%20ability%20to%20function"
                webbrowser.get().open(url)
                engine_speak("information about hepatitis A in english")
            if type == "b":
                search_term=voice_data.split("for")[-1]
                url="https://www.mayoclinic.org/diseases-conditions/hepatitis-b/symptoms-causes/syc-20366802"
                webbrowser.get().open(url)
                engine_speak("information about hepatitis A in english")
    
    if there_exists(["influenza"]):
        engine_speak("tamil or english")
        ask = record_audio()
        if ask == "tamil":
            search_term=voice_data.split("for")[-1]
            url="https://www.myupchar.com/ta/disease/flu-influenza"
            webbrowser.get().open(url)
            engine_speak("information about influenza in tamil")
        if ask == "english":
            search_term=voice_data.split("for")[-1]
            url="https://www.mayoclinic.org/diseases-conditions/flu/symptoms-causes/syc-20351719"
            webbrowser.get().open(url)
            engine_speak("information about influenza in english")

    if there_exists(["leprosy","hansen disease"]):
        engine_speak("tamil or english")
        ask = record_audio()
        if ask == "tamil":
            search_term=voice_data.split("for")[-1]
            url="https://www.myupchar.com/ta/disease/leprosy"
            webbrowser.get().open(url)
            engine_speak("information about leprosy in tamil")
        if ask == "english":
            search_term=voice_data.split("for")[-1]
            url="https://www.medicinenet.com/leprosy/article.htm"
            webbrowser.get().open(url)
            engine_speak("information about leprosy in english")

    if there_exists(["malaria"]):
        engine_speak("tamil or english")
        ask = record_audio()
        if ask == "tamil":
            search_term=voice_data.split("for")[-1]
            url="https://www.medlife.com/blog/%E0%AE%AE%E0%AE%B2%E0%AF%87%E0%AE%B0%E0%AE%BF%E0%AE%AF%E0%AE%BE-%E0%AE%85%E0%AE%B1%E0%AE%BF%E0%AE%95%E0%AF%81%E0%AE%B1%E0%AE%BF%E0%AE%95%E0%AE%B3%E0%AF%8D-%E0%AE%95%E0%AE%A3%E0%AF%8D%E0%AE%9F/?lang=ta"
            webbrowser.get().open(url)
            engine_speak("information about malaria in tamil")
        if ask == "english":
            search_term=voice_data.split("for")[-1]
            url="https://www.mayoclinic.org/diseases-conditions/malaria/symptoms-causes/syc-20351184"
            webbrowser.get().open(url)
            engine_speak("information about malaria in english")

    if there_exists(["measles","rubeola"]):
        engine_speak("tamil or english")
        ask = record_audio()
        if ask == "tamil":
            search_term=voice_data.split("for")[-1]
            url="https://www.myupchar.com/ta/disease/measles"
            webbrowser.get().open(url)
            engine_speak("information about measles in tamil")
        if ask == "english":
            search_term=voice_data.split("for")[-1]
            url="https://www.mayoclinic.org/diseases-conditions/measles/symptoms-causes/syc-20374857"
            webbrowser.get().open(url)
            engine_speak("information about measles in english")
    
    if there_exists (["bye","exit"]):
        engine_speak("thanks for using me...")
        engine_speak("hope we will meet again...")


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'zuzak'
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("welcome... I'm Zuzak... I'm your medicsl chat bot what can i do for you ?") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond

