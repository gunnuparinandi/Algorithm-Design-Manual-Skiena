# FROM THE ALGORITHM DESIGN MANUAL BY STEVEN S. SKIENA


# CHAPTER 3: DATA STRUCTURES
# PAGE 98

# EXERCISE 3-1
# A common problem for compilers and text editors is determining whether the
# parentheses in a string are balanced and properly nested. For example, the string
# ((())())() contains properly nested pairs of parentheses, which the strings )()( and
# ()) do not. Give an algorithm that returns true if a string contains properly nested
# and balanced parentheses, and false if otherwise.

def balanced(string):
    stack = []
    # Check to see if there is an empty string.
    if string is None:
        return False

    # If the first character in the string is imbalanced, we return false.
    if string[0] is not '(':
        return False

    for i in range(0, len(string)):
        if string[i] == '(':
            stack.append(string[i])
        if string[i] == ')':
            stack.pop()

    # If the string is balanced, we would expect to return 0 as the length of the stack.

    if len(stack) > 0:
        return False

    return True


# main program
if __name__ == "__main__":

    # STRING = '(()'
    print(balanced('(()'))

    print()
    # STRING = '((())())()'
    print(balanced('((())())()'))