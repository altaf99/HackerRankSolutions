#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'shortestSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


from collections import defaultdict 

def shortestSubstring(s): 
    str_len = len(s)  
    dist_count = len(set([x for x in s])) 
    count = 0
    start = 0
    start_index = -1
    min_len = 9999999999

    curr_count = defaultdict(lambda: 0) 

    for j in range(str_len): 
        curr_count[s[j]] += 1

        if curr_count[s[j]] == 1: 
            count += 1

        if count == dist_count: 
            while curr_count[s[start]] > 1: 
                if curr_count[s[start]] > 1: 
                    curr_count[s[start]] -= 1
                start += 1

            len_window = j - start + 1
            if min_len > len_window: 
                min_len = len_window 
                start_index = start 

    return len(s[start_index: start_index + min_len])

if __name__ == '__main__':