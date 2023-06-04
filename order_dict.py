# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict,defaultdict
num_of_items = int(input())

dic = defaultdict(int)

for _ in range(num_of_items):
    item, price = input().rsplit(" ",1)
    dic[item] += int(price)
    
dico = OrderedDict(dic)
for key,value in dico.items():
    print(key,value)
    
    
    
 '''
 Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30


Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

'''
