import turtle 
import Network
import numpy
from tqdm import tqdm


import numpy as np

NoPoints = 6
losses = []
deltaLosses = []
coef = []
learningRates= []
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
  for i in tqdm(range(-610,610)):
    yCoord = 0
    for j in range(len(coefficients)-1,-1,-1):
      yCoord += coefficients[j]*(i**j)
    turtle.goto(i,yCoord)
    turtle.pendown()


def train():
    for i in tqdm(range(-18,0)):
      for j in tqdm(range(0,1000000)):
        bob = Network.Network(points, 50, 1*(10**(-(i))))
        bob.train()
        losses.append(bob.MinLoss)
        coef.append(bob.coef)
        deltaLosses.append(bob.deltaLoss)
        learningRates.append(bob.learnRate)
    print(min(losses))
    print(coef[losses.index(min(losses))])
    print(deltaLosses[losses.index(min(losses))])
    print(learningRates[losses.index(min(losses))])
    count = 0
    for i in tqdm(range(0,len(deltaLosses)-1)):
      if deltaLosses[i] < 1:
        count += 1
    print("Global minimums found = ",count,"/",len(deltaLosses))
    plotGraph(coef[losses.index(min(losses))])


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

drawAxis()
turtle.penup()
turtle.shape("circle") 
turtle.shapesize(0.5, 0.5, 0.5)
wn.onclick(fxn)
wn.mainloop()
print(points)