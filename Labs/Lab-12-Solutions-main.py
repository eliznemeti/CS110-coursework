## Name:
## ID:
## Save this file as yourname_cs110_lab12.py and submit it to Canvas.
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

from graphics import Point
from Lab_12_Solutions_Shape import ShapeManager

def main():
    manager = ShapeManager("Shape Manager", 400, 400)

    # Add shapes as per the instructions
    manager.add_circle(Point(2, 2), 2, "red")
    manager.add_rectangle(Point(3, 3), Point(6, 5), "blue")
    manager.add_circle(Point(2, 2), 1, "green")

    # Wait for user to close the window
    manager.win.getMouse()
    manager.win.close()

if __name__ == "__main__":
    main()