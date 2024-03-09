# Description

Lexperience is a first-of-a-kind, end-to-end clone of the AI researcher and podcast host, Lex Fridman. 
Our clone presents a new paradigm of media consumption in the AI era, as an alternative to passive listening of information dense media; imagine if you could pause a podcast in real-time and query the podcast host about a particular topic? We have taken a step towards this goal by creating a platform to naturally interact with our favourite podcast host in a surprisingly stimulating manner.
We have implemented the most crucial components of engaging human-like interaction: listening, thinking, speaking and visualisation. Users interact via speech and we levarage ElevenLabs and OpenAI Assistants API's to generate a realistic Lex-Fridman like response in audio. From here we integrate SOTA research in Computer Vision, by utilising DreamTalk (Ma et al, 2023): a diffusion based model to generate incredibly realistic talking head animation, driven by our Lex audio response, for the output.


# Limitation

Lack of compute means that our model takes almost a minute to respond on average, but the output is certainly worth it.

# Setup
- `pip install gradio openai replicate elevenlabs`
- install transformers from [huggingface](https://huggingface.co/docs/transformers/en/installation)
- input API keys for ElevenLabs, OpenAI and Replicate 
- run `gradio main.py`

# Demo 

