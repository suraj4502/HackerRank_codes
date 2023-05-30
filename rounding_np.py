import numpy as np
np.set_printoptions(legacy ='1.13')

arr = np.array(input().split(),float)
print(np.floor(arr))   # if 1.6 then 1
print(np.ceil(arr))    # if 1.2 then 2
print(np.rint(arr))    # if 1.2 then 1 and if 1.6 thrn 2


'''
Sample Input

1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Sample Output

[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

'''
