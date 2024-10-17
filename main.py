import speech_recognition as sr
import pyttsx3
import  musicLibrary
import webbrowser
import requests
import newsapi
from openai import OpenAI

engine=pyttsx3.init()
newsapi="c364a35d19bf49c6a06c71d9f807c0a0"

def sayself(text):
    engine.say(text)
    engine.runAndWait()
    
def gpt(c):

    client = OpenAI(api_key=" Enter your key")


    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant,named jarvis skilled in doing tasks like alexa and google cloud and please give short responses."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    return (completion.choices[0].message.content)
    
def mygpt(c):
        
    if c.startswith("open"):
        website=c.split("open ")[1]
        webbrowser.open(f"https://www.{website}.com/")
        sayself(f"opening{website}")
        
    elif c.startswith("play"):
        song=c.split("play ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    
    
    
    elif "news" in c:
        r=requests.get(f"Enter your key ={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                sayself(article['title'])
    else:
        a=gpt(c)
        print(a)
        sayself(a)


if __name__=="__main__":
    sayself
    while True: 
        #listen for the word jarvis
        #receive audio form microphone  
        r = sr.Recognizer()
        print("Recognizing...")
        

                
        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Jarvis is listening")
                audio = r.listen(source,timeout=4, phrase_time_limit=2)
            word= r.recognize_google(audio).lower()
            word1= r.recognize_google(audio).lower()
            
            if (word1=="close"):
                print("Program Terminated")
                sayself("Program Terminated")
                break
            
            if (word=="jarvis"):
                sayself("Yes,Boss")
                
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    Command= r.recognize_google(audio).lower()

                    print( "You are saying",Command)
                    
                    mygpt(Command)
                    
                    
                    
            
            
            
        
        except Exception as e:
            print(f"Jarvis error: {e}")
