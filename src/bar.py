class bar:
    def __init__(self, index, height, color, arrayLength, canvas):
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
        y = 500 - self.height
        self.canvas.create_rectangle(x, y, x + self.width, 400, fill=self.color)