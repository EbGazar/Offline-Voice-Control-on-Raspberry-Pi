import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    print("Assistant : " + audio)
    engine.say(audio)
    engine.runAndWait()
    