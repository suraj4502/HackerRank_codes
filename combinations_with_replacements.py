from itertools import combinations_with_replacement,combinations

S, k = input().split()

S = "".join(sorted(S))

result = combinations_with_replacement(S, int(k))

for i in result:
    print("".join(i))
    
    
 '''
 Sample Input
HACK 2

Sample Output
AC
AK
cc
CH
CK
KK
'''
