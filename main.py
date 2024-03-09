import gradio as gr
from transformers import pipeline
import numpy as np
from openai import OpenAI
import time
import os
import replicate
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
    message= False
    response = None
    
    while not message:
        messages_response = client.beta.threads.messages.list(thread_id=thread.id)
        print(f'messages_response:{messages_response}')
        print(message.role for message in messages_response.data)
        message_count = len([message for message in messages_response.data if message.role == 'user'])
        gpt_messages = [message for message in messages_response.data if message.role != 'user']

        print(f'messages:{gpt_messages}')
        if len(gpt_messages) == message_count:
            try:
                response = gpt_messages[0].content[0].text.value
                message = True
            except:
                time.sleep(1)

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
    with open("response.mp3",'wb') as f:
        f.write(lex_response_audio)
    lex_response_video = get_lex_response_video(lex_response_audio)
    return lex_response_audio, response, lex_response_video

def get_lex_response_audio(text_input):
    audio = elevenlabs.generate(text=text_input, voice=LEXVOICE)
    return audio

def get_lex_response_video(audio):
    image= open('podcastcover.jpg', "rb")
    audio= open('response.mp3', "rb")
    output = replicate.run(
    "cjwbw/dreamtalk:c52a2bad8c0bdf9645609de071dddb1ddab0b396b8bf7096027819473a85b4ca",
    input={
        "pose": "data/pose/RichardShelby_front_neutral_level1_001.mat",
        "audio": audio,
        "image": image,
        "crop_image": True,
        "style_clip": "data/style_clip/3DMM/M030_front_neutral_level1_001.mat",
        "max_gen_len": 1000,
        "num_inference_steps": 10
    }
    )
    return output

demo = gr.Interface(
    main,
    gr.Audio(sources=["microphone"]),
    [gr.Audio(), "text", gr.Video()],
    live=True
)

if __name__ == "__main__":
    OPENAI_API_KEY='' 
    REPLICATE_API_TOKEN=''
    os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN
    # Create OpenAI client and thread to persist throughout session
    client = create_client()
    print(f'client: {client}')
    assistant = create_assistant(client)
    print(f'assistant: {assistant}')
    thread = create_thread(client, assistant)
    print(f'thread: {thread}')

    elevenlabs.set_api_key("") #insert key here
    voices = elevenlabs.voices()
    LEXVOICE = voices[-1]

    demo.launch()  # Launches the Gradio app
