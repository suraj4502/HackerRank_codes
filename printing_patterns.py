
# taking the no of rows and columns.
n,m = map(int,input().split())


# printing the upper part
for i in range(1,n,2):
    pattern = ".|." *i
    print(pattern.center(m,'-'))

# printing the middle part
print("WELCOME".center(m,'-'))

# printing the lower part
for i in range(n-2,0,-2):
    pattern = ".|." *i
    print(pattern.center(m,'-'))
    
    
#  input = 7 21

"""
output :


---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------


"""
    
