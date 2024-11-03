import gradio as gr
import speech_recognition as sr
import keyboard
import threading

stop_listening = False

def listen_for_key():
    global stop_listening
    while True:
        if keyboard.is_pressed('q'):
            stop_listening = True
            break

def recognize_kannada_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="kn-IN")
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError as e:
        return f"Error: {e}"

# Gradio interface for speech recognition
gr_speech_rec = gr.Interface(fn=recognize_kannada_speech, inputs=None, outputs="text", title="Kannada Speech Recognition")
