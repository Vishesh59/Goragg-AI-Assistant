
import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr  

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    print("Goragg", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")
    
    except Exception as e:
        
        print("Say that again please...")
        return "None"
        
    return query.lower()

sites = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "linkedin": "https://linkedin.com",
    "dsa": "https://www.youtube.com/playlist?list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz"

}

speak("Heyy.. Vishesh, I am Goragg. What should i do for you?")

while True:
    command = take_command()
    
    if command: 
        print(f"You said: {command}")

       
        for site in sites:
            if site in command:
                speak(f"Opening {site}")
                webbrowser.open(sites[site])

        
        if "time" in command:
            speak(datetime.datetime.now().strftime("It's %I:%M %p"))
        

        elif "say hello to" in command:
       
            name = command.replace("say hello to", "").strip()
        
        
            if name:
                speak(f"Hello {name}, how are you doing today?")
            else:
                speak("Who should I say hello to?")

        elif "greet" in command or "great" in command:
            name = command.replace("greet", "").replace("great","").strip()
            speak(f"Greetings {name}! Welcome to AI system made by vishesh.")
        
        elif "search" in command:
            ser= command.replace("search", "").strip()
            speak(f"searching {ser} on your browser")
            webbrowser.open(f"https://www.google.com/search?q={ser}")
        
        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break
    