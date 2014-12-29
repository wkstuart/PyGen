from Tkinter import *
from ttk import *


root = Tk()
mainframe = Frame(root)

style = Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = Label(text="Test", style="BW.TLabel")
l2 = Label(text="Test", style="BW.TLabel")

root.mainloop()