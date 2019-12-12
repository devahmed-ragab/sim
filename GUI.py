from tkinter import *


root = Tk()
val = Label(root, text = "electricity Monitor simulator")

topFrame = Frame(root)
topFrame.pack()
downFrame = Frame(root)
downFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Start", fg="blue")
button2 = Button(downFrame, text="Terminate", fg="Red")

button1.pack(side=LEFT)
button2.pack(side=LEFT)







val.pack()
root.mainloop()