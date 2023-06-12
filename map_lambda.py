cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else: 
        seq = [0,1]
        for i in range(2,n):
            next_rec = seq[i-1] + seq[i-2]
            seq.append(next_rec)
    return seq
    

if __name__ == '__main__':
     n = int(input())
    print(list(map(cube, fibonacci(n))))
    
    
    
  '''
  Sample Input
5

Sample Output

[0, 1, 1, 8, 27]
'''
