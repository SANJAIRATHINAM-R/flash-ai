import speech_recognition as sr  # type: ignore
import pyttsx3  # type: ignore
import openai
import os

# Load OpenAI API key from file
if not os.path.exists("key.env"):
    raise FileNotFoundError("Missing 'key.env'. Please create the file and paste your API key into it.")

with open("key.env", "r") as f:
    api_key = f.read().strip()

client = openai.OpenAI(api_key=api_key)

# Initialize speech recognition and TTS
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand."
    except sr.RequestError:
        return "Speech recognition service is unavailable."
    except Exception as e:
        return f"Error with microphone: {e}"

def generate_ai_reply(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
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
        return "I am Flash, your AI assistant."
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
