
"""
given this input 'Sorting1234' how can i get this output 'ginortS1324'

"""


#Taking Input
S = input()

# Seperating strs and nums
str_ =[]
num = []
for letter in S:
    if letter.isalpha():
        str_.append(letter)
    elif letter.isnumeric():
        num.append(letter)
        

# Seperating lower and upper chars
lower =[]
big =[]
num = sorted(num)

for i in str_:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        big.append(i)
       
# Seperating even and odd nums
even =[]  
odd  =[]    
for i in num:
    if (int(i) %2) ==0:
        even.append(i)
    else :
        odd.append(i)
        
# finally adding all
final = []
for i in sorted(lower),sorted(big), sorted(odd),sorted(even):
    final.append(i)
    

final_ = sum(final, [])
print(''.join(final_))
