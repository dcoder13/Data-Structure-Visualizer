
from random import randint
import tkinter as tk
from tkinter import ttk
from src.node import node
from src.dataStructures import dataStructures
class dsRender:

    # array will be used by the data structure to fill the data into the grid accordingly 

    def __init__(self, canvas, speed):
        self.array = []
        self.grid = [[]]
        self.nodeGrid = [[]]
        self.canvas = canvas
        self.speed = speed
        self.initGrid()

    def inputBox(self, root):
        # the input box will take the array input from the user, and then change the a
        self.array_var = tk.StringVar(root, self.array)
        self.inputBox = tk.Entry(root, textvariable=self.array_var, width=10)
        self.inputBox.pack()
        self.inputBox.focus_set()
        self.inputBox.setvar('[]' , self.array_var)
        self.array_var.trace_add("write", self.updateArray)
        return self.inputBox

    def updateArray(self, *args):
        
        try:
            self.array = eval(self.inputBox.get())
        except Exception as e:
            print(e)

        print(self.array)

    # initializes with an empty black grid and an empty array
    def initGrid(self):
        self.canvas.delete("all")
        self.array.clear()
        self.grid.clear()
        self.nodeGrid.clear()
        # keep the array empty for during insitialization
        # we will keep the size of the grid to be 8 x something
        for i in range(2**(4-1)):
            self.grid.append([])
            for j in range(2**(4 - 1)):
                self.grid[i].append("null")

        self.initDraw()

    def run(self):
        pass

    def initDraw(self):
        for i in range(len(self.grid)):
            self.nodeGrid.append([])
            for j in range(len(self.grid[i])):
                self.nodeGrid[i].append(node(len(self.grid),self.grid[i][j], i, j, self.canvas, "white"))
        self.canvas.update()
        print("drawn")

    def reDraw(self):
        self.canvas.delete("all")
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.nodeGrid[i][j].draw()
        self.canvas.update()

    def nextFrame(self):
        print("nextFrame")
        self.reDraw()
        if(self.speed[1] == -1):
            raise Exception("Sort Stopped")
        elif(self.speed[1] > 0):
            self.canvas.after(int(200//self.speed[0]))
        else:
            print("paused")
            while(self.speed[1] == 0):
                self.canvas.after(50)
                self.canvas.update()
        

    def reset(self):
        self.initGrid()

    def startGrid(self, selection):
        self.initGrid()
        selected_option = selection.get()
        DA = dataStructures(self.nextFrame, self.array , self.grid , self.nodeGrid, self.canvas)
        switcher = {
            "testStructure" : DA.testStructure,
            "Stack": DA.stack,
            "Queue": DA.queue,
            "Linked List": DA.linkedList,
            "Binary Tree": DA.binaryTree,
            "Binary Search Tree": DA.binarySearchTree,
            "Graph": DA.graph,
        }
        func = switcher.get(selected_option, lambda: "Invalid")
        func()
    