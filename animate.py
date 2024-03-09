api_key = ""

import os
import requests
import json
import moviepy.editor as mpe

files = [
    ("input_face", open("lex_image.png", "rb")),
    ("input_audio", open("audio.wav", "rb")),
]
payload = {}
response = requests.post(
    "https://api.gooey.ai/v2/Lipsync/form/",
    headers={
        "Authorization": "Bearer " + api_key,
    },
    files=files,
    data={"json": json.dumps(payload)},
)
assert response.ok, response.content

result = response.json()
vid = requests.get(result["output"]["output_video"], allow_redirects=True).content
print(response.status_code, result)

open('response.mp4','wb').write(vid)
