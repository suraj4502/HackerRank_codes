if __name__ == '__main__':
    N = int(input())
    li =[]
    for i in range(N):
        op = list(input().split())
        if op[0] == 'insert':
            li.insert(int(op[1]),int(op[2]))
        elif op[0] == 'print':
            print(li)
        elif op[0] == 'remove':
            li.remove(int(op[1]))
        elif op[0] == 'append':
            li.append(int(op[1]))
        elif op[0]== 'sort':
            li.sort()
        elif op[0]=='pop':
            li.pop()
        elif op[0] == 'reverse':
            li.reverse()
            
