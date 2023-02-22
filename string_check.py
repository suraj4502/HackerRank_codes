if __name__ == '__main__':
    s = input()
    print(any([alpha.isalnum() for alpha in s]))
    print(any([alpha.isalpha() for alpha in s]))
    print(any([alpha.isdigit() for alpha in s]))
    print(any([alpha.islower() for alpha in s]))
    print(any([alpha.isupper() for alpha in s]))
# The any() function in Python returns True if at least one element in an iterable is true, and False otherwise
