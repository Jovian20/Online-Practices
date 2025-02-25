#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input()
    char_counter = Counter(s.lower())
    most_common = sorted(char_counter.items(), key=lambda x: (-x[1], x[0]))[:3]
    
    for char, count in most_common:
        print(f"{char} {count}")
