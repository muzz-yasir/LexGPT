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
    input = transcribe(audio)
    lex_response = get_lex_response(input)
    lex_response_audio = get_lex_response_audio(lex_response)



    return input


def get_lex_response(input):
    """Call Lex Fridman GPT API"""



def get_lex_response_audio(input):
    """Get Lex Audio transcription"""



demo = gr.Interface(
    prompt,
    gr.Audio(sources=["microphone"]),
    "text",
)

demo.launch()
