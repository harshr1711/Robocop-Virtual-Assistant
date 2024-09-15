import speech_recognition as sr
import webbrowser
import pyttsx3
import pygame
import requests
from openai import OpenAI


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "7ee11e159f9342f794996f9769de17cf"

def speak(text):
    engine.say(text)
    engine.runAndWait()
 

def aiProcess(command):
    client = OpenAI(
        api_key = "sk-sEKhf5c62GDTsq5b5KGxZlQ_********************************************************"
    )

    completion = client.chat.completion.create(
    model = "gpt-3.5-turbo",
    messages = [
       {"role": "system", "content": "You are a virtual assistant named RoboCop skilled in task completion"},
       {"role": "user", "content": command }
    ]
    )

    return completion.choices[0].message.content




def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open stock" in c.lower():
        webbrowser.open("https://www.screener.in/explore/")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = pygame.mixer.music[song]
        webbrowser.open(link)
        #pygame.mixer.music.load(self.playlist[song])
                
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    else:
        # Let openAI handle the request
        output = aiProcess(c)
        speak(output)



if __name__ == "__main__":
    speak("Initializing Robocop....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "robocop"):
                speak("Robocop is ready to interact")
                # Listen for command
                with sr.Microphone() as source:
                    print("Robo Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))