# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n  = int(input())
dic = defaultdict(int)

for i in range(n):
    dic[input()] += 1
    
    
print(len(dic))
print(*(dic.values()))


'''
Sample Input
4
bcdef
abcdefg
bcde
bcdef


Sample Output
3
2 1 1
Explanation

There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions.
The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.


'''
