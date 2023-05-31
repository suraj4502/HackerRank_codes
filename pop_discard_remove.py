n = int(input())
s = set(map(int, input().split()))

no_of_commands = int(input())

for i in range(no_of_commands):
    inp = input()
    if inp == 'pop':
        s.pop()
    else:
        cmd, val = inp.split()
        if cmd =='remove':
            s.remove(int(val))
        elif cmd =='discard':
            s.discard(int(val))    
        
        
print(sum(s))


'''
Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
Sample Output

4
Explanation

After completing these  operations on the set, we get set{4}. Hence, the sum is  5.

Note: Convert the elements of set s to integers while you are assigning them. 
To ensure the proper input of the set, we have added the first two lines of code to the editor.
'''
