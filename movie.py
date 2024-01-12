import os
from moviepy import editor


def save(path=os.getcwd()):
    images = []
    for img in os.listdir(f"{os.getcwd()}\\temp_imgs"):
        images.append(os.getcwd()+"\\temp_imgs\\"+img)
    video = editor.ImageSequenceClip(images, fps=1)
    video.write_videofile(f"{path}\\coded_vdo.avi",
                          verbose=False, preset="veryslow",
                          codec="rawvideo")
