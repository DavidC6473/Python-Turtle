# import lines
from tkinter import *
import tkinter.ttk as ttk
import turtlefigures
import turtle


# make the frame and give its geometry
root = Tk()
root.title("Turtle Application")
root.geometry("1600x1250+300+300")
root.configure(bg = "PeachPuff2")

# ----------make the interface--------------

# make the canvas panel

canvasPanel = LabelFrame(root, text = "Canvas Frame", bg = "PeachPuff2")
canvasPanel.grid(row = 1, column = 5, columnspan = 100, rowspan = 100)

canvas = Canvas(canvasPanel, width = 1250, height = 1200, bg = "#adb6ee")
canvas.pack()

# make the control panel
controlPanel = LabelFrame(root, text = "Control Frame", bg = "#ffebcd")
controlPanel.grid(row = 0, column = 0, columnspan = 3, rowspan = 19)

# get the canvas pen and screen
screen = turtle.TurtleScreen(canvas)
pen = turtle.RawTurtle(screen)

# make info panel
infoPanel = LabelFrame(root, text = "Fractal Information", bg = "#ffebcd")
infoPanel.grid(row = 21, column = 0, columnspan = 3, rowspan = 5)

infoText = Text(infoPanel, height = 50, width = 40, bg = "lavender blush", fg = "#e63e6e", highlightbackground = "#ffebcd")
infoText.pack()


# control turtle pen and screen
###pen = Pen()
pen.color("black")
pen.speed(0)
pen.shape("turtle")
pen.width(1)
pen.fillcolor("black")

###screen = Screen()
screen.bgcolor("#adb6ee")

# make the first label
label = Label(controlPanel, bg = "#ffebcd", fg = "black", text = "Turtle Generator")
label.grid(row = 0, column = 0, columnspan = 2)

# make the length widgets
lengthLabel = Label(controlPanel, bg = "#ffebcd", fg = "black", text = "Length")
lengthLabel.grid(row = 1, column = 0)

lengthStr = StringVar()
lengthEntry = Entry(controlPanel, highlightbackground = "#ffebcd", textvariable = lengthStr)
lengthEntry.grid(row = 1, column = 1)

# make the order widgets
orderLabel = Label(controlPanel, bg = "#ffebcd", fg = "black", text = " Order")
orderLabel.grid(row = 2, column = 0)

orderStr = StringVar()
orderEntry = Entry(controlPanel, highlightbackground = "#ffebcd", textvariable = orderStr)
orderEntry.grid(row = 2, column = 1)

# make the X widgets
xLabel = Label(controlPanel, bg = "#ffebcd", fg = "black", text = "   X:")
xLabel.grid(row = 5, column = 0)

xStr = StringVar()
xEntry = Entry(controlPanel, highlightbackground = "#ffebcd", textvariable = xStr)
xEntry.grid(row = 5, column = 1)

# make the Y widgets
yLabel = Label(controlPanel, bg = "#ffebcd", fg = "black", text = "   Y:")
yLabel.grid(row = 6, column = 0)

yStr = StringVar()
yEntry = Entry(controlPanel, highlightbackground = "#ffebcd", textvariable = yStr)
yEntry.grid(row = 6, column = 1)


# make the position label
goToLabel = Label(controlPanel, bg = "#ffebcd", fg = "black", text = "Turtle Position")
goToLabel.grid(row = 4, column = 0, columnspan = 2)

# make go to button
def goToF():
    # tells pen where to go
    pen.up()
    pen.goto(int(xStr.get()), int(yStr.get()))
    pen.down()
    
#end
goToButton = Button(controlPanel, text = "   Go To   ", highlightbackground = "#ffebcd", bg = "#f0cdff", fg = "black", command = goToF)
goToButton.grid(row = 7, column = 1)


# make clear L & O button
def clearLOF():
    # reset the entries using their textvars
    lengthStr.set("")
    orderStr.set("")
    
#end
clearLOButton = Button(controlPanel, text = "Clear L & O", highlightbackground = "#ffebcd", bg = "#f0cdff", fg = "black", command = clearLOF)
clearLOButton.grid(row = 3, column = 0)


# make clear X & Y button
def clearXYF():
    # reset the entries using their textvars
    xStr.set("")
    yStr.set("")
    
#end
clearXYButton = Button(controlPanel, text = "Clear X & Y", highlightbackground = "#ffebcd", bg = "#f0cdff", fg = "black", command = clearXYF)
clearXYButton.grid(row = 7, column = 0)


# make clear all button
def clearF():
    # reset the entries using their textvars
    lengthStr.set("")
    orderStr.set("")
    xStr.set("")
    yStr.set("")
    screen.reset()
    pen.color(pencolorStr.get())
    pen.speed(0)
    infoText.delete("1.0","end")

    
#end
clearButton = Button(controlPanel, text = "  Clear All  ", highlightbackground = "#ffebcd", bg = "#f0cdff", fg = "black", command = clearF)
clearButton.grid(row = 18, column = 0)


# make left button
def leftF():
    pen.left(45)

leftButton = Button(controlPanel, text = "    Left 45°  ", highlightbackground = "#ffebcd", bg = "#f0cdff", fg = "black", command = leftF)
leftButton.grid(row = 9, column = 0)


# make right button
def rightF():
    pen.right(45)

rightButton = Button(controlPanel, text = "Right 45°", highlightbackground = "#ffebcd", bg = "#f0cdff", fg = "black", command = rightF)
rightButton.grid(row = 9, column = 1)

# make color set list

