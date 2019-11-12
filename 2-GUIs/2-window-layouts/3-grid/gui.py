from tkinter import *

class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()

     # set window attributes
        self.title("Newsletter")
        self.configure(bg="gray69", height=230, width=500)

        self.add_border()
        
        self.add_border_marker_BL

        self.add_border_marker_BR

        self.add_border_marker_TL

        self.add_border_marker_TR

        self.add_heading_label()

        self.add_instruction_label()

        self.add_box_label()

        self.add_text_field()

        self.add_button()




    def add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.grid(row=1, column=1, columnspan=2)

        #style
        self.heading_label.configure(font="Arial 24", text="RECEIVE OUR NEWSLETTER")

    def add_instruction_label(self):
        # create
        self.instruction_label = Label()
        self.instruction_label.grid(row=2, column=1, columnspan=2)

        # style
        self.instruction_label.configure(font="Arial 12", text="Please enter your email below to receive our newsletter.")
    
    def add_box_label(self):
        # create
        self.box_label = Label()
        self.box_label.grid(row=3, column=1)

        # style
        self.box_label.configure(font="Arial 12", text="Email: ")
    
    def add_text_field(self):
        # create
        self.text_field = Entry()
        self.text_field.grid(row=3, column=2)

        # style
        self.text_field.configure(font="Arial 12", bg="Snow", bd="3", width=35)

    def add_button(self):
        #create
        self.button = Button()
        self.button.grid(row=4, column=1, columnspan=2)

        #style
        self.button.configure(font="Arial 12", bg="LightPink1", width=42, text="Subscribe")

    def add_border(self):
        #create
        self.border = Canvas()
        self.border.grid(row=1, rowspan=4, column=1, columnspan=2)

        #style
        self.border.configure(bg="gray92", bd=10, height=190, width=460)
    
    def add_border_marker_TL(self):
        self.border_marker_TL = Label()
        self.border_marker_TL.grid(row=0, column=0)
        self.border_marker_TL.configure(font="Arial 12", text="1")

    def add_border_marker_TR(self):
        self.border_marker_TR = Label()
        self.border_marker_TR.grid(row=0, column=3)
        self.border_marker_TR.configure(font="Arial 12", text="2")    

    def add_border_marker_BL(self):
        self.border_marker_BL = Label()
        self.border_marker_BL.grid(row=5, column=0)
        self.border_marker_BL.configure(font="Arial 12", text="3")

    def add_border_marker_BR(self):
        self.border_marker_BR = Label()
        self.border_marker_BR.grid(row=5, column=3)
        self.border_marker_BR.configure(font="Arial 12", text="4")


# handle events
# (callback functions to handle events will go here)