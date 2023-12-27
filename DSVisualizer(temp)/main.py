import threading
import tkinter as tk
from tkinter import ttk
from src import sortRender
from src import dsRender


root = tk.Tk()
root.title("Data Structure Visualizer")
root.geometry("700x500")
root.configure(background="white")
root.resizable(False, False)
  
def startCompute( SR , canvas , selection , speed):
    global computeThread
    # computeThread = threading.Thread(target=SR.startSort, args=(selection,))
    # computeThread.start()
    SR.startSort(selection)

def stopCompute(SR):
    SR.reset()    
    pass

def secondaryFrameSetup():
    global speed
    speed = [50]
    secondaryFrame = tk.Frame(root)

    # title Frame
    titleFrame = tk.Frame(secondaryFrame)
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

    # setting up the canvas
    canvasFrame = tk.Frame(secondaryFrame)
    canvasFrame.pack(side=tk.LEFT)
    canvas = tk.Canvas(canvasFrame, width=500, height=400, background="black")
    canvas.pack(pady=10)
    selectionFrame = tk.Frame(secondaryFrame)
    selectionFrame.configure(height=500, width=200)
    selectionFrame.pack(side=tk.RIGHT, anchor="n")
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

    SR = sortRender.sortRender(canvas, speed)    

    # start button
    startButton = tk.Button(selectionFrame, text="Start", command=lambda: startCompute(SR , canvas , selection , speed), width=200)
    startButton.pack(pady=10)

    # reset button
    resetButton = tk.Button(selectionFrame, text="Reset", command=lambda: stopCompute(SR), width=200)
    resetButton.pack(pady=10)

    # frame for algo speed
    speedFrame = tk.Frame(selectionFrame, width=200)
    speedFrame.pack(pady=10)
    speedLabel = tk.Label(speedFrame, text="Speed", width=100, background="black", foreground="white")
    speedLabel.pack(pady=10)
    speedVar = tk.IntVar(speedFrame, 5)
    # scroll bar for speed
    speedScale = tk.Scale(speedFrame, from_=1, to=100, orient=tk.HORIZONTAL, variable=speedVar, resolution = 1)
    speedScale.set(speed[0])
    speedScale.pack(pady=10)

    # text box for speed
    speedEntry = tk.Entry(speedFrame, textvariable=speedVar, width=10)
    speedEntry.insert(0, speedVar.get())
    speedEntry.pack(side=tk.LEFT, pady=10)

    def updateSpeedScale(*args):
        if speedVar.get():
            global speed
            speed[0] = min(100, speedVar.get())
        else:
            speed[0] = 1
    speedVar.trace_add("write", updateSpeedScale)
    secondaryFrame.pack()

def mainFrameSetup():
    pass

secondaryFrameSetup()
root.mainloop()


