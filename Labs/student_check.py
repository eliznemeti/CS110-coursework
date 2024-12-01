#Task 1

from graphics import * 

class ShapeManager:
    def __init__ (self, win_title, win_width, win_height, color):
        self.shapes = []
        self.win = GraphWin(win_title, win_width, win_height)
        self.win.setCoords(0.0, 0.0, 10.0, 10.0)
        self.win.setBackground(color)
    
    def add_circle(self, center, radius, color):
        circle = Circle(Point(center[0], center[1]), radius)
        circle.setFill(color)
        circle.draw(self.win)
        self.shapes.append(circle)
    
    def add_rectangle(self, bottom_left, top_right, color):
        rec = Rectangle(Point(bottom_left[0], bottom_left[1]), Point(top_right[0], top_right[1]))
        rec.setFill(color)
        rec.draw(self.win)
        self.shapes.append(rec)

    def change_color(self, index, color):
        if 0 <= index < len(self.shapes):
            shape = self.shapes[index]
            shape.setFill(color)

    def delete_shape(self, index):
        if 0 <= index < len(self.shapes):
            shape = self.shapes.pop(index)
            shape.undraw()

def main():
    shape_manager = ShapeManager("Shape Manager", 400, 400, "white")
    shape_manager.add_circle(center=(2,2), radius=2, color='red')
    shape_manager.add_rectangle(bottom_left=(3,3), top_right = (6,5), color='blue')
    shape_manager.add_circle(center=(2,2), radius=1, color='green')
    shape_manager.win.getMouse()
    shape_manager.win.close()

if __name__ == "__main__":
    main()