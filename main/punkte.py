import board

def punkte_x():
    xl = x["xol"] + x["xml"] + x["xul"]
    xm = x["xom"] + x["xmm"] + x["xum"]
    xr = x["xor"] + x["xmr"] + x["xur"]

    return xl + xm + xr

def punkte_y():
    yl = y["yol"] + y["yml"] + y["yul"]
    ym = y["yom"] + y["ymm"] + y["yum"]
    yr = y["yor"] + y["ymr"] + y["yur"]

    return yl + ym + yr

def x_lmr():
    xl = x["xol"] + x["xml"] + x)["xul"]
    xm = x["xom"] + x["xmm"] + x["xum"]
    xr = x["xor"] + x["xmr"] + x["xur"]

    return (xl, xm, xr)

def y_lmr():
    yl = y["yol"] + y["yml"] + y["yul"]
    ym = y["yom"] + y["ymm"] + y["yum"]
    yr = y["yor"] + y["ymr"] + y["yur"]

    return (yl, ym, yr)
