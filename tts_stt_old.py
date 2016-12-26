import os
import speech_recognition as sr

com_sign = "Bot >> " 


r = sr.Recognizer()
while True:
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.adjust_for_ambient_noise(source)
        print(com_sign+"Say something")
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

    try:
        user_message = r.recognize_google(audio)
        user_message_str = user_message.lower()
        print("You said >> " + user_message_str)      # recognize speech using Google Speech Recognition        
        os.system("espeak '"+user_message_str+"'")
        if user_message_str == "thank you":
            print("bye bye!")
            break
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")
    except sr.UnknownValueError:
        print(com_sign+"could not understand audio")
    except sr.RequestError as e:
        print(com_sign+"Could not request results$; {0}".format(e))
