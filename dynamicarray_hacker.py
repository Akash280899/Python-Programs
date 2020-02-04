#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    la=0
    l=[]
    l1=[]
    for i in range(len(queries)):
        if queries[i][0]==1:
            a = (queries[i][1]^la)%n
            if a==0:
                l.append(queries[i][2])
            elif a==1:
                l1.append(queries[i][2])
        elif queries[i][0]==2:
            a = (queries[i][1]^la)%n
            if a==1:
                
                if len(l1)==1:
                    la=l1[0]
                    return (l1[0])
                else:
                    return (l1[1])
            else:
                return (l[1])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
