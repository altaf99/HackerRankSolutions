#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeChecker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY l
#  3. INTEGER_ARRAY r
#  4. INTEGER_ARRAY k
#
NO_OF_CHARS = 256
 
def pal_poss(st) : 
    count = [0] * (NO_OF_CHARS) 
    for i in range( 0, len(st)) : 
        count[ord(st[i])] = count[ord(st[i])] + 1

    odd = 0
      
    for i in range(0, NO_OF_CHARS ) : 
        if (count[i] & 1) : 
            odd = odd + 1
  
        if (odd > 1) : 
            return False
    return True
  
def palindromeChecker(s, l, r, k):
    # Write your code here
    # print(s,l,r,k)
    res=[]
    for i in range(len(l)):
        print(s[l[i]:r[i]+1])
        ispal = pal_poss(s[l[i]:r[i]+1])
        print(ispal)
        if(ispal == True and k[i] == 0):
            res.append("0")
        else:
            res.append("1")
    # print(res)
    return "".join(res)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    l_count = int(input().strip())

    l = []

    for _ in range(l_count):
        l_item = int(input().strip())
        l.append(l_item)

    r_count = int(input().strip())

    r = []

    for _ in range(r_count):
        r_item = int(input().strip())
        r.append(r_item)

    k_count = int(input().strip())

    k = []

    for _ in range(k_count):
        k_item = int(input().strip())
        k.append(k_item)

    result = palindromeChecker(s, l, r, k)

    fptr.write(result + '\n')

    fptr.close()
