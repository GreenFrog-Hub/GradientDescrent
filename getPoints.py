import turtle 
from Network2 import Network
import numpy
from tqdm import tqdm
import matplotlib.pyplot as plt

import numpy as np
NoPoints = 4
losses = []
deltaLosses = []
coef = []
learningRates= []
exitConditions = []
backUpPoint = [[-100/1000,-100/1000],[100/1000,100/1000],[-100/1000,100/1000],[100/1000,-100/1000]]
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
  plotPoints = np.arange(-0.610,0.610,0.001)
  turtle.pencolor("red")
  for i in tqdm(plotPoints):
    yCoord = 0
    for j in range(len(coefficients)-1,-1,-1):
      yCoord += (coefficients[j])*(i**j)
    turtle.goto(i*1000,yCoord*1000)
    turtle.pendown()

def train():
  bob = Network(points, 1000000, 0.1)
  startGuess = []
  startGuess = bob.coef
  bob.train()
  print(bob.loss)
  print(bob.coef)
  plt.plot(bob.iteration, bob.losses, label = str(startGuess))
  leg = plt.legend(loc='upper center')
  plt.ylim(0,5* 10**4)
  plt.show()
  plotGraph(bob.coef)
# screen object 

wn = turtle.Screen() 

# method to perform action 
def fxn(x, y): 
  points.append([x/1000, y/1000])
  turtle.goto(x, y) 
  turtle.stamp()
  turtle.write(str(x)+","+str(y)) 
  if len(points) == NoPoints:
    train()
  

# onclick action
points = []
turtle.speed(0)

drawAxis()
turtle.penup()
turtle.shape("circle") 
turtle.shapesize(0.5, 0.5, 0.5)
wn.onclick(fxn)
wn.mainloop()
print(points)
