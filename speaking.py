import requests
from elevenlabs import clone, generate, play
import elevenlabs
elevenlabs.set_api_key("8b937b9e5eccf5758db8ef7444d115b5")
voices = elevenlabs.voices()
lexvoice = voices[-1]

def text_to_lex(text_input):
    print("text_to_lex called")
    
    audio = generate(text=text_input, voice=lexvoice)
    return(audio)
    

def main():
    print("main called")
    text = "hello mustafa"
    print(text)
    audio = text_to_lex(text)
    play(audio)

if __name__ == "__main__":
    print("script run")
    main()