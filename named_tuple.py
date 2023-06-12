# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

#taking num of inputs
no_of_students = int(input())

#creating a namedtuple object.
student = namedtuple('student','ID MARKS NAME CLASS')

#taking the next line as input which is name of the columns
columns = input().split()

#creating a dictionary to store column name and its index
index_mapping = {column : index for index,column in enumerate(columns)}

#creating varibles to store marks and count
marks = 0
count_of_students = 0
    
#iterating for N times and getting input data of N students.
for _ in range(no_of_students):
    data = input().split()
    #storing the data into a namedtuple object
    st_data = student(*(data))
    marks += int(st_data[index_mapping['MARKS']])
    count_of_students += 1
    
print(float(marks/count_of_students))

'''
Sample Input

TESTCASE 01

5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
TESTCASE 02

5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
Sample Output

TESTCASE 01

78.00
TESTCASE 02

81.00

'''
    


    
