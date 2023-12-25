from tkinter import*
from tkinter.ttk import*
from math import*

# creating the main window
root = Tk()

# giving the title to the main window
root.title("First Program")
root.geometry("500x500")

# creating a frame inside the main window
frame = Frame(root)
frame.pack()

# adding the label to the frame
label = Label(frame, text = "Hello World!")
label.pack()

def clicked():
    label.configure(text = "line deleted")
    canvas.delete(line)



canvas = Canvas(root, width = 300, height = 300 , background="black")
line = canvas.create_line(0, 0, 100, 0, fill="red", width=3)
print(canvas.coords(line))

deg = pi/180

def rotateLine():
    coords = canvas.coords(line)
    rotatedCoords = [0 , 0 , coords[2]*cos(1*deg) - coords[3]*sin(1*deg) , coords[3]*cos(1*deg) + coords[2]*sin(1*deg)]
    canvas.coords(line, rotatedCoords)
    print(rotatedCoords)

def continueRotate():
    rotateLine()
    canvas.after(10 , continueRotate)

canvas.configure(scrollregion=(-150,-150, 150, 150))
canvas.pack()


button = Button(frame, text = "Rotate!" , command = continueRotate)
button.pack()

# calling the mainloop
root.mainloop()