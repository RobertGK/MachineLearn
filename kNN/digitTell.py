# -*- coding: utf-8 -*-
"""
Spyder Editor

this file is to tell the digit by knn
"""
import numpy as np
import os
import operator


def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistance = sqDiffMat.sum(axis = 1)
    distance = sqDistance**0.5
    sortedDistanceindex = distance.argsort()
    classCount = {}
    for i in range(k):
        votelabel = labels[sortedDistanceindex[i]]
        classCount[votelabel] = classCount.get(votelabel,0) +1
    sortedClassCount = sorted(classCount.items(),
                              key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]
    
    
def img2vector(filename):
    returnVect = np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

def handWritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir("trainingDigits")
    m = len(trainingFileList)
    trainingMat = np.zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split(".")[0]
        classNumStr = int(fileStr.split("_")[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector("trainingDigits/%s"% fileNameStr)
    testFileList = os.listdir("testDigits")
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split(".")[0]
        classNumStr = int(fileStr.split("_")[0])
        vectorUnderTest = img2vector("testDigits/%s" %fileNameStr)
        classifierResult = classify0(vectorUnderTest,\
                                      trainingMat,hwLabels,10)
        print("the classfier came back with:%d,the real answer is :%d"\
              %(classifierResult,classNumStr))
        if (classifierResult != classNumStr):errorCount += 1.0
    print("\nthe total number of error is :{}".format(errorCount))
    print("\nthe total error rate is :{}".format(errorCount/float(mTest)))
        