import numpy as np
from tqdm import tqdm
from time import sleep
import random

class Network:
    def __init__(self, data, passes, learnRate):
        self.data = data
        self.dataXs = []
        self.dataX = np.zeros(len(self.data))
        self.dataY = np.zeros(len(self.data))
        self.coef = np.random.randint(-200,200,len(data))
        #self.coef = np.random.randn(2)
        #self.coef[0] = random.randint(-600,600)

        self.passes = passes
        for i in range(len(self.data)):
            self.dataX = np.zeros(len(self.data))
            self.dataX.put(0, 1)
            for j in range(1, len(self.data)):
                self.dataX.put(j, self.data[i][0]**j)
            self.dataXs.append(self.dataX)
            self.dataY.put(i, self.data[i][1])
        self.passes = passes
        self.learnRate = learnRate

        self.graph = []

        
        
        
        
    def train(self):
        self.losses = []
        self.deltaLoss = 5
        self.prevLoss = 0
        for i in tqdm(range(self.passes)):
            self.grad = np.zeros(len(self.data))
            self.deltaYHat = np.zeros(len(self.data))
            self.dataYHat = np.zeros(len(self.data))
            self.lossVector = np.zeros(len(self.data))
            self.forwardPass()
            self.backPass()
            self.tweak()
            print(self.loss)



    
    def forwardPass(self):
        for i in range(len(self.data)):
            self.dataYHat.put(i, np.dot(self.dataXs[i],self.coef))
            self.deltaYHat.put(i, self.dataYHat[i]-self.dataY[i])
            self.lossVector.put(i, self.deltaYHat[i]**2)
        self.loss = np.sum(self.lossVector)
            
    
    def backPass(self):
        dotVector = np.zeros(len(self.data))
        
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                dotVector.put(i, self.dataXs[j][1] ** i)
            self.grad.put(i, 2* np.dot(self.dataYHat, dotVector))
    
    def tweak(self):
        mag = np.linalg.norm(self.grad)
        self.coef = self.coef - self.learnRate * self.grad
    


