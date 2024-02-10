from board import get_x, get_y

def punkte_x():
    xl = get_x()["xol"] + get_x()["xml"] + get_x()["xul"]
    xm = get_x()["xom"] + get_x()["xmm"] + get_x()["xum"]
    xr = get_x()["xor"] + get_x()["xmr"] + get_x()["xur"]

    return xl + xm + xr

def punkte_y():
    yl = get_y()["yol"] + get_y()["yml"] + get_y()["yul"]
    ym = get_y()["yom"] + get_y()["ymm"] + get_y()["yum"]
    yr = get_y()["yor"] + get_y()["ymr"] + get_y()["yur"]

    return yl + ym + yr

def x_lmr():
    xl = get_x()["xol"] + get_x()["xml"] + get_x()["xul"]
    xm = get_x()["xom"] + get_x()["xmm"] + get_x()["xum"]
    xr = get_x()["xor"] + get_x()["xmr"] + get_x()["xur"]

    return (xl, xm, xr)

def y_lmr():
    yl = get_y()["yol"] + get_y()["yml"] + get_y()["yul"]
    ym = get_y()["yom"] + get_y()["ymm"] + get_y()["yum"]
    yr = get_y()["yor"] + get_y()["ymr"] + get_y()["yur"]

    return (yl, ym, yr)