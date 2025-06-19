# flash-ai
# 🔊 Flash AI Voice Assistant

Flash is a Python-based voice assistant powered by OpenAI's GPT model. It listens to your voice commands, processes them using GPT-3.5/4, and responds with synthesized speech.

---

## 🚀 Features

- 🎙️ Speech recognition via `speech_recognition`
- 🧠 AI responses from `OpenAI` API (GPT-3.5/GPT-4)
- 🔊 Voice reply via `pyttsx3` (offline TTS engine)
- 🔐 Secure API key handling from `key.env`

---

## 🛠️ Requirements

Make sure you have Python **3.8+** installed. Then install dependencies:

```bash
pip install -r requirements.txt
If you face issues with pyaudio on Windows:
pip install pipwin
pipwin install pyaudio
📁 Setup
Create a file named key.env in the project root.

Paste your OpenAI API key inside key.env (no quotes):

Copy
Edit
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
(Optional) Update the model in code if you want to use "gpt-4".

🧠 How It Works
The assistant activates on run.

Listens via microphone.

Sends spoken command to OpenAI Chat API.

Converts AI response into speech.

Loops until you say "exit" or "bye".

▶️ Run the Assistant
bash
Copy
Edit
python flash.py
Example interaction:

vbnet
Copy
Edit
Assistant: Voice Assistant activated. Say something.
You: Who is Elon Musk?
Assistant: Elon Musk is a technology entrepreneur and CEO of SpaceX and Tesla...
📦 File Structure
graphql
Copy
Edit
flash-ai/
│
├── flash.py          # Main assistant script
├── key.env           # Contains your OpenAI API key
├── requirements.txt  # All Python dependencies
└── README.md         # Project documentation
🛡️ Security Notice
Never share your key.env file or expose your OpenAI API key in public repositories.

📃 License
This project is released under the MIT License.

yaml
Copy
Edit

---

Would you also like a `requirements.txt` file to go with this?
