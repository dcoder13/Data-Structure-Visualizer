from random import randint
from .node import node


class dataStructures:
    def __init__(self , nextFrame , array, Grid, nodeGrid , canvas):
        self.array = array
        self.Grid = Grid
        self.nodeGrid = nodeGrid
        self.nextFrame = nextFrame
        self.canvas = canvas

    # each structure will be provided with a grid and a nodeGrid
    # the DS can manupulate the grid and the nodeGrid accordingly
    

    def testStructure(self):
        print("testStructure")
        # self.nodeGrid[0][0] = node(len(self.Grid), 1 , 0 , 0 , self.canvas , "black" )
        # self.nextFrame
        for i in range(len(self.Grid[0])):
            for j in range(len(self.Grid[i])):
                self.nodeGrid[i][j] = node(len(self.Grid) , 1 , i , j , self.canvas , "black")
                self.nextFrame()
        print("completed")

    def graph(self):

        pass

    def binarySearchTree(self):
        print("Starting BT")
        pass

    def binaryTree(self):
        pass

    def linkedList(self):
        pass

    def queue(self):
        pass

    def stack(self):
        pass
    