## Name:
## ID:
## Save this file as yourname_cs110_lab13.py and submit it to Canvas.
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

from graphics import GraphWin, Line, Polygon, Text, Entry, Point

class ShapeInteractionManager:
    def __init__(self, win):
        self.shapes = []
        self.win = win
        self.message = Text(Point(250, 30), "")
        self.message.setSize(12)
        self.message.draw(win)

    def add_colorline(self, point1, point2, color):
        line = Line(point1, point2)
        line.setFill(color)
        line.draw(self.win)
        self.shapes.append(line)

    def add_triangle(self, points, color):
        triangle = Polygon(points)
        triangle.setFill(color)
        triangle.draw(self.win)
        self.shapes.append(triangle)

    def add_text_input(self, location, prompt):
        self.message.setText(prompt)
        entry = Entry(location, 10)
        entry.draw(self.win)

        # Wait for user to press Enter and return the input
        while True:
            self.win.getMouse()  # Wait for a key press
            text = entry.getText()
            if text:  # Return the text if it's not empty
                entry.undraw()
                return text


def main():
    # Create the GraphWin
    win = GraphWin("Shape Interaction Manager", 500, 500)
    manager = ShapeInteractionManager(win)

    # Task 1: Draw a line between two points
    manager.message.setText("Click on two points to draw a line.")
    point1 = win.getMouse()
    point2 = win.getMouse()
    manager.add_colorline(point1, point2, "blue")

    # Task 2: Draw a triangle using three points
    manager.message.setText("Click on three points to draw a triangle.")
    points = [win.getMouse(), win.getMouse(), win.getMouse()]
    manager.add_triangle(points, "green")

    # Task 3: Allow the user to change the triangle's color
    color_prompt_location = Point(250, 470)
    color_input_location = Point(250, 450)
    new_color = manager.add_text_input(color_input_location, "Enter a color to change the triangle:")
    manager.shapes[-1].setFill(new_color)  # Update the last shape's color (triangle)

    # Task 4: Wait for user to quit
    manager.message.setText("Click anywhere to quit.")
    win.getMouse()  # Wait for a mouse click to close the window
    win.close()


if __name__ == "__main__":
    main()