from Tkinter import Tk
from WCK import Widget

class MyTextWidget(Widget):

    ui_option_text = ""
    ui_option_font = "times"
    ui_option_color = "black"

    ui_option_width = 100
    ui_option_height = 100

    def ui_handle_config(self):
        self.font = self.ui_font(self.ui_option_color, self.ui_option_font)
        return int(self.ui_option_width), int(self.ui_option_height)

    def ui_handle_repair(self, draw, x0, y0, x1, y1):
        draw.text((0, 0), self.ui_option_text, self.font)

root = Tk()

widget = MyTextWidget(root, text="hello!", width=200)
widget.pack()

root.mainloop()