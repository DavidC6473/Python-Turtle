from turtle import *
import math



def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)

#end 

def dandelion(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(90)
     dandelion(n-1, l/2, pen)
     pen.right(60)
     dandelion(n-1, l/2, pen)
     pen.right(60)
     dandelion(n-1, l/2, pen)
     pen.right(60)
     dandelion(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l)

#end

def fern(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(0.3*l)
     pen.left(55)
     fern(n-1, l/2, pen)
     pen.right(55)
     pen.forward(0.7*l)
     pen.right(40)
     fern(n-1, l/2, pen)
     pen.left(40)
     pen.forward(l)
     pen.left(5)
     fern(n-1, 0.8*l, pen)
     pen.right(5)
     pen.right(90)
     pen.fillcolor("red")
     pen.begin_fill()
     pen.circle(l*.05)
     pen.end_fill()
     pen.left(90)
     pen.backward(2*l)

#end 

def koch(n, l, pen):
     if n==0 or l<2 :
          pen.forward(l)
          return
     #endif
     koch(n-1, l/3, pen)
     pen.left(60)
     koch(n-1, l/3, pen)
     pen.right(120)
     koch(n-1, l/3, pen)
     pen.left(60)
     koch(n-1, l/3, pen)

#end 

def flake(n, l, pen):
     colors = ["white", "green", "blue"]
     y = 0
     pen.begin_fill()
     for i in range(3):
          pen.color(colors[y])
          koch(n, l, pen)
          pen.right(120)
          y += 1
     #endfor
     pen.fillcolor("gold")
     pen.end_fill()
#end


def antiflake(n, l, pen):
     for i in range(3):
          koch(n, l, pen)
          pen.left(120)
     #endfor
#end




def gasket(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     gasket(n-1, l/2, pen)
     pen.forward(l)
     pen.left(120)
     gasket(n-1, l/2, pen)
     pen.forward(l)
     pen.left(120)
     gasket(n-1, l/2, pen)
     pen.forward(l)
     pen.left(120)
#end
     



def pentaplex(n, l, pen):
     if n==0 or l<2 :
          return     
     #endif
     for i in range(5):
          pentaplex(n-1, (l)-(l*0.309016699437*2), pen)
          pen.forward((l/2)-(l*0.309016699437))
          pen.left(72)
          pen.forward((l/2)-(l*0.309016699437))
          pen.left(72)
          pen.forward((l/2)-(l*0.309016699437))
          pen.left(72)
          pen.forward((l/2)-(l*0.309016699437))
          pen.left(72)
          pen.forward((l/2)-(l*0.309016699437))
          pen.left(72)
          pen.forward((l/2)-(l*0.309016699437))
          pen.left(72)
          pen.forward((l/2)-(l*0.309016699437))
          pen.right(144)
          pen.forward((l/2)-(l*0.309016699437))
          pen.left(72)
          pen.forward((l/2)-(l*0.309016699437))
          pen.left(72)
#end




# vvv not in use vvv

def pent2(n, l, pen):
     if n==0 or l<2 :
          return     
     #endif
     for i in range(5):
          pent2(n-1, l*0.381966601126, pen)
          pen.forward(l)
          pen.left(72)
#end


     

def square(n, l, pen):
     if n==0 or l<2 :
          return     
     #endif
     square(n-1, l/3, pen)
     pen.forward(2*(l/3))
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(2*(l/3))
     pen.left(90)
     square(n-1, l/3, pen)
     pen.forward(2*(l/3))
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(2*(l/3))
     pen.left(90)
     square(n-1, l/3, pen)
     pen.forward(2*(l/3))
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(2*(l/3))
     pen.left(90)
     square(n-1, l/3, pen)
     pen.forward(2*(l/3))
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(2*(l/3))
     pen.left(90)
     pen.forward(l/3)
     pen.left(90)
     pen.forward(l/3)
     pen.right(90)
     square(n-1, l/3, pen)
     pen.right(90)
     pen.forward(l/3)
     pen.right(90)
     pen.forward(l/3)
     pen.right(180)
#end

def htree(n, l, pen):
     if n==0 or l<2 :
          return     
     #endif
     pen.forward(l/2)
     pen.left(90)
     pen.forward(l/2)
     pen.right(90)
     htree(n-1, l/2, pen)
     pen.left(90)
     pen.left(180)
     pen.forward(l)
     pen.right(90)
     htree(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l/2)
     pen.right(90)
     pen.forward(l)
     pen.left(90)
     pen.forward(l/2)
     pen.right(90)
     htree(n-1, l/2, pen)
     pen.left(90)
     pen.left(180)
     pen.forward(l)
     pen.right(90)
     htree(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l/2)
     pen.right(90)
     pen.forward(l/2)
     
#end
     
def flakeStem(n, l, pen):
     if n==0 or l<2 :
          return     
     #endif
     pen.forward(l)
     pen.backward(l/3)
     pen.right(60)
     flakeStem(n-1, l/2, pen)
     pen.left(120)
     flakeStem(n-1, l/2, pen)
     pen.right(60)
     pen.backward(2*(l/3))
#end

     
def flake2(n, l, pen):
     for i in range(6):
          flakeStem(n, l, pen)
          pen.left(60)
     #endfor
#end
     


     

def halfCircle(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     halfCircle(n-1, l/2, pen)
     pen.circle(l/2)
     pen.left(90)
     pen.up()
     pen.forward(l)
     pen.down()
     pen.left(90)
     pen.circle(l/2)
     pen.right(90)
     pen.up()
     pen.backward(l/2)
     pen.down()
     pen.right(90)
     halfCircle(n-1, l/2, pen)
     pen.left(90)
     pen.up()
     pen.backward(l/2)
     pen.down()
     pen.right(90)
     

def circleTunnel(n, l, pen):
     if n==0 or l<2 :
          return
     #endif

     circleTunnel(n-1, l*0.9, pen)
     pen.circle(l)
     

def circleCross(n, l, pen):
     for i in range(4):
          circleTunnel(n, l, pen)
          pen.left(90)
     #endfor
#end



def circleTriangle(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     for i in range(3):

          #cos(30) = 1.73205080757
          #1+(2/root3) = 2.15470053838
          circleTriangle(n-1, l/2.15470053838, pen)
          pen.circle(l/2.15470053838)
          pen.left(60)
          pen.up()
          pen.forward(l*1.73205080757)
          pen.down()
          pen.left(60)
     #endfor
          
     pen.circle(l)
#end
     



def circle3(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     circle3(n-1, l/1.5, pen)
     pen.circle(l/3)
     pen.left(90)
     pen.up()
     pen.forward(l)
     pen.down()
     pen.left(90)
     pen.circle(l/6)
     pen.right(90)
     pen.up()
     pen.backward(l/3)
     pen.down()
     pen.right(90)
     circle3(n-1, l/3, pen)
     pen.left(90)
     pen.up()
     pen.backward(l/1.5)
     pen.down()
     pen.right(90)
#end
     
# vvv not in use vvv

     
def carpet(n, l, pen):
    if n==0 or l<2 :
        return
    #endif
    carpet(n-1, l/3, pen)
    for i in range(3):
        pen.forward(l/3)
        carpet(n-1, l/3, pen)
        pen.forward(l/3)
        carpet(n-1, l/3, pen)
        pen.forward(l/3)
        pen.left(90)
    pen.forward(l/3)
    carpet(n-1, l/3, pen)
    pen.forward(l/1.5)
    pen.left(90)
    pen.forward(l/3)
    pen.left(90)
    pen.up()
    pen.forward(l/3)
    pen.down()
    pen.begin_fill()
    for i in range(4):
        pen.forward(l/3)
        pen.right(90)
    #endfor
    pen.end_fill()
    pen.up()
    pen.backward(l/3)
    pen.right(90)
    pen.backward(l/3)
    pen.down()
    
#end


def carpet3(n, l, pen):
    if n==0 or l<2 :
        return
    #endif
    carpet3(n-1, l/3, pen)
    pen.up()
    pen.forward(l/3)
    pen.down()
    carpet3(n-1, l/3, pen)
    pen.up()
    pen.forward(l/3)
    pen.down()
    carpet3(n-1, l/3, pen)
    pen.up()
    pen.forward(l/3)
    pen.left(90)
    pen.forward(l/3)
    pen.down()
    carpet3(n-1, l/3, pen)
    pen.up()
    pen.forward(l/3)
    pen.down()
    carpet3(n-1, l/3, pen)
    pen.up()
    pen.forward(l/3)
    pen.left(90)
    pen.forward(l/3)
    pen.down()
    carpet3(n-1, l/3, pen)
    pen.up()
    pen.forward(l/3)
    pen.down()
    carpet3(n-1, l/3, pen)
    pen.up()
    pen.forward(l/3)
    pen.left(90)
    pen.forward(l/3)
    pen.down()
    carpet3(n-1, l/3, pen)
    pen.up()
    pen.left(90)
    pen.forward(l/3)
    pen.down()
    pen.begin_fill()
    pen.forward(l/3)
    pen.right(90)
    pen.forward(l/3)
    pen.right(90)
    pen.forward(l/3)
    pen.right(90)
    pen.forward(l/3)
    pen.end_fill()
    pen.up()
    pen.left(90)
    pen.forward(l/3)
    pen.left(90)
    pen.forward(l/1.5)
    pen.left(90)
    pen.down()
    
def c(n, l, pen):
     if n==0:
          pen.forward(l)
          return
     c(n-1, l, pen)
     pen.right(90)
     c(n-1, l, pen)
     pen.left(90)


def spiral(n, l, pen):
     if n==0 or l<2 :
          return
     pen.forward(l)
     pen.right(119)
     spiral(n-1, l*0.98, pen)



def bentTree(n, l, pen):
     if n==0 or l<2:
          return
     for i in range(4):
          pen.forward(l)
          pen.left(90)
     pen.left(90)
     pen.forward(l)
     pen.right(60)
     bentTree(n-1, l*0.86602540378, pen)
     pen.forward(l*0.86602540378)
     pen.right(90)
     bentTree(n-1, l/2, pen)
     for i in range(4):
          pen.forward(l/2)
          pen.left(90)
     pen.left(180)
     for i in range(3):
          pen.forward(l*0.86602540378)
          pen.left(90)
     pen.right(120)
     pen.forward(l)
     pen.left(90)
     

def all(pen):
     pen.up()
     pen.goto(-500, -450)
     pen.down()
     pen.left(90)
     pen.color("sea green")
     tree(5, 150, pen)
     pen.up()
     pen.goto(-250, -450)
     pen.down()
     pen.color("spring green")
     dandelion(5, 150, pen)
     pen.up()
     pen.goto(-500, -100)
     pen.down()
     pen.right(90)
     pen.color("green")
     fern(4, 50, pen)
     pen.up()
     pen.goto(-50, -200)
     pen.down()
     flake(4, 125, pen)
     pen.up()
     pen.goto(-150, -450)
     pen.down()
     pen.color("royal blue")
     antiflake(4, 175, pen)
     pen.up()
     pen.goto(50, -450)
     pen.down()
     pen.color("red")
     gasket(5, 175, pen)
     pen.up()
     pen.goto(250, -450)
     pen.down()
     pen.color("cyan")
     pentaplex(4, 200, pen)
     pen.up()
     pen.goto(415, -450)
     pen.down()
     pen.color("dark orange")
     square(4, 200, pen)
     pen.up()
     pen.goto(450, -100)
     pen.down()
     pen.color("CadetBlue1")
     htree(5, 100, pen)
     pen.up()
     pen.goto(175, -200)
     pen.down()
     pen.color("white")
     flake2(5, 75, pen)
     pen.up()
     pen.goto(-100, 75)
     pen.down()
     pen.right(90)
     pen.color("dark olive green")
     halfCircle(6, 250, pen)
     pen.up()
     pen.goto(-200, -100)
     pen.down()
     pen.color("magenta")
     circle3(5, 250, pen)
     pen.up()
     pen.goto(-450, 150)
     pen.down()
     pen.color("yellow")
     circleCross(50, 60, pen)
     pen.up()
     pen.goto(350, 25)
     pen.down()
     pen.left(90)
     pen.color("salmon")
     circleTriangle(5, 125, pen)
     pen.up()
     pen.goto(350, 300)
     pen.down()
     pen.color("khaki4")
     carpet3(4, 200, pen)
     pen.up()
     pen.goto(200, 340)
     pen.down()
     pen.right(180)
     pen.color("blue")
     c(10, 4, pen)
     pen.right(180)
     pen.up()
     pen.goto(-400, 300)
     pen.down()
     pen.color("red")
     bentTree(6, 50, pen)
     pen.up()
     pen.goto(-200, 400)
     pen.down()
     pen.color("black")
     spiral(150, 250, pen)
     














     
