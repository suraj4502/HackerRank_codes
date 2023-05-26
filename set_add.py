num_of_stamps = int(input())
unique_count = set()
for _ in range(num_of_stamps):
    unique_count.add(input())
    
    
print(len(unique_count))




'''
Output the total number of distinct country stamps on a single line.

Sample Input

7
UK
China
USA
France
New Zealand
UK
France 


Sample Output

5
Explanation

UK and France repeat twice. Hence, the total number of distinct country stamps is  (five).

'''
