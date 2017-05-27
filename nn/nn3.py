# -*- coding: utf-8 -*-
"""
Created on Sat May 27 21:04:32 2017

@author: Robert
"""

import numpy as np

def sigmond(x):
    return 1/(1+np.exp(-x))
    
def derivative_sigmond(x):
    return x*(1-x)
    

class Neuron:
    def __init__(self,len_input):
        self.weights = np.random.random(len_input)*0.1
        self.input = np.ones(len_input)
        self.output = 1
        self.deltas_item = 0
        self.last_weight_add = 0
    
    def calc_output(self,x):
        self.input = x
        self.output = sigmond(np.dot(self.weights.T,self.input))
        return self.output
        
    def get_back_weight(self):
        return self.weight * self.deltas_item
        
    def update_weight(self,target = 0,back_weight = 0,learning_rate = 0.1,layer = "OUTPUT"):
        if layer == "OUTPUT":
            self.deltas_item = (target - self.output)*derivative_sigmond(self.output)
        elif layer == "HIDDEN":
            self.deltas_item = back_weight * derivative_sigmond(self.output)
            
        weight_add = self.input * self.deltas_item * learning_rate + 0.9 * self.last_weight_add
        self.weights += weight_add
        self.last_weight_add = weight_add
        
class NetLayer:
    
    def __init__(self.len_node,in_count):
        self.neurons = [Neuron(in_count) for _ in range(len_node)]
        self.next_layer = None
        
    def calc_output(self,x):
        output = np.array([node.calc_output(x) for node in self.neurons])
        if self.next_layer is not None:
            return self.next_layer.calc_output(output)
        return output
    
    def get_back_weight(self):
        return sun(node.get_back_weight() for node in self.neurons)
        
    def update_weight(self,learning_rate,target):
        layer = "OUTPUT"
        back_weight = np.zeros(len(self.nerons))
        if self.next_layer = self.next_layer.update_weight(learning_rate,target):
            layer = "HIDDEN"
        for i,node in enumerate(self.neurons):
            target_item = 0 if len(target) <= i else target[i]
        node.update_weight(target = target_item,back_weight = back_weight[i],learning_rate = learning_rate,
                           layer = layer)
        return self.get_back_weight
        

        