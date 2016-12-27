import os
import speech_recognition as sr
from time import ctime
import webbrowser
import json
from random import randint
import urllib
from gtts import gTTS
import random

com_sign = "Bot >> " 
man_sign = "You >> " 


def speak(audioString):
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

    
def tell_me_joke():    
    sub = "jokes"
    json_loc = "https://www.reddit.com/r/" + sub + ".json"
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(json_loc, headers = headers)
    response = urllib.request.urlopen(req)    
    # Convert bytes to string type and string type to dict
    string = response.read().decode('utf-8')
    json_data = json.loads(string)
    post = json_data["data"]["children"][randint(0, 24)]["data"]
    title = post["title"].replace("'","")
    title = post["title"].replace("\"","")
    selftext = post["selftext"].replace("'","")
    selftext = post["selftext"].replace("\"","")
    return title + "," + selftext

def show_me_map(line):
    line_ar = line.split(" ")
    location_name = str(line_ar[-1])
    bot_answer = "Showing you "+location_name+" in map."    
    #os.system("espeak '"+bot_answer+"'")
    url = "https://www.google.com/maps/place/" + location_name + "/&amp;"
    webbrowser.open(url)
    return bot_answer
    
def show_me_website(line):
    line_ar = line.split(" ")
    website_name = str(line_ar[-1])
    bot_answer = "Showing you "+website_name+" in map."    
    #os.system("espeak '"+bot_answer+"'")
    url = "http://"+website_name
    webbrowser.open(url)
    return bot_answer
    
word_map = {
    "hi":["Hi! How are you?","Hello there!"],        
    "hello":["Hi! How are you?","Hello there!"],        
    "your name":["My name is Pyvis.","I am Pyvis and I am invisible"],
    "pyvis":["Yes sir?","What can I do for you, sir?"],
    "how are you":["I am fine. Thank you for asking.","Not bad!"],
    "who are you?":["I am Pyvis. I am here to assist you.","I am your digital assistant, Pyvis"],
    "love me":["I love everyone.","I love coding"],
    "shut up":["Okay, Boss!","See you soon!"],
    "fuck":["Be gentle please.","I thought you are better than this!","Dont be rediculous."],
    "bitch":["Be gentle please.","I thought you are better than this!","Dont be rediculous."],
    }


r = sr.Recognizer()
while True:
    current_time = str(ctime())
    word_map["time"] = [current_time,"Its now: "+current_time]
    '''
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.adjust_for_ambient_noise(source)
        print(com_sign+"Say something")
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    '''        
    try:
        #user_message = r.recognize_google(audio)
        #user_message_str = user_message.lower()
        user_message_str = input(com_sign+"Write something: ")
        print(man_sign + user_message_str)    # recognize speech using Google Speech Recognition
        
        for key in word_map.keys():
            if key in user_message_str:
                bot_answer = random.choice(word_map[key])
                print(com_sign+bot_answer)
                #os.system("espeak '"+bot_answer+"'")
                speak(bot_answer)

        if "shut up" in user_message_str:
            break
        if "show me" in user_message_str:
            bot_answer = show_me_map(user_message_str)
            print(com_sign+bot_answer)
            #os.system("espeak '"+bot_answer+"'")
            speak(bot_answer)
        if "joke" in user_message_str:
            bot_answer = tell_me_joke()
            print(com_sign+bot_answer)
            #os.system("espeak '"+bot_answer+"'")
            speak(bot_answer)        
        if "open" in user_message_str:
            bot_answer = show_me_website(user_message_str)
            print(com_sign+bot_answer)
            #os.system("espeak '"+bot_answer+"'")
            speak(bot_answer)
        
        
        
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")
    except sr.UnknownValueError:
        print(com_sign+"could not understand audio")
    except sr.RequestError as e:
        print(com_sign+"Could not request results$; {0}".format(e))
