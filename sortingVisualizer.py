from random import randint
from tkinter import*
from tkinter.ttk import*
from math import*

# creating the main window
root = Tk()

# giving the title to the main window
root.title("Sorting Algorithm")
root.geometry("500x500")
# creating a frame inside the main window
frame = Frame(root)
frame.pack()

# adding the label to the frame
label = Label(frame, text = "Sorting Visualizer")
label.pack()

# creating the square object class
class bars:
    width = 20
    def __init__(self,index, height, color):
        self.index = index
        self.height = height
        self.color = color
        self.draw(canvas)
        
    def draw(self,canvas):
        self.canvas = canvas
        x = self.index * self.width
        y =  400 - self.height
        self.canvas.create_rectangle(x, y , x + self.width, 400, fill = self.color)
            

canvas = Canvas(root, width = 400, height = 400 , background="black")
canvas.pack()

array = []
# create a random array 
for i in range(20):
    array.append(randint(0, 400))

barsList = []
for i in range(len(array)):
    barsList.append(bars(i, array[i], "red"))

def reDraw():
    canvas.delete("all")
    for i in range(len(array)):
        barsList[i].draw(canvas)
    canvas.update()


def drawGraph():
    for i in range(len(array)):
        barsList[i].draw(canvas)
        canvas.after(100)
        canvas.update()
    

def sort():
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                barsList[i] = bars(i, array[i], "blue")
                barsList[j] = bars(j, array[j], "blue")
    
                canvas.after(100)
                reDraw()
                canvas.update()
    print(array)


class sortingAlgos:
    def bubbleSort():
        n = len(array)
        for i in range(n):
            for j in range(0, n-i-1):
                if(array[j] > array[j+1]):
                    array[j], array[j+1] = array[j+1], array[j]
                    barsList[j] = bars(j, array[j], "red")
                    barsList[j+1] = bars(j+1, array[j+1], "red")
                    reDraw()
                    canvas.update()
                    canvas.after(100)
            barsList[n - i - 1] = bars( len(array) - i - 1, array[len(array) - i - 1], "blue")

    def insertionSort():
        pass

    def selectionSort():
        pass

    def mergeSort():
        pass

    def quickSort():
        pass


# creating the buttons
simpleSortButton = Button(frame, text="Simple Sort", command = sort)
simpleSortButton.pack()

bubbleSortButton = Button(frame, text="Bubble Sort", command=sortingAlgos.bubbleSort)
bubbleSortButton.pack()
root.mainloop()

