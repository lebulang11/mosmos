from tkinter import *



def motion(event):

    canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10)


root = Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()
canvas.bind("<B1-Motion>", motion)
root.mainloop()
