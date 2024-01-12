import sys
import cv2
import os
import shutil
from PIL import Image


class Main:
    def __init__(self, video, ext):
        self.ext = ext
        self.path = f"{os.getcwd()}\\temp_frames"
        self.video = cv2.VideoCapture(video)
        self.admiss_value = 255
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.save(self.bin2bytes(self.dec()))

    def dec(self):
        byte = ""
        # get frames of the video:
        duration = self.video.get(cv2.CAP_PROP_FRAME_COUNT)
        for idx in range(int(duration)):
            self.video.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = self.video.read()
            cv2.imwrite(f"{self.path}\\frame_{idx}.png", frame)
        # interpret then:
        for frme in os.listdir(self.path):
            img = Image.open(f"{self.path}\\{frme}")
            pix = img.load()
            num = 0
            for y in range(img.size[1]):
                for x in range(img.size[0]):
                    if pix[x, y][0] == self.admiss_value:
                        byte += "1"
                    elif pix[x, y][2] == self.admiss_value:
                        byte += "0"
                    else:
                        break
        return byte

    def save(self, byte):
        with open(f"decoded.{self.ext}", "wb") as file:
            for i in byte:
                file.write(i.to_bytes(1, "big"))
        shutil.rmtree(self.path)

    @staticmethod
    def bin2bytes(byte_s):
        act_bit = -2
        b_list = []
        for byte in range(8, len(byte_s)+8, 8):
            b_list.append(int(byte_s[act_bit+2:byte], 2))
            act_bit += 8
        return b_list
