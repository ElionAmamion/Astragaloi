from würfel import *
from board import *

def ki():

    erg = w6()
    leg = w3()

    if leg == "l" or leg == "L":
        if x["xol"] == 0:
            x["xol"] = erg
        elif x["xml"] == 0:
            x["xml"] = erg
        elif x["xul"] == 0:
            x["xul"] = erg

    elif leg == "m" or leg == "M":
        if x["xom"] == 0:
            x["xom"] = erg
        elif x["xmm"] == 0:
            x["xmm"] = erg
        elif x["xum"] == 0:
            x["xum"] = erg

    elif leg == "r" or leg == "R":
        if x["xor"] == 0:
            x["xor"] = erg
        elif x["xmr"] == 0:
            x["xmr"] = erg
        elif x["xur"] == 0:
            x["xur"] = erg