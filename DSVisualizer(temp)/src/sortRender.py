
from random import randint
import tkinter as tk
from tkinter import ttk
from src.bar import bar
from src.sortingAlgos import sortingAlgos

class sortRender:
    def __init__(self, canvas, speed):
        self.array = []
        self.barsList = []
        self.canvas = canvas
        self.speed = speed
     
    def initArray(self):
        self.canvas.delete("all")
        self.array.clear()
        self.barsList.clear()
        for i in range(50):
            self.array.append(randint(0, 400))
        print(self.array, "init array")
        self.initDraw()

    def run(self):
        self.initArray()
        self.root.mainloop()

    def initDraw(self):
        for i in range(len(self.array)):
            self.barsList.append(bar(i, self.array[i], "red", len(self.array), self.canvas))
        self.canvas.update()

    def reDraw(self):
        self.canvas.delete("all")
        for i in range(len(self.array)):
            self.barsList[i].draw(self.canvas)
        self.canvas.update()

    def reset(self):
        self.initArray()

    def startSort(self, selection):
        self.initArray()
        selected_option = selection.get()
        print(selected_option,"from sortRender")
        SA = sortingAlgos(self.reDraw, self.array, self.barsList, self.canvas, self.speed)
        switcher = {
            "Bubble Sort": SA.bubbleSort,
            "Insertion Sort": SA.insertionSort,
            'Selection Sort': SA.selectionSort,
            'Merge Sort': SA.mergeSort,
            'Quick Sort': SA.quickSort
        }
        func = switcher.get(selected_option, lambda: "Invalid")
        func()
    
