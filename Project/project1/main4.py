import speech_recognition as sr
import pyttsx3
import webbrowser
import time

# recognizer
r = sr.Recognizer()

# text to speech engine
engine = pyttsx3.init('sapi5')

# voice settings
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)


def speak(text):
    print("Jarvis:", text)

    engine.say(text)
    engine.runAndWait()


def processcommand(c):

    c = c.lower()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open kaggle" in c:
        speak("Opening Kaggle")
        webbrowser.open("https://kaggle.com")

    else:
        speak("Command not recognized")


# startup voice
speak("Initializing Jarvis")

while True:

    try:

        # LISTEN
        with sr.Microphone() as source:

            print("Listening...")

            r.adjust_for_ambient_noise(source, duration=1)

            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        # recognize
        word = r.recognize_google(audio)

        print("You said:", word)

        # activation word
        if "hello" in word.lower():

            # IMPORTANT
            time.sleep(0.5)

            speak("Yes sir")

            # second command
            with sr.Microphone() as source:

                print("Jarvis Active...")

                r.adjust_for_ambient_noise(source, duration=1)

                audio = r.listen(source)

            command = r.recognize_google(audio)

            print("Command:", command)

            processcommand(command)

    except sr.WaitTimeoutError:
        print("Timeout")

    except sr.UnknownValueError:
        print("Could not understand")

    except Exception as e:
        print("Error:", e)