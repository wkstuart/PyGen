from Tkinter import *
from personClass import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.closebutton = Button(self)
        self.closebutton["text"] = "Close"
        self.closebutton["fg"]   = "black"
        self.closebutton["command"] =  self.closebutton

        self.closebutton.pack({"side": "left"})
        
        self.personSurnameTextbox = Entry(self)
        self.personSurnameTextbox["text"] = 'STUART, William Kelly (b 1947)'
        self.personSurnameTextbox["bg"] = 'black'
        self.personSurnameTextbox["fg"] = 'white'
 
        self.personSurnameTextbox.pack({"side":"left"})
        
class labelFieldGrp(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack({"side":"left"})
        self.createWidgets()
        
    def createWidgets(self):
        self.the_label = Label(self)
        self.the_label['text'] = 'Surname'
        self.the_label['bg'] = '#667788'
        self.the_label['fg'] = 'white'
        self.the_label['relief'] = 'ridge'
        self.the_label.pack({"side":"top"})
        
        self.the_content = Label(self)
        self.the_content['text'] = "STUART"
        self.the_content['bg'] = '#667788'
        self.the_content['fg'] = 'white'
        self.the_content['relief'] = 'ridge'
        self.the_content.pack({"side":"bottom"})
        
