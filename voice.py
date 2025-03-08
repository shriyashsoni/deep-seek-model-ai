import speech_recognition as sr
from gtts import gTTS
import os

def recognize_speech():
    """Convert speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand."
    except sr.RequestError:
        return "Could not request results."

def text_to_speech(text):
    """Convert AI response to speech."""
    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")
    os.system("start response.mp3")  # Use 'mpg321 response.mp3' for Linux
