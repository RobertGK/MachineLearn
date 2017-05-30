# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:08:26 2017

@author: Robert
"""
import numpy as np

class ConLayer(object):
    def __init__(self,input_width,input_height,channel_number,filter_width,filter_height,
                 filter_number,zero_padding,stride,activator,learining_rate):
        self.input_width = input_width
        self.input_height = input_height
        self.channel_number = channel_number
        self.filter_width = filter_width
        self.filter_height = filter_height
        self.filter_number = filter_number
        self.zero_padding = zero_padding
        self.stride = stride
        self.output_width = ConLayer.calculate_output_size(self.input_width,filter_width,zero_padding,stride)
        self.output_height = ConLayer.calculate_output_size(self.input_height,filter_height,zero_padding,stride)
        self.output_array = np.zeros(self.filter_number,self.output_height,self.output_width)
        self.filter = []
        for i in range(filter_number):
            self.filter.append(Filter(filter_width,filter_height,self.channel_number))
        self.activator = activator
        self.learning_rate = learining_rate
        

    @staticmethod
    def calculate_output_size(input_size,filter_size,zero_padding,stride):
        return (input_size - filter_size + 2*zero_padding/stride +1)
        
    def forward(self,input_array):
        self.input_array = input_array
        self.padded_input_array = padding(input_aray,self.zeros_padding)
        for f in range(self.filter_number):
            filter = self.filters[f]
            conv(self.padded_input_array,filter.get_weights(),self.output_array[f],self.stride,filter.get_biases())
        element_wise_op(self.output_array,self.activator.forward)
        

    def element_wise_op(aray,op):
        for i in np.nditer(array,op_flags = ["readwrite"]):
            i[...] = op(i)
            
    def conv(input_array,kernel_array,output_array,stride,biases):
        channel_number = input_array.ndim
        output_width = output_array.shape[1]
        output_height = output_arary.shape[0]
        kernel_width = kernel_array.shape[-1]
        kennel_height = kernel_array.shape[-2]
        for i in range(output_width):
            for j in range(out_width):
                output_array[i][j] = (
                get_patch(input_array,i,j,kernel_width,kennel_height,stride)*
                kernel_array).sum() + biases

    def padding(input_array,zp):
        if zp ==0:
            return input_array
        else:
            if input_array.ndim ==3:
                input_width = input_array.shape[2]
                input_height = inout_array.shape[1]
                input_depth = input_array.shape[0]
                padded_array = np.zeros((input_depth,
                                         input_height + 2*zp,
                                         input_width + 2*zp))
                padded_array[:,zp:zp+input_height,zp:zp+input_width] = input_array
                return padded_array
            elif input_array.ndim == 2:
                input_width  = input_array.shape[1]
                input_height = input_array.shape[0]
                padded_array = np.zeros((input_height + 2*zp,
                                         input_width + 2*zp))
                padded_array[zp:zp+input_height,zp:zp+input_width] = input_array
                return padded_array
        
    def bp_sensitivity_map(self,sensitivity_array,activator):
        expanded_array = self.expand_sensitivity_map(sensitivity_array)
        expand_width = expand_array.shape[2]
        zp = (self.input_width + self.filter_width -1-expand_width)/2
        padded_array = padding(expanded_array,zp)
        
        self.delta_array = self.creat_delta_array()
        for f in range(self.filter_number):
            filter = self.filters[f]
            flipped_weights = np.array(map(lambda i:np.rot90(i,2),delta_array[d],1,0))
        delta_array = self.create_delta_array()
        for d in range(delta_array.shape[0]):
            conv(padded_array[f],flipped_weights[d],delta_array[d],1,0)
            self.delta_array += delta_array
            
        deritive_array = np.array(self.input_array)
        element_wise_op(derivative_array,activator.backward)
        self.delta_array *= derivativr_array
        
    def expand_sensitivity_map(self.sensitivity_array):
        depth = sensitivity_array.shape[0]
        expanded_width  = (self.input_width - self.filter_width +2*self.zero_padding +1)
        expended_height = (self.input_height - self.filter_height +2*self.zero_padding +1)
        expanded_array = np.zeros((depth,expanded_height,expanded_width))
        
        for i in range(self.output_height):
            for j in range(self.output_width):
                i_pos = i*self.stride
                j_pos = j*self.stride
                expand_array[:,i_pos,j_pos] = sensitivity_array[:,i,j]
        return expand_array
        
    def create_delta_array(self):
        return np.zeros((self.channel_number,self,input_height,self.input_width))
        
    def bp_gradient(self,sensitivity):
        expanded_array = self.expand_sensitivity_map(sensitivity_array)
        for f in range(self.filter_number):
            for d in range(filter.weights.shape[0]):
                conv(self.padded_input_array[d],expanded_array[f],filter.weights_grad[d],1,0)
            filter.biases_grad = expanded_array[f].sum()
            
    def update(self):
        for filter in self.filters:
            filter.update(self.learning_rate)
        
        
        
class Filter(object):
    def __init__(self,width,height,depth):
        self.weights = np.random.uniform(-1e-4,1e-4,(depth,height,width))
        self.biases = 0
        self.weights_grad = np.zeros(self.weights.shape)
        self.biases_grad = 0
        
    def __repr__(self):
        return "filter weights:%n%s\nbiases:%s"(repr(self.weights),repr(self.biases))
        
    def get_weights(self):
        return self.weights
    
    def get_biases(self):
        return self.biases
        
    def update(self,learning_rate):
        self.weight -= learning_rate * self.weights_grad
        self.biases -= learning_rate * self.biases_grad
        
    
class ReluActivator(object):
    def forward(self,weighted_input):
        return max(0,weighted_input)
        
    def backword(self,output):
        return 1 if output > 0 else 0
        


        
        
        
        
        
        
        
        
        
        
        
        
        