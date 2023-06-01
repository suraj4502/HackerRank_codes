def minion_game(string):
    vow = 0  # Variable to store Kevin's score (starting with vowels)
    cons = 0  # Variable to store Stuart's score (starting with consonants)

    length = len(string)  # Length of the input string

    # Iterate through each character of the string
    for i in range(length):
        if string[i] in 'AEIOU':  # If the character is a vowel
            vow += (length - i)  # Increment Kevin's score by the remaining substring length
        else:
            cons += (length - i)  # Increment Stuart's score by the remaining substring length

    # Compare the scores and print the result
    if vow > cons:
        print("Kevin", vow)
    elif vow == cons:
        print("Draw")
    else:
        print("Stuart", cons)


if __name__ == '__main__':
    s = input()
    minion_game(s)
