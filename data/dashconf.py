import bluetooth as bti
import os
import tkinter as tk

#indHCI=[("hci0":"88:53:2E:F2:5B:79")]  #xNOTE Work tablet info
indHCI=[("hci0","88:78:73:51:47:07")]  #xNOTE Personal laptop info
#ifcWIFI=[("wlp1s0","88:53:2E:F2:5B:75")]  #xNOTE Work tablet info
indWL=[("wlo1","88:78:73:51:47:03")]  #xNOTE Personal laptop info

fontLARGE=("Roboto",14)
fontSMALL=("Droid Sans",10)

startZOOM = False
mnWIDTH = 800
mnHEIGHT = 600

