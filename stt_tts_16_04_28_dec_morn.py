import os
import subprocess
import speech_recognition as sr
from time import ctime
import webbrowser
import json
from random import randint
import urllib
from gtts import gTTS
import random
import wikipedia

com_sign = "Bot >> " 
man_sign = "You >> " 

def remove_quote_mark(passed_str):
    return_str = str(passed_str)
    return_str = return_str.replace("\"","")
    return_str = return_str.replace("'","")
    return return_str

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
    title = title.replace("\"","")
    selftext = post["selftext"].replace("'","")
    selftext = selftext.replace("\"","")
    return title + "," + selftext

def tell_me_quote(line):    
    json_loc = "http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json"
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(json_loc, headers = headers)
    response = urllib.request.urlopen(req)    
    # Convert bytes to string type and string type to dict
    string = response.read().decode('utf-8')
    json_data = json.loads(string)
    quote_text = json_data["quoteText"].replace("'","")
    quote_text = quote_text.replace("\"","")
    quote_author = json_data["quoteAuthor"].replace("'","")
    quote_author = quote_author.replace("\"","")
    return quote_text + ".By " + quote_author

def tell_me_country(line):
    line_ar = line.split(" ")
    country_name = str(line_ar[-1])
    json_loc = "https://restcountries.eu/rest/v1/name/"+country_name+"?fullText=true"
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    return_str = ""
    try:
        req = urllib.request.Request(json_loc, headers = headers)    
        response = urllib.request.urlopen(req)    
        # Convert bytes to string type and string type to dict
        string = response.read().decode('utf-8')
        json_data = json.loads(string)
        json_data = json_data[0]
        country_area = int(json_data["area"])
        country_area = remove_quote_mark(country_area)
        country_capital = remove_quote_mark(json_data["capital"])
        country_population = remove_quote_mark(json_data["population"])
        country_region = remove_quote_mark(json_data["region"])
        country_subregion = remove_quote_mark(json_data["subregion"])
        country_name = country_name.capitalize()
        return_str = country_name+" is situated in "+country_subregion+", of "
        return_str += country_region+". The capital of the coutry is "+country_capital+". "
        return_str += "It has a total "+country_population+" population. "
        return_str += country_name+" covers an area of "+country_area+" square kilometers. "
    except:
        return_str = "Sorry, could not find any information on this."
    return return_str

def tell_me_wiki(line):
    line_ar = line.split(" ")
    pername = str(line_ar[-1])
    sr_engine = wikipedia.search(pername)
    bot_answer = wikipedia.summary(pername,sentences=4)
    return bot_answer 
                
def show_me_map(line):
    line_ar = line.split(" ")
    location_name = str(" ".join(line_ar[1:]))
    bot_answer = "Showing you "+location_name+" in map."    
    #os.system("espeak '"+bot_answer+"'")
    url = "https://www.google.com/maps/place/" + location_name + "/&amp;"
    webbrowser.open(url)
    return bot_answer
    
def show_me_website(line):
    line_ar = line.split(" ")
    website_name = str(line_ar[-1])
    bot_answer = "Showing you "+website_name+" in browser."    
    #os.system("espeak '"+bot_answer+"'")
    url = "http://"+website_name
    webbrowser.open(url)
    return bot_answer

def show_me_lock(line):
    line_ar = line.split(" ")
    subprocess.call(["gnome-screensaver-command", "-l"])
    bot_answer = "Locking your computer, Sir."
    return str(bot_answer)    

word_map = {
    "hi":["Hi! How are you?","Hello there!"],        
    "hello":["Hi! How are you?","Hello there!"],        
    "your name":["My name is Pyvis.","I am Pyvis and I am invisible"],
    "pyvis":["Yes sir?","What can I do for you, sir?"],
    "how are you":["I am fine. Thank you for asking.","Not bad!"],
    "who are you?":["I am Pyvis. I am here to assist you.","I am your digital assistant, Pyvis"],
    "love me":["I love everyone.","I love coding"],
    "shut up":["Okay, Boss!","See you soon!"],
    "*":["Be gentle please.","I thought you are better than this!","Dont be rediculous."],
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
        user_message_str = str(user_message_str).lower()
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
        if "anything" in user_message_str:
            bot_answer = tell_me_wiki(user_message_str)
            print(com_sign+bot_answer)
            #os.system("espeak '"+bot_answer+"'")
            speak(bot_answer)  
        if "open" in user_message_str:
            bot_answer = show_me_website(user_message_str)
            print(com_sign+bot_answer)
            #os.system("espeak '"+bot_answer+"'")
            speak(bot_answer)
        if "country" in user_message_str:
            bot_answer = tell_me_country(user_message_str)
            print(com_sign+bot_answer)
            #os.system("espeak '"+bot_answer+"'")
            speak(bot_answer)
        if "lock" in user_message_str:
            bot_answer = show_me_lock(user_message_str)
            print(com_sign+bot_answer)
            #os.system("espeak '"+bot_answer+"'")
            speak(bot_answer)        
        if "quote" in user_message_str:
            bot_answer = tell_me_quote(user_message_str)
            print(com_sign+bot_answer)
            #os.system("espeak '"+bot_answer+"'")
            speak(bot_answer)        
        
        
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")
    except sr.UnknownValueError:
        print(com_sign+"could not understand audio")
    except sr.RequestError as e:
        print(com_sign+"Could not request results$; {0}".format(e))
