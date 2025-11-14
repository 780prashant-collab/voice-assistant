def generate(text):
    return f"Generated reply for: {text}"

def play(audio):
    print("Playing audio:", audio)

import google.generativeai as genai
import pyttsx3

# ---------------------------
# SET GEMINI API KEY
# ---------------------------
def set_api_key(api_key):
    genai.configure(api_key=api_key)


# ---------------------------
# GENERATE TEXT FROM GEMINI
# ---------------------------
def generate(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text


# ---------------------------
# TEXT-TO-SPEECH (OPTIONAL)
# ---------------------------
def play(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
