import gradio as gr
from transformers import pipeline
import numpy as np

transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")

def transcribe(audio):
    sr, y = audio
    y = y.astype(np.float32)
    # Normalise 
    y /= np.max(np.abs(y))
    return transcriber({"sampling_rate": sr, "raw": y})["text"]

def prompt(audio):
    text = transcribe(audio)
    return text+'testing____'

demo = gr.Interface(
    prompt,
    gr.Audio(sources=["microphone"]),
    "text",
)

demo.launch()
