import tkinter as tk
import time

from data import dashconf


folderLOG="./logs/"

BLUETL=("Bluelog","Blueranger","RedFang")
WIFITL=("Wifite",)
SDRTL=("unk",)
OTHTL=("und",)


def tool_BLUELOG():

    iFace=dashconf.indHCI[0][0]
    adDrs=dashconf.indHCI[0][1]
    now="bluelog_"+time.strftime("%H%M_%d%b%Y")+".log"

    command="bluelog -i "+iFace+" -o "+folderLOG+now

    print(command)
    return command

tool_BLUELOG()