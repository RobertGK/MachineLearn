# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:55:00 2017

@author: RobertHOU
"""
import numpy as np

def file2matrix(filename):
    fr = open(filename)
    arrayLines = fr.readlines()
    numberOfLines = len(arrayLines)
    returnMat = np.zeros((numberOfLines,3))
    classLableVector = []
    index = 0
    for line in arrayLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, : ] = listFromLine[0:3]
        classLableVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLableVector
    
    
