# Python-Turtle
Turtle Fractal Generator

Below are details of my personal figures and personal contributions to the project.

**Personal Figures**
	
	■  Fern:
		• Added filled circle in recursion to look like berries on the fern.

	■  Flake:
		• Pen changes colours for each iteration of Koch.
		• Flake is filled with gold colour after completion.

	■  Pentaplex:
		• Designed Pentaplex to not have an outlining pentagon, creating a flower-like shape.
		• Used Sine rule to calculate figures and ratios needed to create pentaplex.

	■  Square:
		• Created square gasket using principles learned from the triangular gasket.

	■  H Tree:
		• Created the H Tree by splitting the drawing into four sections which repeat to create a dense image.

	■  CircleTriangle:
		• After creating the simpler halfCircle Gasket, it was easier to understand the use of circles in recursive fractals.
		• Used trigonometry to find that the radius of the three inner circles of the fractal have a radius of (1 + 2/root3)*l.

	■  Circle3:
		• The dual circle was similar to the halfCircle only the ratio of the two circles was different.
		• I removed the outer circle to make the fractal less similar to the halfCircle.
		• It was essential for me to ensure that the larger circle was on the left and smaller on the right within both recursions.

	■  Carpet3:
		• After creating my first iteration of the carpet, which I decided not to use, 
		• I was unhappy and wanted to make a carpet that only filled the negative space.

	■  Spiral:
		• I created the spiral to use a different type of fractal that would create a 3D illusion. 
		• To do this, I made it so that a line would turn 1 degree less than it would to form the angle of an equilateral triangle 
		  and reduce in length by each recursion.

	■  Bent Tree:
		• To come full circle, I created a new tree fractal. This time using some of what I learned from creating previous fractals
		  I was able to create a tree that would bend in on itself and grow larger the more recursions were called.
		

**UI Personal Contribution**
	
	• I wanted to give the user a lot of control over the interface.
	• I created an entry input for both the x & y position. Using this, the user can position the pen on any point of the canvas to start the drawing.
	• Once the user inputs values for x and y, the pen will lift and goto the inputted coordinates.
	• I created two buttons that would allow the user to turn the pen 45° to the left or the right to give control of the direction the fractal is drawn.
	• I created two options menus so the user could set both the pen colour and canvas colour.
	• I used a list of colours from "Tkinter Programming by Jan Bodnar" so the user would have a wide selection of colours.
	• I created a clear all button that would reset the canvas, removing any drawings made and clearing all entries.
	• I created a display all button that draws all of the fractals on the canvas using different colours to display how each fractal looks.
	• To do this, I set values for n and l in a function that moved the pen to the correct location and angle to draw the fractal.
	• I set colours for the background and foreground of all the widgets.
	• I imported tkinter.ttk as ttk to use it when needed, and it would not interrupt my use of tk inter. I used this to create more functional optionsmenus.
	• I did this while working on my Windows PC at home when I opened my project on the Mac in the University,
	  I realised that this did not look right on Mac OS. This is because Tkinter takes some of its elements from the OS it is operating on.
	  Because of this, I had to design the UI to look nice on both platforms using highlightbackground, which made the widgets blend into the background colour.
	• I created an information panel that displays the name, length and order of the fractal drawn.
