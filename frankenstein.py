from moviepy.editor import *
import random

def get_file_paths(folder_path):
    file_name_list = os.listdir(folder_path)

    path_name_list = []
    for name in file_name_list:
        if name == ".DS_Store": 
            pass
        else:
            path_name_list.append(folder_path + "/"+ name)
    return path_name_list

listOfVideoPaths = get_file_paths("./files")
unattachedVideos = []

for x in listOfVideoPaths: 
    myClip = VideoFileClip(x)
    for y in range(0, int(myClip.duration)-3, 3): 
        unattachedVideos.append(myClip.subclip(y, y+3))

random.shuffle(unattachedVideos)

finalVideo = concatenate_videoclips(unattachedVideos[:43])
audio = AudioFileClip("music.m4a")
shortAudio = audio.set_duration(finalVideo.duration)
finalVideo = finalVideo.set_audio(shortAudio)
finalVideo.write_videofile("export.avi",fps=24,codec='libx264')