"""
There is a string s of lowercase English letters that is repeated infinitely many times.
Given an integer n find and print the number of letter a's in the first  letters of the infinite string.
"""

#
# Complete the 'repeated_string' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeated_string(s, n):
    string_length = len(s)

    remainder_val = n % string_length
    quotient = n // string_length

    count = 0
    for x in s:
        if x == "a":
            count += 1
    count = count * quotient
    substring = s[:remainder_val]

    for x in substring:
        if x == "a":
            count += 1
    return count


if __name__ == "__main__":
    s = input()

    n = int(input().strip())

    result = repeated_string(s, n)
