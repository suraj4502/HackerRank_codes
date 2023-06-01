# A deque is a double-ended queue. It can be used to add or remove elements from both ends.


from collections import deque
num_of_operations = int(input())

d = deque()

for i in range(num_of_operations):
    inp = input()
    if inp == 'pop':
        d.pop()
    elif inp == 'popleft':
        d.popleft()
    else :
        op,val = inp.split()
        if op =='append':
            d.append(val)
        if op == 'appendleft':
            d.appendleft(val)
        if op == 'extend':
            d.extend(val)
        if op == 'extendleft':
            d.extendleft(val)
        if op =='remove':
            d.remove(val)
        if op == 'reverse':
            d.reverse()
        if op == 'rotate':
            d.rotate()
            
print(*(d))
            
            
            
            
            
