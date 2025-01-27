import turtle 
import Network2
import numpy
from tqdm import tqdm


import numpy as np

NoPoints = 2
losses = []
deltaLosses = []
coef = []
learningRates= []
exitConditions = []
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


# def train():
#     for i in tqdm(range(0,1)):
#       for j in tqdm(range(0,50)):
#         bob = Network2.Network(points, 5000, 0.0000001)
#         bob.train()
#         #losses.append(bob.totalLoss)
#         coef.append(bob.coef)
#         # deltaLosses.append(bob.deltaLoss)
#         # learningRates.append(bob.learnRate)
#         # exitConditions.append(bob.exitCondition)
#     # for i in range(len(exitConditions)-1):
#     #   if exitConditions[i] == 0:
#     #     print("found:", i)
#     # print(min(losses))
#     print(coef[losses.index(min(losses))])
#     # print(deltaLosses[losses.index(min(losses))])
#     # print(learningRates[losses.index(min(losses))])
#     # count = 0
#     plotGraph(coef[losses.index(min(losses))])


def train():
  bob = Network2.Network(points, 500000, 0.00005)
  bob.train()
  print(bob.loss)
  print(bob.coef)
  plotGraph(bob.coef)
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