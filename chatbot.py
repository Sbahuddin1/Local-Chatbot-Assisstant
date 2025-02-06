import speech_recognition as sr
import win32com.client as wincl
import os
import webbrowser as wb
from deepseek import generate_response
# Dictionary of sites
sites = {
    'youtube': 'https://www.youtube.com/',
    'google': 'https://www.google.com/',
    'facebook': 'https://www.facebook.com/',
    'linkedin': 'https://www.linkedin.com/',
    'instagram': 'https://www.instagram.com/',
    'twitter': 'https://www.twitter.com/',
    'whatsapp': 'https://web.whatsapp.com/',
    'github': 'https://www.github.com/',
    'stackoverflow': 'https://www.stackoverflow.com/',
    'medium': 'https://www.medium.com/',
    'gmail': 'https://www.gmail.com/',
    'amazon': 'https://www.amazon.com/',
    'flipkart': 'https://www.flipkart.com/',
    'snapdeal': 'https://www.snapdeal.com/',
    'ebay': 'https://www.ebay.com/',
    'myntra': 'https://www.myntra.com/',
    'paytm': 'https://www.paytm.com/',
    'udemy': 'https://www.udemy.com/',
    'coursera': 'https://www.coursera.org/',
    'udacity': 'https://www.udacity.com/',
    'kaggle': 'https://www.kaggle.com/',
    'hackerrank': 'https://www.hackerrank.com/',
    'leetcode': 'https://www.leetcode.com/',
    'codecademy': 'https://www.codecademy.com/',
    'geeksforgeeks': 'https://www.geeksforgeeks.org/',
    'w3schools': 'https://www.w3schools.com/'
}

def speak(text):
    """Speak the provided text using Windows SAPI."""
    speaker = wincl.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def listen_for_phrase(prompt=None):
    """
    Listen for audio and convert it to text.
    Optionally, speak a prompt before listening.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Optionally prompt the user
        if prompt:
            speak(prompt)
        # Adjust for ambient noise (helpful to ignore background hum)
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"Recognized: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Request error from speech recognition service:", e)
            return ""

if __name__ == "__main__":
    speak("Hello, how can I help you?")
    
    while True:
        # Step 1: Always listen for the wake word.
        wake_word_query = listen_for_phrase()
        if "hey jarvis" in wake_word_query:
            # The wake word was detected, now listen for the actual command.
            command = listen_for_phrase("Yes, I'm listening.")
            
            if not command:
                # If no command is captured, skip this cycle.
                continue

            # Optional: Allow exit command
            if "exit" in command:
                speak("Goodbye!")
                break

            # Handle website opening commands
            if "open" in command:
                opened = False
                for site in sites:
                    if site in command:
                        speak(f"Opening {site}")
                        wb.open(sites[site])
                        opened = True
                        break
                if not opened and "open music" in command:
                    speak("Opening Music")
                    os.system("start mswindowsmusic:")
            
            # Handle AI-related command
            elif "using artificial intelligence" in command:
                # Pass the command (or a refined prompt) to your AI module
                response = generate_response(command)
                speak(response)
            
            else:
                # Optionally handle any other commands here.
                speak("I did not understand the command.")
        else:
            # If the wake word is not present, do nothing (or add a small delay)
            continue
