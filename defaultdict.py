from collections import defaultdict

#  A has n words which might repeat.
# B has m words .

# n and m are integers.
# for each m (word in B) check wheteher it has appeared in A or not.
# Task is to print the indices of each occuracance of m in group A if not then -1.


n,m = map(int,input().split())

A  = defaultdict(list)  
''' This means that when we access a key in A that doesn't exist,
 it will automatically create the key and assign it an 
 empty list as the value(in this case a list otherwise whatever value you want).
'''



for i in range(n):
   A[input()].append(i+1)  # we want normal index values not from 0
   
   
   
for i in range(m):
    k = input()
    if k in A :
        print(*(A[k]))   # star to unpack the list
    else :
        print(-1)
        
        
        
        
        
'''
Sample Input

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
Sample Output

1 2 4
3 5
Explanation

'a' appeared  times in positions 1 ,2 and 4.
'b' appeared  times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group , you would print -1 .

'''
