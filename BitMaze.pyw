import os
import tkinter
from tkinter import ttk
import decoder
import encoder


class Screen:
    def __init__(self):
        self.frame = tkinter.Tk()
        self.frame.title("Bit Maze")
        self.frame.geometry("250x200")
        self.frame.iconbitmap(f"{os.getcwd()}\\bitmaze.ico")
        self.frame.grid()
        self.arg1 = None
        self.arg2 = None
        self.arg3 = None
        self.options = ["encode", "decode", "encode"]
        self.option = tkinter.StringVar(self.frame)
        self.option.set(self.options[0])
        self.labels = []
        self.visibility = tkinter.StringVar(self.frame)
        self.visibility.set("disabled")
        for i in range(7):
            self.labels.append(tkinter.StringVar(self.frame))
        self.labels[0].set("Comprimento:")
        self.labels[1].set("Altura:")

    def main(self):
        ttk.Button(self.frame, text="START", command=self.init).grid(column=4, row=10)
        ttk.OptionMenu(self.frame, self.option, *self.options, command=self.start).grid(column=3, row=0)

    def start(self, opt):
        if self.option.get() == "encode":
            self.visibility.set("normal")
            self.labels[0].set("Largura")
            self.labels[0].set("Largura:")
            self.labels[1].set("Altura")
        elif self.option.get() == "decode":
            self.visibility.set("disabled")
            self.labels[0].set("Output extension:")
            self.labels[1].set("")

    def init(self):
        if self.option.get() == "encode":
            encoder.Encoder(str(self.arg1.get()), str(self.arg2.get()), str(self.arg3.get()))
        elif self.option.get() == "decode":
            decoder.Main(str(self.arg1.get()), str(self.arg2.get()))

    def instantiate(self):
        ttk.Label(self.frame, text="Input file path:").grid(column=4, row=2)
        self.arg1 = ttk.Entry()
        self.arg1.grid(column=4, row=3)
        ttk.Label(self.frame, textvariable=self.labels[0]).grid(column=4, row=4)
        self.arg2 = ttk.Entry()
        self.arg2.grid(column=4, row=5)
        ttk.Label(self.frame, textvariable=self.labels[1]).grid(column=4, row=6)
        self.arg3 = ttk.Entry()
        self.arg3.grid(column=4, row=7)


if __name__ == "__main__":
    screen = Screen()
    screen.instantiate()
    screen.main()
    screen.frame.mainloop()
