# Turtle Fractal Generator

This is a Python-Turtle project that generates various fractal patterns using recursion. The program utilizes the Turtle graphics library to create intricate and visually appealing fractal designs. Each fractal comes with its own unique features and characteristics.

## Personal Figures

### Fern
- Added filled circles in recursion to resemble berries on the fern.

### Flake
- Changes pen color for each iteration of Koch.
- Fills the flake with a golden color upon completion.

### Pentaplex
- Designed Pentaplex without an outlining pentagon, resulting in a flower-like shape.
- Utilized the Sine rule to calculate figures and ratios required for creating Pentaplex.

### Square
- Constructed a square gasket using principles learned from the triangular gasket.

### H Tree
- Created the H Tree by dividing the drawing into four sections that repeat to form a dense image.

### CircleTriangle
- Developed the CircleTriangle fractal based on insights gained from creating the HalfCircle Gasket.
- Applied trigonometry to determine that the radius of the three inner circles in the fractal is equal to (1 + 2/sqrt(3)) * l.

### Circle3
- Similar to the HalfCircle fractal but with a different ratio between the two circles.
- Removed the outer circle to differentiate it from the HalfCircle fractal.
- Ensured that the larger circle appears on the left and the smaller circle on the right in both recursions.

### Carpet3
- Created an improved version of the carpet fractal that exclusively fills the negative space.

### Spiral
- Designed the Spiral fractal to produce a three-dimensional illusion.
- Implemented a line rotation of 1 degree less than an equilateral triangle's angle and reduced its length with each recursion.

### Bent Tree
- Developed a new tree fractal that bends inward and grows larger with each recursion.
- Applied knowledge gained from creating previous fractals to accomplish this effect.

## UI Personal Contribution

In addition to the fractal designs, significant effort has been put into enhancing the user interface (UI) to provide greater control and flexibility.

- Implemented an input field for both the x and y coordinates, allowing the user to position the pen at any point on the canvas to start drawing.
- When the user inputs values for x and y, the pen lifts and moves to the specified coordinates.
- Created two buttons that enable the user to turn the pen 45° to the left or right, providing control over the drawing direction of the fractal.
- Integrated two options menus for setting the pen color and canvas color, utilizing a wide range of colors from "Tkinter Programming by Jan Bodnar."
- Implemented a clear all button that resets the canvas, removing any previous drawings and clearing all entries.
- Included a display all button that showcases all the fractals on the canvas using different colors, allowing users to preview each fractal's appearance.
- Developed a function that handles the positioning and angle of the pen to draw the fractals accurately based on provided values for n and l.
- Set colors for the background and foreground of all widgets, ensuring an aesthetically pleasing UI.
- Imported `tkinter.ttk` as `ttk` to maintain compatibility and improve functionality of the options menus.
- Ensured that the UI looks visually appealing on both Windows and macOS platforms by utilizing the `highlightbackground` parameter to blend the widgets with the background color.
- Added an information panel that displays the name, length, and order of the currently drawn fractal.
