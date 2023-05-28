def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        part = string[i : i+k]           # Creating Substring
        # the below lines are used to remove the duplicates.
        result = ''
        for letter in part:
            if letter not in result:
                result += letter
        print(result)
    
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
    
'''

The problem is asking us to split a given string, s, into k equal parts of length k. 
For each part, we need to remove any subsequent occurrences of non-distinct characters and print the resulting merged string.


Sample Input:
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3



Sample Output:
AB
CA
AD

'''
