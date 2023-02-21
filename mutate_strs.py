def mutate_string(string, position, character):
    """include all the chars before position and add character after that and then add 
    the next part which start from position +1 meaning the positon character has been elimninated."""
    string = string[:position] + character + string[position+1:]
    return string
    
    
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
    
    
    
""" 

 input :
s = 'abracadabra'
position = 5, 
character = 'k'


output :

abrackdabra
"""
