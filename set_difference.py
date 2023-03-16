# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
M = list(map(int,input().split()))
m = set(M)
b = int(input())
N = list(map(int,input().split()))
n = set(N)

diffs =[]

diffs.append(list(m.difference(n)) )# Values which exist in m but not in n (only in m not in n)

diffs.append(list(n.difference(m)))

final =[element for row in diffs for element in row]

for i in sorted(final):
    print(i)
    
    
    
    
"""
STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12} 

Output :
5
9
11
12


>> a = {2, 4, 5, 9}
>> b = {2, 4, 11, 12}
>> a.union(b) # Values which exist in a or b
{2, 4, 5, 9, 11, 12}
>> a.intersection(b) # Values which exist in a and b
{2, 4}
>> a.difference(b) # Values which exist in a but not in b
{9, 5}

"""
