import os
import time

def loading_bar(seconds):
    for loading in range(0, seconds+1):
        percent = (loading * 100) // seconds
        print("\n")
        print("Loading...")
        print("<" + ("-" * loading) + ("" * (seconds + loading)) +
              ">" + str(percent) + "%")
        print("\n")
        time.sleep(.3)
        clr()


def loading_screen(seconds):
    print("loading screen...")
    with open('lara.txt','r') as screen:
        for lines in screen:
            print(lines,end='')
            time.sleep(seconds)


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

loading_bar(10)
clr()
loading_screen(.1)