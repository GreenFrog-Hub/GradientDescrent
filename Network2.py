import numpy as np
from tqdm import tqdm
from time import sleep
import random
import turtle

class Network:
    def __init__(self, data, passes, learnRate):
        self.data = data
        self.dataXs = []
        self.dataX = np.zeros(len(self.data))
        self.dataY = np.zeros(len(self.data))
        self.coef = np.random.randn(len(self.data))

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
        
    def train(self):
        self.losses = np.zeros(self.passes)
        self.iteration = np.zeros(self.passes)
        for i in tqdm(range(self.passes)):
            self.grad = np.zeros(len(self.data))
            self.deltaYHat = np.zeros(len(self.data))
            self.dataYHat = np.zeros(len(self.data))
            self.lossVector = np.zeros(len(self.data))
            self.forwardPass()
            self.backPass()
            self.tweak()
            self.losses.put(i, self.loss*1000)
            self.iteration.put(i, i)
    
    def forwardPass(self):
        for i in range(len(self.data)):
            self.dataYHat.put(i, np.dot(self.dataXs[i],self.coef))
            self.deltaYHat.put(i, self.dataYHat[i]-self.dataY[i])
            self.lossVector.put(i, self.deltaYHat[i]**2)
        self.loss = np.sum(self.lossVector)         
    
    def backPass(self):
        for i in range(len(self.data)):
            yVector = np.zeros(len(self.data))
            for j in range(len(self.data)):
                yVector.put(j, self.deltaYHat[i])
            self.grad += 2*yVector*self.dataXs[i]
    
    def tweak(self):
        self.coef = self.coef - self.learnRate * self.grad
