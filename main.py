from tkinter import *
import math
root = Tk()
myCanvas = Canvas(root, height=1024, width=1024)
myCanvas.pack()

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, outline='black')

def plot_dot(x, y, canvsName):
    return create_circle(x, y, 1, canvsName)

corna = 5
cornb = 5
side = 20
for i in range(1000):
    for j in range(1000):
        x = corna + i * side / 100
        y = cornb + j * side / 100
        c = x * x + y * y
        d = math.ceil(c)
        if (d % 2 == 0):
            plot_dot(i, j, myCanvas)


root.mainloop()