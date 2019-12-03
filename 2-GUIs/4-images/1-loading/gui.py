from tkinter import *
from tkinter import messagebox

class Gui(Tk):
   
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Gui")

        self.ambo_image = PhotoImage(file="//pclures01/home/4bakel36/Documents/Problem Solving Through Programming/Week 7/COM404/2-GUIs/4-images/ambulance.gif")
        self.bike_image = PhotoImage(file="//pclures01/home/4bakel36/Documents/Problem Solving Through Programming/Week 7/COM404/2-GUIs/4-images/bike.gif")
        self.plane_image = PhotoImage(file="//pclures01/home/4bakel36/Documents/Problem Solving Through Programming/Week 7/COM404/2-GUIs/4-images/plane.gif")

        # add components
        self.__add_main_frame()
        self.__add_heading_label()
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()
        self.__add_example_entry()

    def __add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.grid(row=0, column=0)

    def __add_heading_label(self):
        # create
        self.heading_label = Label(self.main_frame)

        # layout
        self.heading_label.grid(row=0, column=0, columnspan=3)

        # style
        self.heading_label.configure(font="Arial 14", text="TRANSPORT")

    def __add_ambulance_image_label(self):
        self.ambo_image_label = Label(self.main_frame)
        self.ambo_image_label.grid(row=1, column=0)
        self.ambo_image_label.configure(image=self.ambo_image)
        self.ambo_image_label.bind("<Button-1>", self.ambo_clicked)

    def __add_bike_image_label(self):
        self.bike_image_label = Label(self.main_frame)
        self.bike_image_label.grid(row=1, column=1)
        self.bike_image_label.configure(image=self.bike_image)
        self.bike_image_label.bind("<Button-1>", self.bike_clicked)

    def __add_plane_image_label(self):
        self.plane_image_label = Label(self.main_frame)
        self.plane_image_label.grid(row=1, column=2)
        self.plane_image_label.configure(image=self.plane_image)
        self.plane_image_label.bind("<Button-1>", self.plane_clicked)
    
    def __add_example_entry(self):
        self.example_entry = Entry(self.main_frame)
        self.example_entry.grid(row=2, column=1, columnspan=3)
    
    def ambo_clicked(self, event):
        textBoxValue = self.example_entry.get()

        if textBoxValue == "":
            textBoxValue = "nothing"

        messagebox.showinfo("Ambo", "You have clicked the ambo and put \""+ textBoxValue + "\" in the text box.")

    def bike_clicked(self, event):
        messagebox.showinfo("Bike", "You have clicked the bike.")

    def plane_clicked(self, event):
        messagebox.showinfo("Plane", "You have clicked the plane.")

# Create an object of the Gui class when this module is executed
# This is for convenience. Normally the following would be in the main.py file.
# The if statement simply makes sure that the window is displayed when this file is run
# directly as opposed to being imported into another class.
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()

#https://github.com/dcunningham36
