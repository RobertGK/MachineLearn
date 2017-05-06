# -*- coding: utf-8 -*-
"""
Created on Tue May  2 15:09:22 2017

@author: Robert

this is for nn test
"""

import math
import numpy as np


def sigmaoid(x):
    return 1.0/(1.0+math.exp(-x))
    
def sigmoid_derivate(x):
    return x*(1-x)