from moviepy.editor import *


def get_file_paths(folder_path):
    file_name_list = os.listdir(folder_path)

    path_name_list = []
    final_name_list = []
    for name in file_name_list:
        if name == ".DS_Store":
            pass
        else:
            path_name_list.append(folder_path + "/"+ name)
    return path_name_list

listOfVideos = get_file_paths("/Users/v_yumatthew/frankenstein/files")

print(listOfVideos)

