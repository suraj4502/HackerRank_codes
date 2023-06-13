def coinChange(coins, amount):
    # Sort the coins in descending order
    coins.sort(reverse=True)

    count = 0  # Number of coins used
    result = {}  # Result dictionary to store coin denominations and their counts

    for coin in coins:
        if coin <= amount:
            # Calculate the maximum number of coins of the current denomination
            max_coins = amount // coin

            # Update the amount and count
            amount -= max_coins * coin
            count += max_coins

            # Add the coin to the result dictionary
            result[coin] = max_coins

    if amount == 0:
        return result
    else:
        return {}
    
    
    
'''
# Example usage:
coins = [1, 5, 6, 9, 15]
amount = 55 

output : {15: 3, 9: 1, 1: 1}

'''
   
    
    
  '''
The input coins is a list of coin denominations, and amount is the target amount of money to make up using the coins.

The code first sorts the coins list in descending order using sort(reverse=True). This is done to ensure that larger denomination coins are considered first during the calculation.

Two variables, count and result, are initialized. count keeps track of the total number of coins used, and result is a dictionary that stores the coin denominations and their counts.

The code iterates over each coin in the sorted coins list.

For each coin, it checks if the coin value is less than or equal to the remaining amount to be made up.

If the condition is satisfied, it calculates the maximum number of coins of the current denomination that can be used to make up the amount. This is done by dividing the amount by the coin value using integer division (// operator).

It then updates the amount by subtracting the value of the maximum number of coins multiplied by the coin value.

The count is incremented by the maximum number of coins used.

The coin denomination and its count are added to the result dictionary.

After iterating through all the coins, the code checks if the amount is reduced to zero. If it is, it means that the target amount has been fully covered using the available coins, and it returns the result dictionary.

If the amount is not reduced to zero, it means that the target amount cannot be made up using the available coins, and it returns an empty dictionary {} to indicate that it is not possible.
'''
