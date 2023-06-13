from itertools import groupby
S = input()

result = groupby(S)

for key,group in result:
    print(f"({len(list(group))}, {key})", end=" ")


''''
Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)

'''
