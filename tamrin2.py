from email.mime import audio
from moviepy  import editor

video = editor.VideoFileClip(r'C:\Users\Nasrin\Desktop\folder\folder_python\assignment7\video.mp4')
audio = video.audio
audio.write_audiofile(r'C:\Users\Nasrin\Desktop\folder\folder_python\assignment7\video.mp3')