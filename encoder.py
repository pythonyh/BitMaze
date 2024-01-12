import reader
import movie
from PIL import Image
from PIL import ImageDraw
import sys
import shutil
import os


class Encoder:
    def __init__(self, arg1, arg2, arg3):
        self.res = [int(arg2), int(arg3)]
        self.frame = Image.new("RGB", (self.res[0], self.res[1]), (0, 0, 0))
        self.draw_frame = ImageDraw.Draw(self.frame)
        self.clr = {"0": (255, 0, 0), "1": (0, 0, 255)}
        self.file_size = os.stat(arg1).st_size*8
        self.encode(reader.open_file(arg1))

    def encode(self, bts):
        if not os.path.exists(f"{os.getcwd()}\\temp_imgs"):
            os.mkdir(f"{os.getcwd()}\\temp_imgs")
        x = 0
        y = 0
        img_idx = 0
        for bit in bts:
            self.draw_frame.point([x, y], self.clr[bit])
            x += 1
            if x+y == self.res[0]+self.res[1]:
                self.frame.save(f"{os.getcwd()}\\temp_imgs\\img_{img_idx+1}.png", "PNG")
                self.draw_frame.rectangle((0, 0, self.res[0], self.res[1]), 0)
                img_idx += 1
                x = 0
                y = 0
            elif x >= self.res[0]:
                y += 1
                x = 0
        self.frame.save(f"{os.getcwd()}\\temp_imgs\\img_{img_idx+1}.png", "PNG")
        os.system("cls")
        movie.save()
        shutil.rmtree(f"{os.getcwd()}\\temp_imgs")
