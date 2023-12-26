from random import randint
from tkinter import *
from tkinter.ttk import *
from math import *

# making the global variables
array = []
barsList = []

stopSorting = False

class bars:
    def __init__(self,index, height, color , arrayLength):
        self.index = index
        self.height = height
        if(color != "null"):
            self.color = color
        else: self.color = color
        
        self.width = 500/arrayLength
        self.draw(canvas)
        
    def draw(self,canvas):
        self.canvas = canvas
        x = self.index * self.width
        y =  400 - self.height
        self.canvas.create_rectangle(x, y , x + self.width, 400, fill = self.color)
           
def intitDraw():
    for i in range(len(array)):
        barsList.append(bars(i, array[i], "red" , len(array)))
    canvas.update()

def reDraw():
    canvas.delete("all")
    for i in range(len(array)):
        barsList[i].draw(canvas)
    canvas.update()

# initializing array with random values
def initArray():
    global stopSorting
    stopSorting = True
    canvas.delete("all")
    array.clear()
    barsList.clear()
    for i in range(50):
        array.append(randint(0, 400))
    intitDraw()

# can add another option to make custom array
def customArray():
    pass

# class from sorting algos
class sortingAlgos:
    def bubbleSort():
        n = len(array)
        for i in range(n):
            if(stopSorting):
                break
            for j in range(0, n-i-1):
                if(array[j] > array[j+1]):
                    array[j], array[j+1] = array[j+1], array[j]
                    barsList[j] = bars(j, array[j], "red" , n)
                    barsList[j+1] = bars(j+1, array[j+1], "red" , n)
                    reDraw()
                    canvas.after(10)
            barsList[n - i - 1] = bars( len(array) - i - 1, array[len(array) - i - 1], "blue", n)

    def insertionSort():
        print(array)
        n = len(array)
        for i in range(1, n):
            key = array[i]
            if(stopSorting):
                break
            j = i - 1
            while(j+1 >= 0 and key < array[j]):
                array[j+1] = array[j]
                barsList[j+1] = bars(j+1, array[j+1], "blue" , n)
                
                reDraw()
                canvas.after(10)
                j -= 1
            array[j+1] = key
            reDraw()
        print(array)

    
    def selectionSort():
        pass

    def mergeSort():
        pass

    def quickSort():
        pass
        
        

# creating the main window
root = Tk()

root.title("DSA Visualizer")
root.geometry("700x500")
root.configure(background="white")
root.resizable(False, False)

#title Frame
titleFrame = Frame(root)
titleFrame.pack()

titleLabel = Label(titleFrame, text="DSA Visualizer", width=700, font=('Serif Sans', 15), background="black", foreground="white", justify="center", anchor="center")
titleLabel.config(padding=10)
titleLabel.pack()

# drawing canvas frame
canvasFrame = Frame(root)
canvasFrame.pack(side=LEFT)

# creating the canvas
canvas = Canvas(canvasFrame, width=500, height=400, background="black")
canvas.pack(pady=10)


# creating the selection frame
selectionFrame = Frame(root)
selectionFrame.configure(height=500, width=200)
selectionFrame.pack(side=RIGHT, anchor="n")

# creating the selection label
selectionLabel = Label(selectionFrame, text="Select Algorithm", font=('Serif Sans', 10), width="200", background="black", foreground="white")
selectionLabel.pack(pady=10)


# creating the selection combobox
selection = Combobox(selectionFrame, width=200)
selection['values'] = ('Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort')
selection.current(0)
selection.pack(pady=10)

def startSort():
    global stopSorting
    stopSorting = False
    selected_option = selection.get()
    switcher = {
        'Bubble Sort': sortingAlgos.bubbleSort,
        'Insertion Sort': sortingAlgos.insertionSort,
        # 'Selection Sort': sortingAlgos.selectionSort,
        # 'Merge Sort': sortingAlgos.mergeSort,
        # 'Quick Sort': sortingAlgos.quickSort
    }
    func = switcher.get(selected_option, lambda: "Invalid")
    func()


# start button
startButton = Button(selectionFrame,text="Start",command=startSort,width=200)
startButton.pack(pady=10)

# reset button
resetButton = Button(selectionFrame,text="Reset",command=initArray,width=200)
resetButton.pack(pady=10)

initArray()
root.mainloop()