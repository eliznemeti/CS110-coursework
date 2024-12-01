## Name:
## ID:
## Save this file as yourname_cs110_lab12.py and submit it to Canvas.
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

from graphics import GraphWin, Point, Circle, Rectangle

class ShapeManager:
    def __init__(self, win_title, win_width, win_height):
        self.shapes = []
        self.win = GraphWin(win_title, win_width, win_height)
        self.win.setCoords(0.0, 0.0, 10.0, 10.0) 

    def add_circle(self, center, radius, color):
        circle = Circle(center, radius)
        circle.setFill(color)
        circle.draw(self.win)
        self.shapes.append(circle)

    def add_rectangle(self, bottom_left, top_right, color):
        rectangle = Rectangle(bottom_left, top_right)
        rectangle.setFill(color)
        rectangle.draw(self.win)
        self.shapes.append(rectangle)

    def change_color(self, index, color):
        if 0 <= index < len(self.shapes):
            shape = self.shapes[index]
            shape.setFill(color)
        else:
            raise IndexError("Index out of range")

    def delete_shape(self, index):
        if 0 <= index < len(self.shapes):
            shape = self.shapes.pop(index)
            shape.undraw()
        else:
            raise IndexError("Index out of range")