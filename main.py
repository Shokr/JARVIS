"""
JARVIS:
- Control Windows programs with your voice

__author__ = 'Muhammed Shokr <mohammedshokr2014@gmail.com>'
__version__ = 'v 1.0'

JARVIS repo <https://github.com/Shokr/JARVIS>
"""

# import modules

# subprocess module allows you to spawn new processes
import subprocess

# importing the pyttsx3 library
import pyttsx3
# speech_recognition Library for performing speech recognition with support for Google Speech Recognition
import speech_recognition as sr

# initialisation
engine = pyttsx3.init()

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    engine.say("Say something")
    engine.runAndWait()
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
Query = r.recognize_google(audio)
print(Query)


# Run Application with Voice Command Function
def get_app(query):
    cmd = {
        "browser": "C:\Program Files\Internet Explorer\iexplore.exe",
        "calculator": "calc.exe",
        "cmd": "cmd.exe",
        "notepad": "Notepad.exe",
        "paint": "mspaint.exe",
        "shell": "powershell.exe",
        "stikynot": "StikyNot.exe",
    }.get(query.lower())
    if cmd:
        subprocess.call([cmd])
    else:
        engine.say("Sorry Try Again")
        engine.runAndWait()


def main():

    # Call get_app(Query) Func.
    get_app(Query)


if __name__ == "__main__":
    main()
