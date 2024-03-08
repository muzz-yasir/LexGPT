from elevenlabs import clone, generate, play

voice = clone(
    api_key="8b937b9e5eccf5758db8ef7444d115b5",
    name="Alex",
    description="An old American male voice with a slight hoarseness in his throat. Perfect for news", # Optional
    files=["./sample_0.mp3", "./sample_1.mp3", "./sample_2.mp3"],
)

audio = generate(text="Hi! I'm a cloned voice!", voice=voice)

play(audio)