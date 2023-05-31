my_dict = {'apple': 3, 'banana': 1, 'orange': 2, 'grape': 1, 'cherry': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1], x[0])))
print(sorted_dict)

# {'apple': 3, 'cherry': 2, 'orange': 2, 'banana': 1, 'grape': 1}



'''
By using -x[1] as the first condition in the sorting key, we sort the quantities in descending order.
And by using x[0] as the second condition, we sort the names in ascending order.
 
'''

my_list = [(3, 'apple'), (1, 'banana'), (2, 'orange'), (1, 'grape'), (2, 'cherry')]
sorted_list = sorted(my_list, key=lambda x: (x[0], x[1]))[:3]
print(sorted_list)


# [(1, 'banana'), (1, 'grape'), (2, 'cherry')]


'''
In this code, the key argument of the sorted() function is set to a lambda function lambda x: (x[0], x[1]). 
This lambda function defines the sorting criteria, where the list elements are sorted first based on the first element (x[0]), 
and then based on the second element (x[1]).
'''
