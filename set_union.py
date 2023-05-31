# Enter your code here. Read input from STDIN. Print output to STDOUT

eng_count = int(input())
eng = set(map(int,input().split()))

fre_count = int(input())
fre = set(map(int,input().split()))

union = eng.union(fre)

print(len(union))


'''
Sample Input
9
123456789
9
10 123 11 21 55 68

Sample Output
13


Explanation
Roll numbers of students who have at least one subscription:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21 and 55. Roll numbers: 1, 2, 3, 6 and 8 are in both
sets so they are only counted once.
Hence, the total is 13 students.

'''
