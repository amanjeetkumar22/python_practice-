import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer=sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    # if "open google" in c.lower():
    #     webbrowser.open("https://google.com")
    # elif "open facebook" in c.lower():
    #     webbrowser.open("https://facebook.com")
    # elif "open youtube" in c.lower():
    #     webbrowser.open("https://youtube.com")
    # elif "open kaggle" in c.lower():
    #     webbrowser.open("https://kaggle.com")
    pass




if __name__== "__main__":
    # speak("Hey sir how may i help uh How are you buddy?")
    speak("Intializing jarvis..")
   
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("---recognizing---")
        try:
            with sr.Microphone() as source:
                print("...Listening...")
                audio=r.listen(source,timeout=2,phrase_time_limit=3)
            word=r.recognize_google(audio)
            if(word.lower() == "hello"):
                speak("Yes sir")
                #listen for command 
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print(" Error:{0}".format(e))        