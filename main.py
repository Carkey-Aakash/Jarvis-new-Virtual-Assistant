import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="75fa6b858ce147c28f464a9274b27c78"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = OpenAI(
    api_key="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"
)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis same as alexa and google cloud."},
            {
                "role": "user",
                "content": "what is content"
            }
        ]
    )
    return (completion.choices[0].message.content)

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open chrome" in c.lower():
        webbrowser.open("https://chrome.com")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON data
            data = r.json()
            
            # Extract the articles
            articles = data.get("articles", [])
            #printing the headlines
            for article in articles:
                speak(article['title'])

    else:
        output=aiprocess(c)
        speak(output)



if __name__=="__main__":
   speak("Initializing Jarvis...")

while True:
    # Listen for the wake word "Jarvis"
    # Obtain audio from the microphone
    r = sr.Recognizer()

    print("Recognizing...")
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("Yaa")

                #Listen for the command
                with sr.Microphone() as source:
                    print("Jarvis activating...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    command = r.recognize_google(audio)
                    processcommand(command)

            
    except Exception as e:
        print("Error: {0}".format(e))
