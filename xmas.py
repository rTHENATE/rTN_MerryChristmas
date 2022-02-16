import termcolor
import random
import time
import datetime
import sys
import os
from colorama import init
from termcolor import colored


def clear():
    if sys.platform == 'win32':   # window
        return os.system('cls')
    else:
        return os.system('clear')


colors = [                       # color light
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white']

yellowlight = termcolor.colored('r', 'yellow')
magentalight = termcolor.colored('T', 'red')
cyanlight = termcolor.colored('N', 'cyan')


lightlist = [yellowlight, cyanlight, magentalight]

init()
while True:
    print('edit code rTHENET')
    for i in range(1, 30, 2):                # tree
        tree = ''
        for j in range(i):                   # lights random
            randNum = random.randint(0, 500)
            if (randNum <= 750) and (randNum >= 250):
                tree += lightlist[random.randint(0, 2)]
            else:
                tree += termcolor.colored('*', 'green')
        string = '_'*(15-int(i/2))+tree+'_'*(15-int(i/2))+'\n'
        print(string, end='')
    trunk = colored('rTHENET', 'red')
    for k in range(3):
        outbuffer = '_'*12+trunk+'_'*12+'\n'

        print(outbuffer, end='')
        merry_Christmas = termcolor.colored(
            'Merry Christmas', colors[random.randint(0, len(colors)-1)])
    outbuffer2 = '.'*8+merry_Christmas+'.'*8+'\n'
    print(outbuffer2, end='')

    time.sleep(0.3)
    clear()
