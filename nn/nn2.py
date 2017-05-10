# -*- coding: utf-8 -*-
"""
Created on Wed May 10 19:25:37 2017

@author: Robert

i find it's hard for me to write a nn work today,this is just a copy
"""
import numpy as np

def logistic(x):
    return 1 / (1 + np.exp(x))
    
def logistic_derivate(x):
    return logistic(x)*(1 - logistic(x))
    
class Neron:
    def __init__(self,len_input):
        self.weights = np.random.random(len_input)*0.1
        self.input = np.ones(len_input)
        self.output = 1
        self.deltas_item = 0
        self.last_weight_add = 0
        
    def calc_out_put(self,x):
        self.input = x
        self.output = logistic(np.dot(self.weight.T,self.input))
        
    def get_back_weight(self):
        return self.weight * self.deltas_item
        
    def update_weight(self,target = 0,back_weight = 0,learning_rate = 0.1,layer = "OUTPUT"):
        if layer == 'OUTPUT':
            self.deltas_item = (target - self.output)*logistic_derivate(self.output)
        elif layer == "HIDDEN":
            self.deltas_item = back_weight *logistic_derivate(self.output)
        
        weight_add = self.input * self.deltas_item * learning_rate + 0.9 *self.last_weight_add
        self.weights += weight_add
        self.last_weight_add = weight_add
        
        
        
        