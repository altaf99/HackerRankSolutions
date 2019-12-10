#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numberOfWays' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY cases as parameter.
#

def numberOfWays(cases):
    # Write your code here
    res =[]
    for case in cases:
        N = case[0]
        M = case[1]

        dim = min(N,M)
        S=0

        for i in range(1,dim+1):
            S+=(N-i+1) * (M-i+1)
        res.append(S)
    return res

if __name__ == '__main__':