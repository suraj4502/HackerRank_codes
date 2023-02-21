def count_substring(string, sub_string):
    count =0
    start_index = 0
    end_index = int(len(sub_string))
    for i in range(len(string)):
        if sub_string == string[start_index:end_index]:
            count +=1
        start_index +=1
        end_index +=1
    return count
  
  
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
    
    
# input
# ABCDCDC
# CDC

# output = 2
