#!/bin/python3

import math
import os
import random
import re
import sys


import math
def calculate(no1, no2):
    if(no1 == no2):
        return 0
    half = math.ceil(no1/2.0)
    if(no2 >= half):
        return 1
    return 1+calculate(math.ceil(no1/2.0), no2)

def minMoves(h, w, h1, w1):
    # Write your code here
    count = 0
    count = calculate(h,h1)
    count += calculate(w,w1)
    return count
if __name__ == '__main__':