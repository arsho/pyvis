import os
import speech_recognition as sr

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
    if user_message_str == "what is your name":
        os.system("espeak 'my_name_is_jarrviss.\n'")
    elif user_message_str == "jarvis":
        os.system("espeak 'Yes?\n'")
    elif user_message_str == "how are you":
        os.system("espeak 'I_am_Fine,Thank_you.What_about_you?\n'")
    elif user_message_str == "tell me about you":
        os.system("espeak 'I_am_jarvis_and_I_am_coded_in_python.My_CPU_is_2.4_gigahertz_and_I_have_intel_core_i3_processor.I_have_4gb.\n'")
    elif user_message_str == "are you single":
        os.system("espeak 'yes...but_i_lovee_IRONMAN.\n'")
    elif user_message_str == "add 20 + 40":
        os.system("espeak 'sixty\n'")
    elif user_message_str == "5 into 5":
        os.system("espeak 'twentyfive\n'")
    elif user_message_str == "which search engine do you prefer":
        os.system("espeak 'I_prefer_google.\n'")
    elif user_message_str == "shut up":
        os.system("espeak 'Okay\n'")
    
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
except sr.UnknownValueError:
    print(com_sign+"could not understand audio")
except sr.RequestError as e:
    print(com_sign+"Could not request results$; {0}".format(e))
