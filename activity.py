# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Number Pad')
root.geometry('250x300')

# Create a frame to organize elements better
# frame = Frame(master=root, height=200, width=360, bg="#d0efff")

#


for i in range(4):
	# Configure rows and columns to resize window
	root.columnconfigure(i, weight=1, minsize=75)
	root.rowconfigure(i, weight=1, minsize=50)
  #




		frame.grid(row=i, column=j)
		label = Label(master=frame, text=nums[i][j], bg='#d0efff')
		label.pack(padx=3, pady=3)

# Start the GUI event loop
root.mainloop()
