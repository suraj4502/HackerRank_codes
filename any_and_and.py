n= int(input())
arr = list(map(int,input().split()))

print(all(map(lambda x: x >0, arr)) and any([str(j)==str(j)[::-1] for j in arr]))

# returns true if all the elements are postive and if any one is palindrome meaning after reversing they look same e.g = 55.
