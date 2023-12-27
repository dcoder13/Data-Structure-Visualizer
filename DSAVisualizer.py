from random import randint
import tkinter as tk
from math import *
from tkinter import ttk

# making the global variables
array = []
barsList = []

stopSorting = False
speed = 5

class bars:
    def __init__(self, index, height, color, arrayLength):
        self.index = index
        self.height = height
        if color != "null":
            self.color = color
        else:
            self.color = color

        self.width = 500 / arrayLength
        self.draw(canvas)

    def draw(self, canvas):
        self.canvas = canvas
        x = self.index * self.width
        y = 400 - self.height
        self.canvas.create_rectangle(x, y, x + self.width, 400, fill=self.color)


def intitDraw():
    for i in range(len(array)):
        barsList.append(bars(i, array[i], "red", len(array)))
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
            if stopSorting:
                return
            for j in range(0, n - i - 1):
                if stopSorting:
                    return
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    barsList[j] = bars(j, array[j], "red", n)
                    barsList[j + 1] = bars(j + 1, array[j + 1], "red", n)
                    reDraw()
                    canvas.after(int(200//speed))
            barsList[n - i - 1] = bars(
                len(array) - i - 1, array[len(array) - i - 1], "blue", n
            )

    def insertionSort():
        print(array)
        n = len(array)
        for i in range(1, n):
            j = i - 1
            while j >= 0 and array[j+1] < array[j]:
                if stopSorting:
                    return
                array[j + 1], array[j] = array[j], array[j+1]
                barsList[j + 1] = bars(j + 1, array[j + 1], "blue", n)
                barsList[j] = bars(j, array[j], "blue", n)
                reDraw()
                canvas.after(int(200//speed))
                j -= 1
            if stopSorting:
                return
        print(array)

    def selectionSort():
        print(array)
        n = len(array)
        for i in range(n):
            for j in range(i+1,n):
                if stopSorting:
                    return
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
                    barsList[i] = bars(i, array[i], "blue", n)
                    barsList[j] = bars(j, array[j], "red", n)
                    reDraw()
                    canvas.after(int(200//speed))
            if stopSorting:
                return
            barsList[i] = bars(i, array[i], "blue", n)
            reDraw()
        print(array)

    def mergeSort():
        print(array)
        n = len(array)
        def merge(low, mid, high):
            if stopSorting:
                return
            n1 = mid - low + 1
            n2 = high - mid
            L = [0] * (n1)
            R = [0] * (n2)
            for i in range(0, n1):
                L[i] = array[low + i]
            for j in range(0, n2):
                R[j] = array[mid + 1 + j]
            i = 0
            j = 0
            k = low
            while i < n1 and j < n2:
                if stopSorting:
                    return
                if L[i] <= R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                barsList[k] = bars(k, array[k], "blue", len(array))
                reDraw()
                canvas.after(int(200//speed))
                k += 1
            while i < n1:
                if stopSorting:
                    return
                array[k] = L[i]
                barsList[k] = bars(k, array[k], "blue", len(array))
                reDraw()
                canvas.after(int(200//speed))
                i += 1
                k += 1
            while j < n2:
                if stopSorting:
                    return
                array[k] = R[j]
                barsList[k] = bars(k, array[k], "blue", len(array))
                reDraw()
                canvas.after(int(200//speed))
                j += 1
                k += 1
        def divide(low, high):
            if low < high:
                if stopSorting:
                    return
                mid = (low + high) // 2
                divide(low, mid)
                divide(mid + 1, high)
                merge(low, mid, high)
        divide(0, n - 1)
        print(array)

    def quickSort():
        print(array)
        n = len(array)
        def partition(low, high):
            i = low - 1
            pivot = array[high]
            for j in range(low, high):
                if stopSorting:
                    return
                if array[j] < pivot:
                    i += 1
                    array[i], array[j] = array[j], array[i]
                    barsList[i] = bars(i, array[i], "red", n)
                    barsList[j] = bars(j, array[j], "red", n)
                    reDraw()
                    canvas.after(int(200//speed))
            array[i+1], array[high] = array[high], array[i+1]
            barsList[i+1] = bars(i+1, array[i+1], "green", n)
            barsList[high] = bars(high, array[high], "red", n)
            reDraw()
            canvas.after(int(200//speed))
            return i+1
        def quick(low, high):
            if low < high:
                pi = partition(low, high)
                quick(low, pi-1)
                for i in range(low, pi):
                    if stopSorting:
                        return
                    barsList[i] = bars(i, array[i], "blue", n)
                canvas.after(int(200//speed))
                quick(pi+1, high)
                for i in range(pi, high+1):
                    if stopSorting:
                        return
                    barsList[i] = bars(i, array[i], "blue", n)
                canvas.after(int(200//speed))
        quick(0, n-1)
        print(array)


# creating the main window
root = tk.Tk()

root.title("DSA Visualizer")
root.geometry("700x500")
root.configure(background="white")
root.resizable(False, False)

# title Frame
titleFrame = tk.Frame(root)
titleFrame.pack()

titleLabel = tk.Label(
    titleFrame,
    text="DSA Visualizer",
    width=700,
    font=("Serif Sans", 15),
    background="black",
    foreground="white",
    justify="center",
    anchor="center",
)
titleLabel.config(padx=10, pady=10)
titleLabel.pack()

# drawing canvas frame
canvasFrame = tk.Frame(root)
canvasFrame.pack(side=tk.LEFT)

# creating the canvas
canvas = tk.Canvas(canvasFrame, width=500, height=400, background="black")
canvas.pack(pady=10)


# creating the selection frame
selectionFrame = tk.Frame(root)
selectionFrame.configure(height=500, width=200)
selectionFrame.pack(side=tk.RIGHT, anchor="n")

# creating the selection label
selectionLabel = tk.Label(
    selectionFrame,
    text="Select Algorithm",
    font=("Serif Sans", 10),
    width="200",
    background="black",
    foreground="white",
)
selectionLabel.pack(pady=10)


# creating the selection combobox
selection = tk.ttk.Combobox(selectionFrame, width=200)
selection["values"] = (
    "Bubble Sort",
    "Insertion Sort",
    "Selection Sort",
    "Merge Sort",
    "Quick Sort",
)
selection.current(0)
selection.pack(pady=10)


def startSort():
    global stopSorting
    stopSorting = False
    selected_option = selection.get()
    switcher = {
        "Bubble Sort": sortingAlgos.bubbleSort,
        "Insertion Sort": sortingAlgos.insertionSort,
        'Selection Sort': sortingAlgos.selectionSort,
        'Merge Sort': sortingAlgos.mergeSort,
        'Quick Sort': sortingAlgos.quickSort
    }
    func = switcher.get(selected_option, lambda: "Invalid")
    func()


# start button
startButton = tk.Button(selectionFrame, text="Start", command=startSort, width=200)
startButton.pack(pady=10)

# reset button
resetButton = tk.Button(selectionFrame, text="Reset", command=initArray, width=200)
resetButton.pack(pady=10)

#frame for algo speed
speedFrame = tk.Frame(selectionFrame, width=200)
speedFrame.pack(pady=10)
speedLabel = tk.Label(speedFrame, text="Speed", width=100, background="black", foreground="white")
speedLabel.pack(pady=10)
speedVar = tk.IntVar(speedFrame, 5)
# scroll bar for speed
speedScale = tk.Scale(speedFrame, from_=1, to=100, orient=tk.HORIZONTAL, variable=speedVar, resolution = 1)
speedScale.set(5)
speedScale.pack(pady=10)

# text box for speed
speedEntry = tk.Entry(speedFrame, textvariable=speedVar, width=10)
speedEntry.insert(0, speedVar.get())
speedEntry.pack(side=tk.LEFT, pady=10)
def updateSpeedScale(*args):
    global speed
    if speedVar.get():
        speed= min(100, speedVar.get())
    else:
        speed = 1
speedVar.trace_add("write", updateSpeedScale)

initArray()
root.mainloop()
