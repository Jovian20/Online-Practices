import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    # Write your code here
    first_val = 0
    second_val = 0
    
    for i in range(0, len(arr)):
        first_val += arr[i][i]
    for i in range(len(arr)):
        second_val += arr[i][len(arr) - i - 1]
        
    return abs(first_val - second_val)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
