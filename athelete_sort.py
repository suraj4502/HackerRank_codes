
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    

sorted_data = sorted(arr,key=lambda x: x[k]) # lamda function returns the kth element of arr



for row in sorted_data:
    print(*row)
    
    
    
    
"""
input :
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

output: 
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
"""
