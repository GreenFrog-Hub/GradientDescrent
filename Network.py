import numpy as np
from tqdm import tqdm
from time import sleep
class Network:
    def __init__(self, data):
        self.data = data
        self.learnRate = 0.0000000001
        self.passes = 50
        self.coef = np.random.randn(len(self.data))
        self.allCoef = []
        self.allCoef.append(self.coef)
        self.loss = []
        self.totalLoss = 1000000
        print('')

        
        
        
        
    def train(self):
        for loops in range(self.passes):
            self.grad = []
            self.calcY = 0
            self.delatY = []
            for i in range(0,len(self.data)):
                self.grad.append(0)
                self.delatY.append(0)
            self.totalLoss = 0
            self.forwardPass()
            self.backPass()
            #print(self.totalLoss)
            self.tweak()
            self.allCoef.append(self.coef)
            #print('(',self.allCoef[loops][0],',',self.allCoef[loops][1],',',self.loss[loops],')')
            #print(self.coef)
            #print(self.totalLoss)
        #print(self.totalLoss)
    
    def forwardPass(self):
        for i in range(0,len(self.data)):
            self.calcY = 0
            for j in range(0,len(self.data)):
                self.calcY += self.coef[j] * (self.data[i][0]**j)
            self.delatY[i] = (self.calcY - self.data[i][1])
            self.totalLoss += (self.calcY - self.data[i][1])**2
            self.loss.append(self.totalLoss)
            
    
    def backPass(self):
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                self.grad[j] += 2*self.delatY[i]*(self.data[i][0]**j)
    
    def tweak(self):
        for i in range(0,len(self.coef)):
            self.coef[i] = self.coef[i] - self.learnRate * self.grad[i]
    


