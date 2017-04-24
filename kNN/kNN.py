# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:55:00 2017

@author: RobertHOU
"""
import numpy as np
import operator
import os,sys

def createdataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0.1,0.1]])
    labels = ['A','A','B','B']
    return group,labels

    
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis = 1)
    distance = sqDistances**0.5
    sortedDistIndicies = distance.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]
    

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
    
# 下面的这串代码深刻的表现了numpy使用矩阵而不是你for循环的有优点，代码少！  
def autoNorm(dataSet) :
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals,(m,1))
    normDataSet = dataSet/ np.tile(ranges,(m,1))
    return normDataSet,ranges,minVals
     
def datingClassTest():
    hoRatio = 0.1
    datingDataMat,datingLabels = file2matrix("datingTestSet2.txt")
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],\
                                     datingLabels[numTestVecs:m],3)
        print("the classifier came back with:%d, the real answer is: %d"\
              %(classifierResult,int(datingLabels[i]))
#   try:
#       print("the total error rate is : %f"　%(errorCount/(float(numTestVecs))))
#   except Exception as ex:
#       print ("表达式为空，请检查") 
      
     
def img2vector(filename):
    returnVect = np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int[lineStr[j]]
    return returnVect
    
    
def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir("trainingDigits")
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest,\
                                     trainingMat,hwLabels,3)
        print("the classifier came back with:%d,the real answer is:d%"\
              %(classfierResult,classNumStr))
        if(classifierResult != classNumStr):errorCount += 1.0
    print("\nthe total number of errors is :%d"% errorCount)
    print("\nthe total error rate is : %f" % (errorCount/float(mTest)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    