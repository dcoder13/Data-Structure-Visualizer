import tkinter as tk
from tkinter import ttk
from random import randint
from .bar import bar
from .sortingAlgos import sortingAlgos



class mainFrame(sortingAlgos):

    def intitDraw(self):
        for i in range(len(self.array)):
            self.barsList.append(bar(i, self.array[i], "red", len(self.array), self.canvas))
        self.canvas.update()

    def initArray(self): #random values
        self.stopSorting = True
        self.sorted = False
        self.canvas.delete("all")
        self.array.clear()
        self.barsList.clear()
        for i in range(50):
            self.array.append(randint(0, 400))
        print(self.array, "init array")
        self.intitDraw()

    def run(self):
        self.initArray()
        self.root.mainloop()

    def __init__(self):
        self.array = []
        self.barsList = []
        self.speed = 10
        self.stopSorting = False
        self.root = tk.Tk()
        self.root.title("DSA Visualizer")
        self.root.geometry("700x500")
        self.root.configure(background="white")
        self.root.resizable(False, False)

        # title Frame
        titleFrame = tk.Frame(self.root)
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

        self.canvasFrame = tk.Frame(self.root)
        self.canvasFrame.pack(side=tk.LEFT)
        self.canvas = tk.Canvas(self.canvasFrame, width=500, height=400, background="black")
        self.canvas.pack(pady=10)
        self.selectionFrame = tk.Frame(self.root)
        self.selectionFrame.configure(height=500, width=200)
        self.selectionFrame.pack(side=tk.RIGHT, anchor="n")
        self.selectionLabel = tk.Label(
            self.selectionFrame,
            text="Select Algorithm",
            font=("Serif Sans", 10),
            width="200",
            background="black",
            foreground="white",
        )
        self.selectionLabel.pack(pady=10)

        # creating the selection combobox
        self.selection = tk.ttk.Combobox(self.selectionFrame, width=200)
        self.selection["values"] = (
            "Bubble Sort",
            "Insertion Sort",
            "Selection Sort",
            "Merge Sort",
            "Quick Sort",
        )
        self.selection.current(0)
        self.selection.pack(pady=10)

        # start button
        self.startButton = tk.Button(self.selectionFrame, text="Start", command=lambda: self.startSort(self.selection), width=200)
        self.startButton.pack(pady=10)

        # reset button
        self.resetButton = tk.Button(self.selectionFrame, text="Reset", command=lambda: self.initArray(), width=200)
        self.resetButton.pack(pady=10)

        # frame for algo speed
        self.speedFrame = tk.Frame(self.selectionFrame, width=200)
        self.speedFrame.pack(pady=10)
        self.speedLabel = tk.Label(self.speedFrame, text="Speed", width=100, background="black", foreground="white")
        self.speedLabel.pack(pady=10)
        self.speedVar = tk.IntVar(self.speedFrame, 5)
        # scroll bar for speed
        self.speedScale = tk.Scale(self.speedFrame, from_=1, to=100, orient=tk.HORIZONTAL, variable=self.speedVar, resolution = 1)
        self.speedScale.set(5)
        self.speedScale.pack(pady=10)

        # text box for speed
        self.speedEntry = tk.Entry(self.speedFrame, textvariable=self.speedVar, width=10)
        self.speedEntry.insert(0, self.speedVar.get())
        self.speedEntry.pack(side=tk.LEFT, pady=10)

        def updateSpeedScale(*args):
            if self.speedVar.get():
                self.speed= min(100, self.speedVar.get())
            else:
                self.speed = 1
        self.speedVar.trace_add("write", updateSpeedScale)


