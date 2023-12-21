# Imports
from tkinter import *

root = Tk()

view_events = Button(root, text="View Event")
view_events.pack()
create_events = Button(root, text="Create Event)
create_events.pack()
delete_events = Button(root, text="Delete Event")
delete_events.pack()

root.geometry("250x100")

root.mainloop()

