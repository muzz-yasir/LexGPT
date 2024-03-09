import moviepy.editor as mpe
my_clip = mpe.VideoFileClip("response.mp4")
audio_background = mpe.AudioFileClip("audio.wav")
final_clip = my_clip.set_audio(audio_background)
final_clip.write_videofile("response.mp4",fps=25)