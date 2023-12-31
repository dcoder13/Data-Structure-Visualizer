class node:

    # structure :- each node will have a boundary area , a draw area and a value , the position of the node will be provided as xpos and ypos
    def __init__(self, gridLength , value , xpos , ypos , canvas , color):
        self.gridLength = gridLength
        self.value = value
        self.xpos = xpos
        self.ypos = ypos
        self.canvas = canvas
        self.color = color
        # the side length of the each node (depends on the total number of nodes in )
        self.sideLength = 500/gridLength
        self.drawLength = self.sideLength/2
        self.draw()

    def draw(self):
        x = self.xpos * self.sideLength
        y = self.ypos * self.sideLength

        self.canvas.create_rectangle(x , y , x + self.sideLength , y + self.sideLength , fill = self.color) 
        if(self.value != "null"):
            self.canvas.create_text(x + self.drawLength , y + self.drawLength , text = self.value , font = ("Purisa" , 20))
        
