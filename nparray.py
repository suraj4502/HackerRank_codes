def arrays(arr):
    a = numpy.array(arr,float)
    return a[::-1]
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

'''
Sample Input
1 2 3 4 -8 -10


Sample Output
[-10.  -8.   4.   3.   2.   1.]
'''
