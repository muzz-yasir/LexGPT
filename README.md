# @ENCODEHACK JUDGES
If trying out, use the API keys provided in our submission!

# Description

Lexperience is a first-of-a-kind, end-to-end clone of the AI researcher and podcast host, Lex Fridman. 


Our clone presents a new paradigm of media consumption in the AI era, as an alternative to passive listening of information dense media; imagine if you could pause a podcast in real-time and query the podcast host about a particular topic? We have taken a step towards this goal by creating a platform to naturally interact with our favourite podcast host in a surprisingly stimulating manner.


We have implemented the most crucial components of engaging human-like interaction: listening, thinking, speaking and eye-contact. Users interact via speech and we leverage ElevenLabs and OpenAI Assistants API's to generate a realistic Lex Fridman-like response in audio. From here we integrate SOTA research in Computer Vision, by utilising [DreamTalk (Ma et al, 2023)](https://dreamtalk-project.github.io/): a diffusion based model to generate incredibly realistic talking head animation, driven by our Lex audio response, for the output.


# Limitation

Lack of compute means that our model takes almost a minute to respond on average, but the output is certainly worth it.

# Setup
- `pip install gradio openai replicate elevenlabs`
- install transformers from [huggingface](https://huggingface.co/docs/transformers/en/installation)
- input API keys for ElevenLabs, OpenAI and Replicate 
- run `gradio main.py`

# Usage
Lexperience uses a gradio interface to facilitate interaction with the Lex companion. To use the gradio interface, run `gradio main.py` in the command line, then connect to the the localhost it specifies through a browser. By default, this is likely to be http://127.0.0.1:7860/.

# Demo 


## Raw output 
'Hey Lex, what's your favourite podcast episode and with whom?'


https://github.com/muzz-yasir/Lexperience/assets/56521243/ffc11e05-cae7-4f02-8490-2120971c6157

