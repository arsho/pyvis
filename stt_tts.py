import os
import speech_recognition as sr
from time import ctime

com_sign = "Bot >> " 


r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.adjust_for_ambient_noise(source)
    print(com_sign+"Say something")
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

try:
    user_message = r.recognize_google(audio)
    user_message_str = user_message.lower()
    print("You said " + user_message_str)    # recognize speech using Google Speech Recognition
    #os.system("espeak '"+user_message_str+"'")
    if "your name" in user_message_str:
        os.system("espeak 'my_name_is_jarrviss.\n'")
    elif "jarvis" in user_message_str:
        os.system("espeak 'Yes?\n'")
    elif "time" in user_message_str:
        os.system("espeak '"+ctime()+"'")
    elif "how are you" in user_message_str:
        os.system("espeak 'I_am_Fine,Thank_you.What_about_you?\n'")
    elif "about you" in user_message_str:
        os.system("espeak 'I_am_jarvis_and_I_am_coded_in_python.My_CPU_is_2.4_gigahertz_and_I_have_intel_core_i3_processor.I_have_4gb_RAM.\n'")
    elif "are you single" in user_message_str:
        os.system("espeak 'yes...but_i_lovee_IRONMAN.\n'")
    elif "add" in user_message_str:
        os.system("espeak '"+eval("20+40")+"'")
    elif "5 into 5" in user_message_str:
        os.system("espeak 'twentyfive\n'")
    elif "search engine" in user_message_str:
        os.system("espeak 'I_prefer_google.\n'")
    elif "shut up" in user_message_str:
        os.system("espeak 'Okay\n'")
    
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
except sr.UnknownValueError:
    print(com_sign+"could not understand audio")
except sr.RequestError as e:
    print(com_sign+"Could not request results$; {0}".format(e))
