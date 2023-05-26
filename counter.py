from collections import Counter

num_of_shoes = int(input())
# print(num_of_shoes)

shoe_size_list = list(map(int,input().split()))
# print(shoe_size_list)

num_of_customers = int(input())
# print(num_of_customers)

shoe_count = Counter(shoe_size_list)
# print(shoe_count)
earned = 0

for _ in range(num_of_customers):
    size , price = map(int,input().split())
    if shoe_count[size] > 0:
        earned += price
        shoe_count[size] -= 1
        
print(earned)




'''
Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50


Sample Output

200
'''

# Print the amount of money earned
