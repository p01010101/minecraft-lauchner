
import subprocess
import sys
from json import *
# /Users/antoine/.ssh/id_ed25519

requirements = [
    "pystyle",
    "colorama",
    "requests",
    "beautifulsoup4"
]

def install_dep():
    for dep in requirements:
        try:
            __import__(dep)
        except ImportError:
            subprocess.call([sys.executable, "-m", "pip", "install", dep])

def setup():
    from pystyle import Colors, Write
    
    import pathlib
    install_dep()
    mc_icon = open(pathlib.Path(__file__).absolute().parent.joinpath("assets/minecraft.txt"), "r").read()
    welcome_msg = open(pathlib.Path(__file__).absolute().parent.joinpath("assets/text-welcome.txt"), "r").read()
    print(mc_icon)
    Write.Print(welcome_msg, Colors.green_to_black,  interval=0.001, hide_cursor=True)
    Write.Input("Press enter to install The minecraft laucher...", Colors.green_to_black, end="")
    Write.Print("Installing...", Colors.green_to_black, interval=0.001, hide_cursor=True)

    import time 
    import random
    import platform
    items = list(range(0, 57))
    printProgressBar(0, len(items), prefix = 'Progress:', suffix = 'Complete', length = 50)
    
    for i, item in enumerate(items):
        time.sleep(random.random()/10)
        if i == 28 and platform.system() == "Windows":
            subprocess.call(["mc-setup.exe"])
        else:
            time.sleep(0.3)
        printProgressBar(i + 1, len(items), prefix = 'Progress:', suffix = 'Complete', length = 50)

    Write.Print("Done!\n", Colors.green_to_black, interval=0.001, hide_cursor=True)
    Write.Input("Press enter to continue...", Colors.green_to_black, interval=0.001, hide_cursor=True)
    Write.Print("Starting...", Colors.green_to_black, interval=0.001, hide_cursor=True)
    import os
    os.system("C:\\EasyMC\\dist\\easy_mc.exe")

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

