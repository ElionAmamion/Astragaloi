from os import system
from würfel import *
from board import *

def spieler():
    try:
        erg = w6()
        print(erg)

        print("Wo willst du den Würfel platzieren?")
        leg = input()
        if leg == "l" or leg == "L":
            if y["yol"] == 0:
              y["yol"] = erg
            elif y["yml"] == 0:
                y["yml"] = erg
            elif y["yul"] == 0:
                y["yul"] = erg

        elif leg == "m" or leg == "M":
            if y["yom"] == 0:
                y["yom"] = erg
            elif y["ymm"] == 0:
                y["ymm"] = erg
            elif y["yum"] == 0:
                y["yum"] = erg

        elif leg == "r" or leg == "R":
            if y["yor"] == 0:
                y["yor"] = erg
            elif y["ymr"] == 0:
                y["ymr"] = erg
            elif y["yur"] == 0:
                y["yur"] = erg

        elif leg == "x" or leg == "X":
            running = False
    except:
        print("Bitte probier es nochmal.")