for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i)//9)*i)
   
   
   
   
   '''
   Sample Input

5


Sample Output

1
22
333
4444




code explanation:
For i = 1, 10**1 is 10. Dividing 10 by 9 gives 1 (integer division), and multiplying it by 1 gives 1. So, 1 is printed.
For i = 2, 10**2 is 100. Dividing 100 by 9 gives 11 (integer division), and multiplying it by 2 gives 22. So, 22 is printed.
For i = 3, 10**3 is 1000. Dividing 1000 by 9 gives 111 (integer division), and multiplying it by 3 gives 333. So, 333 is printed.
'''
