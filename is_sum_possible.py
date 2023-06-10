'''
1. Could we sum it?
Let Ankur has given a large weight W, and a list of smaller weights in an array. He needs to write a
code in order to find "can we form weight W or not, using smaller weights". He only knows dp
solution. Could you write a code solution for him without using dp.

Constraint: - list size <= 12

Sample Input1: -
W = 15
list = {4, 3, 5, 6, 4}
Output: - True
Explanation: -
15 =4 + 5 + 6.

Sample Input2: -
W = 9
list = {4, 1, 3, 7}
Output: - False.
Explanation: - There is no way to sum up 7.

'''
# solution :
from itertools import combinations as cm



def is_sum_possible(W: int, weights: list) -> bool:
    for i in range(1, len(weights) + 1):
        combinations = cm(weights, i)   # this will generate combinations like if i =2, then (4,5),(4,5),(4,6) etc
        for combination in combinations:
            if sum(combination) == W:
                return True
    return False
        
                
    
print(is_sum_possible(W=15,weights=[4, 3, 5, 6, 4]))
print(is_sum_possible(W=9,weights=[4, 1, 3, 7]))
print(is_sum_possible(W=10,weights=[4, 1, 3, 7]))
print(is_sum_possible(W=16,weights=[4, 1, 3, 7]))

''' : output :
True
False
True
False
'''
