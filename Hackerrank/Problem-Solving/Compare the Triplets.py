import math
import os
import random
import re
import sys



def compareTriplets(a, b):
    # Write your code here
    result = []
    alice_score = 0
    bob_score = 0
    
    for i in range(0, len(a)):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
        else:
            continue
    
    result.append(alice_score)
    result.append(bob_score)
    
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
