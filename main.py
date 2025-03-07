import requests
import whisper
import sounddevice as sd
import numpy as np
import soundfile as sf
import pyttsx3
import random
import re
import pygame
import time
import serial

# list of tics audios
# 3, 16, 17, 18, 20, 22, 23, 24 have been removed
PATHS_AUDIO = [
    'assets/audio/1.wav',
    'assets/audio/2.wav',
    'assets/audio/4.wav',
    'assets/audio/5.wav',
    'assets/audio/6.wav',
    'assets/audio/7.wav',
    'assets/audio/8.wav',
    'assets/audio/9.wav',
    'assets/audio/10.wav',
    'assets/audio/11.wav',
    'assets/audio/12.wav',
    'assets/audio/13.wav',
    'assets/audio/14.wav',
    'assets/audio/15.wav',
    'assets/audio/19.wav',
    'assets/audio/21.wav',
    'assets/audio/claquement-2.wav',
    'assets/audio/claquement-3.wav',
    'assets/audio/claquement-4.wav',
    'assets/audio/claquement-5.wav',
]


# Mistral AI API Key
API_KEY = "MY_API_KEY"

# Initializing the speech synthesis engine
engine = pyttsx3.init()

# Loading the Whisper model
print("Initialisation du Brainrot...")
whisper_model = whisper.load_model("base")

# Creation of the prompt that will be sent to the API
def create_prompte(text):
    prompte = "Je souhaiterais que tu incarne du debut a la fin de ta reponse quelqu'un avec des tics. \
La personne qui tu incarne ne devras pas avoir plus de 5 tics dans sa réponse. \
Tout les tics seront representés entre crochets, comme ceci : [tic] \
Plusieurs tics d'affilés soront recrésentés entre crochets et non séparés par des espaces. \
Voici la phrese auquel je veux que tu repondes : "
    prompte += text
    return (prompte)


# Function to record audio
def record_audio(filename="output.wav", duration=5, samplerate=44100):
    print("Parle maintenant...")
    recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.float32)
    sd.wait()
    sf.write(filename, recording, samplerate)
    print("Enregistrement terminé.")

# Function to transcribe audio to text
def transcribe_audio(filename="output.wav"):
    print("Transcription de l'audio en cours...")
    result = whisper_model.transcribe(filename)
    text = result["text"].strip()
    print(f"Transcription détectée : '{text}'")
    return text

# Function to send the request to Mistral AI
def generate_response(prompt):
    if not prompt:
        return "Je n'ai rien compris, peux-tu répéter ?"
    
    print("Génération de la réponse...")
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-tiny",
        "messages": [{"role": "user", "content": create_prompte(prompt)}]
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        ai_response = response.json()["choices"][0]["message"]["content"]
        print(f"{ai_response}")
        return ai_response
    else:
        error_message = f"Erreur API Mistral: {response.status_code} - {response.text}"
        print(f"❌ {error_message}")
        return error_message

def play(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def get_audio_path():
    num_tic = random.randint(0, len(PATHS_AUDIO) - 1)
    return (PATHS_AUDIO[num_tic])

# Function to make AI speak
# Possibility to give him different tics
def speak(text, arduino):
    tab_text = re.split(r"[\[\]]", text)
    for text_i in tab_text:
        match text_i.lower():
            case "tic":
                if (random.randint(0, 2) == 0):
                    play(get_audio_path())
                else:
                    print("test")
                    arduino.write(b"R")
            case _:
                engine.say(text_i)
                engine.runAndWait()
       
# Main function
def main():
    pygame.init()
    pygame.mixer.init()
    print("Connexion a la carte arduino...")
    # Replace with the correct port where the arduino is installed. ex: COM4
    arduino = serial.Serial('COM_OF_THE_ARDUINO', 9600, timeout=1)
    time.sleep(2)
    print("Connexion réalisé !")
    while True:
        record_audio()  # Records the user's voice
        user_text = transcribe_audio()  # Transcribes audio to text
        # possibility to send prompts
        # user_text = input("Ecrivez votre prompte : ")
        print(user_text)

        if user_text.lower() in ["stop", "quitte", "exit"]:
            print("Fin du programme.")
            break
        
        response = generate_response(user_text)  # Send the text to Mistral AI

        speak(response, arduino)  # Make AI talk with pyttsx3

if __name__ == "__main__":
    main()