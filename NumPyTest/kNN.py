# -*- coding: utf-8 -*-
"""
this is for a file to matrix
"""

import numpy as np

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = np.zeros((numberOfLines,3))
    classLableVetor = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, : ] = listFromLine[0:3]
        classLableVetor.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLableVetor

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals,(m,1))
    normDataSet = normDataSet/(np.tile(ranges,(m,1)))
    return normDataSet,ranges,minVals


    