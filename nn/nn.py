# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import numpy as np
import math

def resourseSet(dir):
    fileList = os.listdir(dir)
    labelListOrigal = []
    for fileName in fileList:
        fileLabel = fileName.split("_")[0]
        labelListOrigal.append(fileLabel)
    labelList = np.zeros((len(fileList), 10))
    for i in range(len(fileList)):
        labelList[i][int(labelListOrigal[i])] = 1
    fileNum = len(fileList)
    resourceList = np.zeros((fileNum,1024))
    for i in range(fileNum):
        file = open(dir + "/" + fileList[i])
        fileStore = file.readlines()
        k = len(fileStore)
        m = len(fileStore[0])
        for j in range(k):
            resourceList[i][j*m:(j+1)*m] = fileStore[j]
    return resourceList,labelList
    
##神经网络最终是要学习得到每层一个w的矩阵和一个b的矩阵，这里采用只有一层隐含网络
##故只需要设置两层w和两层d，分别设置为wh,wd,和bh，bd。

def sigmond(z):
    return 1.0/(1.0+np.exp(-z))
    
    
def cal(resourceList,wh,wd,bh,bd):
    zh = np.dot(resourceList,wh) 
    yh = sigmond(zh+bh)
    zd = np.dot(yh,wd)
    yd = sigmond(zd+bd)
    return yd
    
    
def loss(yd ,labelList):
    diff = yd - labelList
    diffNum = np.sum(diff**2)
    return diffNum
    
def execute():
    dir = "trainingDigits"
    wh = np.zeros((1024,20))
    wd = np.zeros((20,10))
    bh = np.zeros((1934,20))
    bd = np.zeros((1934,10))
    resourceList,labelList = resourseSet(dir)
    yd = cal(resourceList,wh,wd,bh,bd)
    lossNum = loss(yd ,labelList)
    return lossNum

    
    
    
    
    
    
        