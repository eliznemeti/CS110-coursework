## Name:
## ID:
## Save this file as yourname_cs110_lab13.py and submit it to Canvas.
"""
This code was my own work, it was written without consulting any sources
outside of those approved by the instructor. 
Initial: 
"""

'''[15 pts] Task 1: Define a class `ShapeInteractionManager` with the following:
# - Attributes:
#   - `shapes`: A list to store all graphical objects, such as lines, circles, rectangles, and polygons.
#   - `win`: A `GraphWin` object to display the shapes and handle interactions.
#   - `message`: A `Text` object for prompts and instructions in the window.
# - Methods:
#   1. `add_colorline(point1, point2, color)`:
#      - Takes two points and a color as input.
#      - Draws a colored line between the two points and adds it to the `shapes` list.
#   2. `add_triangle(points, color)`:
#      - Takes three points (mouse clicks) and a color as input.
#      - Creates and draws a triangle (polygon) using the points and adds it to the `shapes` list.
#   3. `add_text_input(location, prompt)`:
#      - Displays an editable `Entry` box at the specified location.
#      - Displays the provided prompt above the box.
#      - Returns the text entered in the box when the function is called.
'''

'''[5 pts] Task 2: Implement the following in the main program:
# 1. Create a `GraphWin` titled "Shape Interaction Manager" with dimensions 500x500 pixels.
# 2. Display an initial prompt: "Click on two points to draw a line."
# 3. Add a line between two points based on mouse clicks (use `getMouse()` to get points).
# 4. Change the prompt to: "Click on three points to draw a triangle."
# 5. After the triangle is drawn, prompt the user with: "Enter a color to change the triangle."
#    - Use an `Entry` box to get the color input and update the triangle’s color.
# 6. Finally, display: "Click anywhere to quit." and close the window upon a mouse click.

# Additional Notes:
# - Use the `graphics` library for all graphical operations.
# - Be sure to test your program to ensure all functionalities work as described.

# Expected Output:
# - A line and a triangle displayed in a graphical window.
# - The triangle changes color based on user input.
'''