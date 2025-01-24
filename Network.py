import numpy as np

class Network:
    def __init__(self, data):
        self.data = data
        self.learnRate = -0.01
        self.passes = 50
        self.coef = np.random.randn(len(self.data))

        
        
        
        
    def train(self):
        for loops in range(0, self.passes):
            self.loss = np.array(len(self.data))
            self.grad = np.array(len(self.data))
            self.totalLoss = 0
            self.forwardPass
            self.backPass
            self.tweak

    
    def forwardPass(self):
        for i in range(0,len(self.data)-1):
            for j in range(0,len(self.data)-1):
                self.loss[j] = (self.data[i,0] - self.coef[j] * self.data[i,0]**j)^2
            self.totalLoss += sum(self.loss)
    
    def backPass(self):
        for i in range(0,len(self.data)-1):
            for j in range(0,len(self.data)-1):
                self.grad[j] += -2*self.data[i,1]*self.data[i,0]**j
    
    def tweak(self):
        for i in range(0,len(self.coef)):
            self.coef[i] += self.learnRate * self.grad[i]
    
    def returnCoef(self):
        return self.coef

