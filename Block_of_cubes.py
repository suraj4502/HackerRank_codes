# Iterate through each test case
for i in range(int(input())):
    # Read the number of cubes for the current test case
    n = int(input())
    
    # Read the lengths of the cubes and store them in a list
    l1 = [int(x) for x in input().split()]
    
    # Find the maximum length of the cubes
    val = max(l1)
    
    # Initialize a condition flag to track stacking possibility
    condition = True
    
    # Continue stacking until all cubes are used
    while len(l1) > 0:
        # Check the leftmost and rightmost cubes
        if l1[0] >= l1[-1]:
            # If left cube is greater or equal, remove it from the list
            temp = l1.pop(0)
        else:
            # If right cube is greater, remove it from the list
            temp = l1.pop()
        
        # Compare the removed cube with the current maximum value
        if val >= temp:
            # If it can be stacked, update the maximum value
            val = temp
        else:
            # If stacking rule is violated, set the condition flag to False
            condition = False
            break
    
    # Check the final stacking condition
    if condition:
        # All cubes were stacked correctly, print "Yes"
        print("Yes")
    else:
        # Stacking rule was violated, print "No"
        print("No")
