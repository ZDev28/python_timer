import os
from time import sleep

def waitSeconds(seconds):
    while seconds > 0:
        seconds -= 1
        print(seconds)
        sleep(1.0)
        try:
            os.system('cls')
        except:
            pass
    print('TIME IS OVER!')

def waitMinutes(minutes):
    while minutes > 0:
        minutes -= 1
        print(minutes)
        sleep(60.0)
        try:
            os.system('cls')
        except:
            pass
    print('TIME IS OVER!')

def waitHours(hours):
    while hours > 0:
        print(hours)
        hours -= 1
        sleep(3600.0)
        try:
            os.system('cls')
        except:
            pass
    print('TIME IS OVER!')

o = input('Choose [S]econds or [M]inutes or [H]ours\n> ')
oss = ['S', 's']
omm = ['M', 'm']
ohh = ['H', 'h']
if o in oss:
    waitSeconds(int(input('Enter seconds\n> ')))
elif o in omm:
    waitMinutes(int(input('Enter minutes\n> ')))
elif o in ohh:
    waitMinutes(int(input('Enter hours\n> ')))
