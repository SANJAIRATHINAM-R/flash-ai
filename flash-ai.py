import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore
import openai # type: ignore
import os
from dotenv import load_dotenv # type: ignore

# Load OpenAI API key from .env file (recommended for security)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Configure TTS voice rate and volume
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand."
    except sr.RequestError:
        return "Speech recognition service is unavailable."

def generate_ai_reply(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if your account supports it
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

def handle_command(command):
    command = command.lower()
    if "hello" in command:
        return "Hi! How can I help you today?"
    elif "your name" in command:
        return "I am your AI assistant."
    elif "how are you" in command:
        return "I'm doing great, thank you!"
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        return generate_ai_reply(command)

# Main loop
speak("Voice Assistant activated. Say something.")
while True:
    command = listen()
    print("You:", command)
    reply = handle_command(command)
    speak(reply)

