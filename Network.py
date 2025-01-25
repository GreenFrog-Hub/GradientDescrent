import numpy as np
from tqdm import tqdm
from time import sleep
import matplotlib
class Network:
    def __init__(self, data, passes, learnRate):
        self.data = data
        self.dataX = np.zeros(len(self.data))
        self.dataY = np.zeros(len(self.data))
        self.coef = np.random.randint(-300,300,len(data))
        self.passes = passes
        for i in range(len(self.data)):
            self.dataX.put(i, self.data[i][0])
            self.dataY.put(i, self.data[i][1])
        self.passes = passes
        self.learnRate = learnRate

        self.graph = []

        
        
        
        
    def train(self):
        self.losses = []
        self.deltaLoss = 5
        self.prevLoss = 0
        while self.deltaLoss > 0.000001 and self.deltaLoss < 10000:
            self.grad = np.zeros(len(self.data))
            self.delatY = np.zeros(len(self.data))
            self.dataYHat = np.zeros(len(self.data))
            self.forwardPass()
            self.backPass()
            self.tweak()
            self.deltaLoss = self.totalLoss - self.prevLoss
            self.prevLoss = self.totalLoss
        self.MinLoss = self.totalLoss
    
    def forwardPass(self):
        for i in range(len(self.dataX)):
            self.yHat = np.dot(self.coef, self.dataX[i])
            self.dataYHat.put(i, self.yHat)
        self.delatY = self.dataYHat- self.dataY
        self.totalLoss = np.sum(self.delatY**2)
        
            
    
    def backPass(self):
        self.grad = 2*self.delatY * self.dataX
    
    def tweak(self):
        mag = np.linalg.norm(self.grad)
        self.coef = self.coef - self.learnRate * np.sqrt(mag)*self.grad
    


