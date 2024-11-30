import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import random
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak a given text
def say(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice commands from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Pause threshold for speech recognition
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()  # Return query in lowercase
        except Exception as e:
            say("Sorry, I didn't catch that. Please repeat.")
            return "None"

# Function to handle website searches
def perform_search(site_name, search_query):
    search_urls = {
        "google": "https://www.google.com/search?q=",
        "youtube": "https://www.youtube.com/results?search_query=",
        "wikipedia": "https://en.wikipedia.org/wiki/",
        "amazon": "https://www.amazon.com/s?k=",
        "flipkart": "https://www.flipkart.com/search?q=",
        "udemy": "https://www.udemy.com/courses/search/?q=",
        "coursera": "https://www.coursera.org/search?query=",
        "linkedin": "https://www.linkedin.com/search/results/all/?keywords=",
        "reddit": "https://www.reddit.com/search/?q=",
    }
    
    if site_name in search_urls:
        search_url = search_urls[site_name] + search_query.replace(" ", "+")
        webbrowser.open(search_url)
        say(f"Searching {search_query} on {site_name} for you.")
    else:
        say(f"Sorry, I don't have search functionality for {site_name} yet.")

# Main program
if __name__ == '__main__':
    say("Hello, I am your AI assistant. How can I assist you today?")
    
    while True:
        query = takeCommand()
        if query == "None":
            continue

        # Exit condition
        if "exit" in query or "bye" in query:
            say("Goodbye! Have a nice day.")
            break

        # Handle user-friendly search requests
        if "open" in query:
            try:
                words = query.split("open")[1].strip()  # Extract everything after "open"
                site_name = None
                search_query = None

                # Identify the site and search query
                for site in ["google", "youtube", "wikipedia", "amazon", "flipkart", "udemy", "coursera", "linkedin", "reddit"]:
                    if site in words:
                        site_name = site
                        search_query = words.replace(site, "").strip()
                        break
                
                if site_name and search_query:
                    perform_search(site_name, search_query)
                elif site_name:
                    webbrowser.open(f"https://{site_name}.com")
                    say(f"Opening {site_name} for you.")
                else:
                    say("Sorry, I couldn't understand your request.")
            except Exception as e:
                say("Sorry, I couldn't process your request. Please try again.")

        # Play music
        elif 'play music' in query or 'play songs' in query:
            music_dir = 'D:\\rsk\\MUSIC'
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:  # Check if the directory has songs
                    random_song = random.choice(songs)
                    os.startfile(os.path.join(music_dir, random_song))
                    say(f"Playing {random_song} for you.")
                else:
                    say("The music directory is empty.")
            else:
                say("The music directory does not exist.")
        
        # Tell the current time
        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {current_time}.")

