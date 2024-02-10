from punkte import *

y = {"yol": 0, "yom": 0, "yor": 0,
     "yml": 0, "ymm": 0, "ymr": 0,
     "yul": 0, "yum": 0, "yur": 0}

x = {"xol": 0, "xom": 0, "xor": 0,
     "xml": 0, "xmm": 0, "xmr": 0,
     "xul": 0, "xum": 0, "xur": 0}

def get_x():
    return x

def get_y():
    return y

def board():
    print(x["xul"], "|", x["xum"], "|", x["xur"])
    print("----------")
    print(x["xml"], "|", x["xmm"], "|", x["xmr"])
    print("----------")
    print(x["xol"], "|", x["xom"], "|", x["xor"])
    print(x_lmr())
    print("\n")
    print(y_lmr())
    print(y["yol"], "|", y["yom"], "|", y["yor"])
    print("----------")
    print(y["yml"], "|", y["ymm"], "|", y["ymr"])
    print("----------")
    print(y["yul"], "|", y["yum"], "|", y["yur"])
    print("\n")
    print("Gegner: ", punkte_x(),
          "Du: ", punkte_y())