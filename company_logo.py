#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict



if __name__ == '__main__':
    # Taking Input
    s = input()   
    
    # creating an empy defaultdict object with int datatype if a certain key is not present then it will assign 0 to it and it will append the number of occurance to a key if it occured multiple times.
    result = defaultdict(int)  
      
    # here it checks if the letter is present in the dictionary or not if not then it adds the letter with a value of 0, and if the same letter appears again then it increments the 0 with 1 and so on.  
    for letter in s:
        result[letter] +=1          
        
    # sorting the dictionary based on two conditions one descending and one ascending both at a same time.
    sorted_dict = sorted(result.items(), key=lambda x: (-x[1], x[0]))
    for i in range(3):
        print(*(sorted_dict[i]))        # * unpacks the list.
    
    
    
    '''
    Output Format:
Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0:
aabbbccde


Sample Output 0:
b 3
a 2
c 2

Explanation 0:
aabbbccde
Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line
because a comes before c in the alphabet.
Note : The string S has at least 3 distinct characters.

    
 '''
