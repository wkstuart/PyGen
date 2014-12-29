import os, sys
lib_path = os.path.abspath('D:\\KestrelDrive\\KestrelShare\\PythonCode\\Genealogy\\classes')
sys.path.append(lib_path)
lib_path = os.path.abspath('D:\\KestrelDrive\\KestrelShare\\PythonCode\\Genealogy\\modules')
sys.path.append(lib_path)
from Tkinter import *
import os, sys
lib_path = os.path.abspath('D:\\KestrelDrive\\KestrelShare\\PythonCode\\Genealogy\\classes')
sys.path.append(lib_path)
lib_path = os.path.abspath('D:\\KestrelDrive\\KestrelShare\\PythonCode\\Genealogy\\modules')
sys.path.append(lib_path)

from Tkinter import *
from ttk import *
from personClass import *
   
root = Tk()

the_person = person(1)

personframe = Frame(root, padding="3 3 12 12")
personframe.grid(column=0, row=0, sticky=(N, W, E, S))
personframe.columnconfigure(0, weight=1)
personframe.rowconfigure(0, weight=1)

style = Style()
style.configure("myLabel.TLabel", foreground="white", background="#667788", justify="center", relief="raised", font="Tahoma 8")
style.configure("myValue.TLabel", foreground="white", background="black", justify="center", relief="raised", font="Tahoma 8", padx=1, pady=1)

Label(personframe, text="Gender", width=8, style="myLabel.TLabel").grid(column=1, row=1, sticky=W)
Label(personframe, text="Person Name", width=64, style="myLabel.TLabel").grid(column=2, row=1, sticky=W)
Label(personframe, text="Born", width=8, style="myLabel.TLabel").grid(column=3, row=1, sticky=W)
Label(personframe, text="Died", width=8, style="myLabel.TLabel").grid(column=4, row=1, sticky=W)


Label(personframe, text= the_person.Characteristic('Gender'), width=8, style="myValue.TLabel").grid(column=1, row=2, sticky=W)
Label(personframe, text= the_person.FormattedName('gL'), width=64, style="myValue.TLabel").grid(column=2, row=2, sticky=W)
Label(personframe, text= the_person.Characteristic('BirthYear'), width=8, style="myValue.TLabel").grid(column=3, row=2, sticky=W)
Label(personframe, text= the_person.Characteristic('DeathYear'), width=8, style="myValue.TLabel").grid(column=4, row=2, sticky=W)

#for child in personframe.winfo_children(): child.grid_configure(padx=5, pady=5)




root.mainloop()