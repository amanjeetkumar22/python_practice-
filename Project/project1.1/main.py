import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()




print(sr.Microphone.list_microphone_names())
if __name__== "__main__":
    speak("Initialising jarvis...")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone 

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source,timeout=2)

        print("Recognising...")
        try:
            command = r.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Sphinx error;{0}".format(e))


