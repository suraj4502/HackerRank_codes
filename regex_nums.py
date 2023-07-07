# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
 ^ indicates the start of the string.
[+-]? matches an optional "+" or "-" symbol.
[0-9]* matches zero or more digits.
\. matches the decimal point symbol ".".
[0-9]+ matches one or more digits after the decimal point.
$ indicates the end of the string.
'''

import re

N = int(input())

pattern = r'^[+-]?[0-9]*\.[0-9]+$'

for _ in range(N):
    num_str = input()
    if re.match(pattern,num_str):
        print("True")
    else:
        print("False")



'''
Input (stdin) :
4
4.0O0
-1.00
+4.54
SomeRandomStuff


Expected Output :
False
True
True
False
'''
