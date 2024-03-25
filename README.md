# @ENCODEHACK JUDGES
If trying out, ping me for the API keys!

# Motivation

Our generation is plagued by passive over-consumption of media. We need new ways to engage in media that uplift us and provide fulfilling interaction with content creators. Lexperience is a first-of-a-kind, end-to-end simulation of the AI researcher and podcast host, Lex Fridman. 

Our project presents a new paradigm of media consumption in the AI era, as an alternative to passive consumption of information dense media; imagine if you could pause a podcast in real-time and query the podcast host about a particular topic? We have taken a step towards this goal by creating a platform to naturally interact with our favourite podcast host in a surprisingly stimulating manner.

# Architecture 

We have implemented the most crucial components of stimulating human-like interaction: listening, thinking, speaking and visualising. Users interact with Lexperience via speech and we leverage Whisper, ElevenLabs and OpenAI Assistants API's to generate a realistic Lex Fridman-like response in audio. From here we integrate SOTA research in Computer Vision, by utilising [DreamTalk (Ma et al, 2023)](https://dreamtalk-project.github.io/): a diffusion based model to generate incredibly realistic talking head animation, driven by our Lex audio response, for the output.

The interaction takes place in Gradio, a GUI for building quick ML prototypes and requires users to press record to chat with Lex, wait for the response and press play on the resulting video. As discussed below, we have much more to say about inference times, but with that aside - extending this to real-time interaction simply requires: a few tweaks in Gradio, appropriate chunking of audio input and pipeline execution and some engaging sample videos to be played whilst the inference takes place.

![LEXPERIENCE ARCHITECTURE](https://github.com/muzz-yasir/Lexperience/assets/56521243/5aa3954d-4fec-48a3-a7bc-f6985b215319)

## Inference

Important caveat: our model takes almost a minute to respond on average, *but the output is certainly worth it*. Given that the project was thrown together over the course of 2 days, **there is huge room for improvement that can be achieved from both non trivial and trivial changes to the architecture and execution**.

- Primarily, apart from API usage, no specialised hardware or compute was explicitly used to improve inference times as we didn't want to throw any money at a prototype. However we expect that, running each of the utilised models (Whisper STT, ElevenLabs TTS, GPT-3.5, DreamTalk) on a dedicated GPU + dedicating some GPU hours to fine-tuning the DreamTalk model on our **fixed** visual and audio input could drastically reduce this.

- Secondly, creating a more tightly integrated architecture that combines the different components of our system into an end-to-end model, fine-tuned and slimmed down precisely for our use case could expect to bring huge efficiency gains. For example, the video synthesis model used, DreamTalk, is designed for One-Shot generalisation to any face and audio input. This highly impressive ability requires significant computation and multiple components of the model could be dropped when the given visual input is fixed.

Supporting this idea is the observation that for a number of similar tools, real-time or near-real-time inference / execution already exists, think; real-time translation, near-real-time conversational chatbots, real-time 3D animation and real-time faceswap/deepfakes. The jump to real-time lifelike digital assistants is non-trivial but we the progress of this project over 48 hours certainly provides hope for such an end goal.

# Setup
- `pip install gradio openai replicate elevenlabs`
- install transformers from [huggingface](https://huggingface.co/docs/transformers/en/installation)
- input API keys for ElevenLabs, OpenAI and Replicate 
- run `gradio main.py`

# Usage
Lexperience uses a gradio interface to facilitate interaction with the Lex companion. To use the gradio interface, run `gradio main.py` in the command line, then connect to the the localhost it specifies through a browser. By default, this is likely to be http://127.0.0.1:7860/.

# Demo's
See our loom video!!
https://www.loom.com/share/a3c1fc520ef94f7b9ec0ab35f4262808?sid=4f77125d-ea94-40a8-ada6-f0b6ccc5b500

## Lex and Lex talking waffle to each other
Here's a pretty good demo of what our project can do. We made Lex have a conversation with himself: https://www.youtube.com/watch?v=ef6W1FfiD7w

## Raw output 
- *Hey Lex, what's your favourite podcast episode and with whom?*

https://github.com/muzz-yasir/Lexperience/assets/56521243/ffc11e05-cae7-4f02-8490-2120971c6157

# Ethical Disclaimer
We do not have permission to clone Lex in this way and we understand the heavy ethical and legal implications this carries. As a rapid prototype, we will make this repository private shortly after submission and think through the various ways we can provide credit and respect to the original creators.

# References

@article{ma2023dreamtalk,
title={DreamTalk: When Expressive Talking Head Generation Meets Diffusion Probabilistic Models},
author={Ma, Yifeng and Zhang, Shiwei and Wang, Jiayu and Wang, Xiang and Zhang, Yingya and Deng, Zhidong},
journal={arXiv preprint arXiv:2312.09767},
year={2023}
}
