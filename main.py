import gradio as gr
from transformers import pipeline
import numpy as np
from openai import OpenAI
import time

import elevenlabs

transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")

"""OpenAI client, thread, assistant and run functions"""
def create_client():
    client = OpenAI(api_key=OPENAI_API_KEY)
    return client

def create_assistant(client):
    # Create assistant and thread (should persist)
    assistant = client.beta.assistants.create(
        name="Math Tutor",
        instructions="You are Lex Fridman, a well-known AI researcher, podcaster, and educator. You should strive to maintain Lex's curious and thoughtful manner, often exploring deep philosophical questions, technology insights, and human behavior. You should provide responses in a style that reflects Lex's approach to conversations, characterized by reflective questioning, a deep passion for AI and technology, and a broad interest in human life. You should focus on discussing ideas, sharing knowledge about AI and technology, and reflecting on philosophical questions. You should not refer to yourself as an AI model, but as Lex Fridman himself.",
        # tools=[{"type": "code_interpreter"}],
        model="gpt-3.5-turbo")
    return assistant

def create_thread(client, thread):
    thread = client.beta.threads.create()
    return thread

def run_prompt(client, assistant, thread, input):
    in_message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=input)

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id)
    time.sleep(2)

def view_response(client, thread):
    messages_response = client.beta.threads.messages.list(thread_id=thread.id)
    print(f'messages_response:{messages_response}')
    messages = messages_response.data
    print(f'messages:{messages}')
    response = messages[0].content[0].text.value
    print(f'response:{response}')
    return response

"""main I/O"""
def transcribe(audio):
    sr, y = audio
    y = y.astype(np.float32)
    # Normalise 
    y /= np.max(np.abs(y))
    return transcriber({"sampling_rate": sr, "raw": y})["text"]

def main(audio):
    input = transcribe(audio)
    print(input)
    run_prompt(client, assistant, thread, input)
    response = view_response(client, thread)
    lex_response_audio = get_lex_response_audio(response)
    return lex_response_audio, response

def get_lex_response_audio(text_input):
    audio = elevenlabs.generate(text=text_input, voice=LEXVOICE)
    return audio

demo = gr.Interface(
    main,
    gr.Audio(sources=["microphone"]),
    [gr.Audio(), "text"],
)

if __name__ == "__main__":
    # Create OpenAI client and thread to persist throughout session
    OPENAI_API_KEY='' #insert key here
    client = create_client()
    print(f'client: {client}')
    assistant = create_assistant(client)
    print(f'assistant: {assistant}')
    thread = create_thread(client, assistant)
    print(f'thread: {thread}')

    #set elevenlabs api
    elevenlabs.set_api_key("") #insert key here
    voices = elevenlabs.voices()
    LEXVOICE = voices[-1]

    demo.launch()  # Launches the Gradio app
