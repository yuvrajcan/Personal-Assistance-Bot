import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import json
from openai import OpenAI





recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def speak(text):
    engine.say(text)
    engine.runAndWait()
    

    
def ask_openai(command):
    client = OpenAI(
    api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a highly intelligent and efficient personal assistant chatbot powered by OpenAI. Your primary goal is to assist the user with daily tasks, productivity, scheduling, reminders, information retrieval, and personalized recommendations."},
        {
            "role": "user",
            "content": command
        }
    ]
)

    return completion.choices[0].message.content

def process_command(command):
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open github" in command.lower():
        webbrowser.open("https://www.github.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com")
    elif command.lower().startswith("play"):
        song=command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in command.lower():
        r=requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}')
        data=r.json() 
        for i in data['articles']:
            speak(i['title'])
            speak("Moving on to the next news...")
            
    else:
        output = ask_openai(command)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Yuvi....")
    while True:
        # Listen for the wake word "Yuvi"
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)  
                print("Recognizing...")
            word = recognizer.recognize_google(audio, language='en-in').lower()


            if "uv" in word:
                speak("Yes, I am here.")
                print("Yuvi active, what can I do for you?")
                
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)  
                    command = recognizer.recognize_google(audio, language='en-in')
                    process_command(command)
        
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please repeat.")
        except sr.RequestError as e:
            print("Error with the speech recognition service; {0}".format(e))
        except Exception as e:
            print("Unexpected error: {0}".format(e))