colorList = ["black", "white", "grey", "red", "green", "blue", "yellow", "orange", "pink", "purple", "cyan", "magenta", "brown", "lightblue", "lightgreen", "lightgrey", "gold", 'snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

# make colour option menu
pencolorStr = StringVar()
pencolorOptionMenu = ttk.OptionMenu(controlPanel, pencolorStr, colorList[0], *colorList)
pencolorOptionMenu.grid(row = 12, column = 0)
pencolorIndex = colorList.index(pencolorStr.get())


pencolorLabel = Label(controlPanel, text = "Set Pen Colour", bg = "#ffebcd", fg = "black")
pencolorLabel.grid(row = 11, column = 0)

# make pen color set button

def set1F():
    # reset the entries using their textvars
    pen.color(pencolorStr.get())
    
#end
set1Button = Button(controlPanel, text = "   Set Pen Color   ", highlightbackground = "#ffebcd", bg = "#f0cdff", fg = "black", command = set1F)
set1Button.grid(row = 12, column = 1)

# make colour option menu
bgcolorStr = StringVar()
bgcolorOptionMenu = ttk.OptionMenu(controlPanel, bgcolorStr, colorList[0], *colorList)
bgcolorOptionMenu.grid(row = 14, column = 0)
bgcolorIndex = colorList.index(bgcolorStr.get())


bgcolorLabel = Label(controlPanel, text = "Set Bg Colour", bg = "#ffebcd", fg = "black")
bgcolorLabel.grid(row = 13, column = 0)

# make bg color set button

def set2F():
    # reset the entries using their textvars
    screen.bgcolor(bgcolorStr.get())
    
#end
set2Button = Button(controlPanel, text = "Set Background Color", highlightbackground = "#ffebcd", bg = "#f0cdff", fg = "black", command = set2F)
set2Button.grid(row = 14, column = 1)

# make display all button
def allF():
    # get the value of order and length as int
    for i in range(20):
        infoText.insert(INSERT, "(☞ﾟ∀ﾟ)☞    (☞ﾟ∀ﾟ)☞    (☞ﾟ∀ﾟ)☞     (☞ﾟ∀ﾟ)☞\n\n")
    turtlefigures.all(pen)
    
     
#end
allButton = Button(controlPanel, text = "Display All", highlightbackground = "#ffebcd", bg = "#f0cdff", fg = "black", command = allF)
allButton.grid(row = 19, column = 0)

# make draw button
def drawF():
    #get order lenght
    length = int(lengthStr.get())
    order = int(orderStr.get())
    #get figure id
    figure = figureStr.get()
    figureId = figureList.index(figure)
    # if check to see what to draw
    if figureId == 0:
        # update info text
        infoText.insert(INSERT, "Fractal Name:\nTree\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        #draw Tree
        turtlefigures.tree(order, length, pen)
    elif figureId == 1:
        infoText.insert(INSERT, "Fractal Name:\nDandelion\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.dandelion(order, length, pen)
    elif figureId == 2:
        infoText.insert(INSERT, "Fractal Name:\nFern\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.fern(order, length, pen)
    elif figureId == 3:
        infoText.insert(INSERT, "Fractal Name:\nFlake\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.flake(order, length, pen)
    elif figureId == 4:
        infoText.insert(INSERT, "Fractal Name:\nFlake 2\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.flake2(order, length, pen)
    elif figureId == 5:
        infoText.insert(INSERT, "Fractal Name:\nAntiflake\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.antiflake(order, length, pen)
    elif figureId == 6:
        infoText.insert(INSERT, "Fractal Name:\nGasket\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.gasket(order, length, pen)
    elif figureId == 7:
        infoText.insert(INSERT, "Fractal Name:\nPentaplex\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.pentaplex(order, length, pen)
    elif figureId == 8:
        infoText.insert(INSERT, "Fractal Name:\nSquare\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.square(order, length, pen)
    elif figureId == 9:
        infoText.insert(INSERT, "Fractal Name:\nH Tree\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.htree(order, length, pen)
    elif figureId == 10:
        infoText.insert(INSERT, "Fractal Name:\nHalf Circle\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.halfCircle(order, length, pen)
    elif figureId == 11:
        infoText.insert(INSERT, "Fractal Name:\nCircle Cross\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.circleCross(order, length, pen)
    elif figureId == 12:
        infoText.insert(INSERT, "Fractal Name:\nCircle Triangle\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.circleTriangle(order, length, pen)
    elif figureId == 13:
        infoText.insert(INSERT, "Fractal Name:\nDual Circle\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.circle3(order, length, pen)
    elif figureId == 14:
        infoText.insert(INSERT, "Fractal Name:\nCarpet\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.carpet3(order, length, pen)
    elif figureId == 15:
        infoText.insert(INSERT, "Fractal Name:\nC Curve\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.c(order, length, pen)
    elif figureId == 16:
        infoText.insert(INSERT, "Fractal Name:\nSpiral\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.spiral(order, length, pen)
    elif figureId == 17:
        infoText.insert(INSERT, "Fractal Name:\nBent Tree\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\nOrder:\n%s\n\n" % (orderStrVar))
        turtlefigures.bentTree(order, length, pen)


drawButton = Button(controlPanel, text = "Draw", highlightbackground = "#ffebcd", bg = "#f0cdff", fg = "black", command = drawF)
drawButton.grid(row = 18, column = 1)


figureList = ["Tree", "Dandelion", "Fern", "Flake","Flake 2", "Antiflake", "Gasket", "Pentaplex", "Square", "H Tree", "Half Circle", "Circle Cross", "Circle Triangle", "Dual Circle", "Carpet", "C Curve", "Spiral", "Bent Tree"]
figureStr = StringVar()
figureOptionMenu = ttk.OptionMenu(controlPanel, figureStr, figureList[0], *figureList)
figureOptionMenu.grid(row = 17, column = 1)

