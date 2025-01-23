import turtle 

def drawAxis():
  turtle.forward(1000)
  turtle.backward(2000)
  turtle.forward(1000)
  turtle.left(90)
  turtle.forward(1000)
  turtle.backward(2000)
  turtle.forward(1000)
  turtle.right(90)
  

def exitprogram():
    wn.bye()
# screen object 
wn = turtle.Screen() 
  
# method to perform action 
def fxn(x, y): 
  points.append([x, y])
  turtle.goto(x, y) 
  turtle.stamp()
  turtle.write(str(x)+","+str(y)) 
  if len(points) == 6:
    exitprogram()
  
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