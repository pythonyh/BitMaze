def open_file(path):
    with open(path, "r+b") as file:
        binary = ""
        for char in file.read():
            num = ""
            for i in range(9-len(str(bin(char)))):
                num += "0"
            binary += bin(char).replace("b", num)
        return binary
