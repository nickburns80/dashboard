import os  #xNOTE deprecated to 'subprocess' import currently for xterm launch?
import bluetooth._bluetooth as _bt
import subprocess as sp
import tkinter as tk
from tkinter import filedialog,ttk

from data import dashconf

def callback(event):
    print(event.width, event.height)


class StatusBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.place(relx=0,rely=0.95,relwidth=1,relheight=0.05)
#        self.pack(side="bottom", fill="x")
#        bt_cont=_bt.rea
        bt_cont="HCI01"
        wf_cont="ETH01"
        stat_BT=ttk.Label(master=self,
                            text="BT: "+bt_cont+" // WiFi: "+wf_cont).pack()


class ToolBar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.place(relx=0,rely=0,relwidth=1,relheight=0.05)
#        self.pack(side="top", fill="x")


class NavBar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.place(relx=0,rely=0.05,relwidth=0.1,relheight=0.9)
#        self.pack(side="left", fill="y")
'''
        nav_menu=tk.Frame(self).pack(side="top",fill="both")
        text=tk.Text(master=nav_menu).pack(side="right")
        nav_cats=["Bluetooth","Wi-Fi","SW Radio","Other"]
        for cat in nav_cats:
            text.insert("end","%s\n" % cat, "header")
#        nav_txt=tk.text

#        nav_bt=tk.LabelFrame(self,text="Bluetooth").pack(fill="x")
#        nav_menu=tk.Label(nav_bt,text='').pack(side='right')
'''
'''
        nav_list={'nav_bt':'Bluetooth',
                'nav_wifi':'Wi-Fi',
                'nav_sdr':'SW Radio',
                'nav_oth':'Other'
                }
        nav_key=[nav_list.keys()]
        nav_ent=[nav_list.items()]
        for key in nav_ke
            key=

        nav_cats=[nav_bt:"Bluetooth","Wi-Fi","SW Radio","Other"]
        yplace=0
        for cat in nav_cats:
            ttk.Label(self,text=cat).place(anchor="ne",y=yplace)
            yplace+=20
'''
#    def BarMake(ttk.Label):
'''
        nav_bt=ttk.Label(self,text="Bluetooth").place(relx=1,
                                                    y=0,
                                                    anchor="ne")

        nav_wifi=ttk.Label(self,text="WiFi").place(relx=1,
                                                    y=20,
                                                    anchor="ne")
        
        nav_sdr=ttk.Label(self,text="sd Radio").place(relx=1,
                                                    y=40,
                                                    anchor="ne")
        
        nav_oth=ttk.Label(self,text="Other").place(relx=1,
                                                    y=60,
                                                    anchor="ne")
'''
'''
        nav_help=["Help","Settings","Exit"]
        yinvert=-20
        for hlp in nav_help:
            ttk.Label(self,text=hlp).place(anchor="sw",y=yinvert)
            yinvert-=20
'''
'''
#        nav_help=ttk.Label(self,text="Help").pack(side="bottom")
        nav_help=tk.Menubutton(self,text="Help").place(relx=0, anchor="sw")
        nav_set=ttk.Label(self,text="Settings").place(relx=0, anchor="sw")
        nav_exit=ttk.Label(self,text="Exit").place(relx=0, anchor="sw")
'''



class Main(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.place(relx=0.1,rely=0.05,relwidth=0.9,relheight=0.9)
#        self.pack(side="right", fill="both", expand=True)


class MainWindow(tk.Tk):
    ### Creation of Main Window hosting entire application
    def __init__(self, *args, **kwargs):
        # main window initialization
        tk.Tk.__init__(self, *args, **kwargs)
    
        ###
        #  MAIN WINDOW basic layout
        ###
        self.minsize(width=dashconf.mnWIDTH,height=dashconf.mnHEIGHT)
        if dasconf.start
        self.attributes('-zoomed', True)
#        self.attributes('-fullscreen', True)
#        self.master=master
#        window_parts=[StatusBar, ToolBar, NavBar, MainWindow]

#        self.statusbar=tk.Frame(bg="Red")
        self.statusbar=StatusBar(self,bg="Green")
        self.toolbar=ToolBar(self, bg="Red")
        self.navbar=NavBar(self, bg="Blue")
        self.main=Main(self, width=300, height=200, bg="Yellow")

#        self.statusbar.pack(side="bottom", fill="x")
#        self.toolbar.pack(side="top", fill="x")
#        self.navbar.pack(side="left", fill="y")
#        self.main.pack(side="right", fill="both", expand=True)

        ###
        #  STATUSBAR layout
        ###
#        stat_test=ttk.Label(master=self.statusbar,
#                            text="This statusbar").pack()

        ###
        #  MENUBAR layout
        ###

        ###
        #  NAVBAR layout
        ###
#        nav_label=ttk.Label(master=self.navbar, text="Navigation").pack()

        ###
        #  MAIN layout
        ###
#        wid = self.main.winfo_id()
#        os.system('xterm -into %d -geometry 50x80 -sb &' % wid)
#        nav_label=tk.Label(master=self.navbar, text="Navigation").pack()


        ###
        #  EVENT binding
        ###





if __name__ == '__main__':

    root = MainWindow()
    root.title("Tech Dash")
    root.bind
    root.mainloop()




'''
### ### ### ### ###

================    Menu:   Tool listing, settings, about, help, exit xNOTE Potentially redundant
Menubar                         xNOTE: Maybe instead of Menu, tabs of active tools?
----------------    Nav:    Heading, tools  ~~~  help, settings, exit
Nav | Main                  
    |               Main:   Were everything happens
____|___________            
Status__________    Status: BT u/d, Wifi u/d, else???


Nav headings:
Bluetooth, Wifi, SDR, Other (sub listing of tools)
Nav bottom:
Exit, Settings, Help (menu button w/ man pages, notes, about, etc)



'''