# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:21:24 2017

@author: Robert

this file is to test logistics regress
"""
import numpy as np


def loadDataSet():
    dataMat  = []
    labelMat = []
    fr = open("testSet.txt")
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[0])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat
    
def sigmond(inX):
    return 1.0/(1+np.exp(-inX))
    

def gradAscent(dataMatIn,classLabels):
    dataMatrix = np.mat(dataMatIn)
    labelMat = np.mat(classLabels).transpose()
    m,n = np.shape(dataMatrix)
    alpha = 0.001
    maxCycle = 500
    weights = np.ones((n,1))
    for k in range(maxCycle):
        h = sigmond(dataMatrix*weights)
        error = (labelMat - h)
        weights = weights + alpha*dataMatrix.transpose()*error
    return weights
    
        