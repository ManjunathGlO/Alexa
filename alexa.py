import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen to user input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return "None"
        return command

def execute_command(command):
    """Execute tasks based on the command."""
    if "wikipedia" in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "play music" in command:
        music_dir = "C:\\Users\\YourUsername\\Music"  # Update to your music directory
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif "time" in command:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}.")

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I am not sure how to do that.")

if __name__ == "__main__":
    speak("Hello, I am your assistant. How can I help you?")
    while True:
        command = take_command()
        if command != "None":
            execute_command(command)
