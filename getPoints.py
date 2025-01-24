import turtle 
import Network
import numpy

global points
NoPoints = 2
def drawAxis():
  turtle.forward(1000)
  turtle.backward(2000)
  turtle.forward(1000)
  turtle.left(90)
  turtle.forward(1000)
  turtle.backward(2000)
  turtle.forward(1000)
  turtle.right(90)
  
def plotGraph(coefficients):
  turtle.pencolor("red")
  for i in range(-610,610):
    yCoord = 0
    for j in range(len(coefficients)-1,-1,-1):
      yCoord += coefficients[j]*i**j
    
    turtle.goto(i,yCoord)
    turtle.pendown()
    



def train():
    coefficients = numpy.zeros(NoPoints)
    bob = Network.Network(points)
    bob.train
    coefficients = bob.coef
    plotGraph(coefficients)
# screen object 
wn = turtle.Screen() 
  
# method to perform action 
def fxn(x, y): 
  points.append([x, y])
  turtle.goto(x, y) 
  turtle.stamp()
  turtle.write(str(x)+","+str(y)) 
  if len(points) == NoPoints:
    train()
  
# onclick action
points = []
turtle.speed(0)
turtle.screensize(canvwidth=400, canvheight=400, 
                  bg="white")
drawAxis()
turtle.penup()
turtle.shape("circle") 
turtle.shapesize(0.5, 0.5, 0.5)
wn.onclick(fxn)
wn.mainloop()
print(points)