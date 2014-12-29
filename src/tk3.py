#!/usr/bin/env python      1
import Tkinter as tk       #2

class myLabel(tk.Label):
    def __init__(self, strText, intWidth):
        tk.Label.__init__(self, master=Application, text = strText)
        self.the_label = tk.Label(self)
        self.the_label['padx'] = 1
        self.the_label['pady'] = 1
        self.the_label['bg'] = '#667788'
        self.the_label['fg'] = 'white'
        self.the_label['relief'] = 'groove'
        self.the_label['height'] = 1
        self.the_label['width'] = intWidth         
    

class Application(tk.Frame):              #3
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   #4
        self.grid()                       #5
        self.createWidgets()

    def createWidgets(self):
        self.gender_label = myLabel('Gender',15) 
        self.gender_label.grid()
        
        self.gender_value = tk.Label(self, text='Male')
        self.gender_value['padx'] = 1
        self.gender_value['pady'] = 1
        self.gender_value['bg'] = '#667788'
        self.gender_value['fg'] = 'white'
        self.gender_value['relief'] = 'groove'
        self.gender_value['height'] = 1
        self.gender_value['width'] = 15
        self.gender_value.grid()
        
        self.person_name_label = tk.Label(self, text='Person Name')            #6
        self.person_name_label['padx'] = 1
        self.person_name_label['pady'] = 1
        self.person_name_label['bg'] = '#667788'
        self.person_name_label['fg'] = 'white'
        self.person_name_label['relief'] = 'groove'
        self.person_name_label['height'] = 1
        self.person_name_label['width'] = 80
        self.person_name_label.grid

        self.person_name_label.grid()            #7
        self.person_name_value = tk.Label(self, text='William Kelly STUART')            #6
        self.person_name_value['padx'] = 1
        self.person_name_value['pady'] = 1
        self.person_name_value['bg'] = '#667788'
        self.person_name_value['fg'] = 'white'
        self.person_name_value['relief'] = 'groove'
        self.person_name_value['height'] = 1
        self.person_name_value['width'] = 80
        self.person_name_value.grid()            #7
        
        
app = Application()                       #8
app.master.title('Sample application')   # 9
app.mainloop()       