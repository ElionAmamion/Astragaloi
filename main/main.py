from os import system
from ki import *
from spieler import *

running = True

while running:
    system("cls")
    board()
    print("")
    spieler()
    board()
    ki()