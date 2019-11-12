from tkinter import *

class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()

     # set window attributes
        self.title("Newsletter")
        self.configure(bg="gray69", height=230, width=500)

        self.add_border()

        self.add_heading_label()

        self.add_instruction_label()

        self.add_box_frame()

        self.add_box_label()

        self.add_text_field()

        self.add_button()


    def add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.pack()

        #style
        self.heading_label.configure(font="Arial 24", text="RECEIVE OUR NEWSLETTER")

    def add_instruction_label(self):
        # create
        self.instruction_label = Label()
        self.instruction_label.pack()

        # style
        self.instruction_label.configure(font="Arial 12", text="Please enter your email below to receive our newsletter.")
    
    def add_box_frame(self):
        self.box_frame = Frame()
        self.box_frame.pack()

    def add_box_label(self):
        # create
        self.box_label = Label(self.box_frame)
        self.box_label.pack(side=LEFT)

        # style
        self.box_label.configure(font="Arial 12", text="Email: ")
    
    def add_text_field(self):
        # create
        self.text_field = Entry(self.box_frame)
        self.text_field.pack(side=RIGHT)

        # style
        self.text_field.configure(font="Arial 12", bg="Snow", bd="3", width=35)

    def add_button(self):
        #create
        self.button = Button()
        self.button.pack()

        #style
        self.button.configure(font="Arial 12", bg="LightPink1", width=42, text="Subscribe")

    def add_border(self):
        #create
        self.border = Canvas()
        self.border.pack

        #style
        self.border.configure(bg="gray92", bd=10, height=190, width=460)
# handle events
# (callback functions to handle events will go here)