import requests
from elevenlabs import clone, generate, play

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/2EiwWnXFnvU5JabPnv8n"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "8b937b9e5eccf5758db8ef7444d115b5"
}


def text_to_lex(text_input):
    print("text_to_lex called")
    data = {
        "text": text_input,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
        }   
    }
    
    response = requests.post(url, json=data, headers=headers)
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

def main():
    print("main called")
    text = "hello mustafa"
    print(text)
    text_to_lex(text)

if __name__ == "__main__":
    print("script run")
    main()