"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. 
The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
"""


def plus_minus(arr):
    # * Total number in array
    total_count = len(arr)

    # * Calculate negative number
    negative_count = len(list(filter(lambda x: (x < 0), arr)))

    # * Calculate positive number
    positive_count = len(list(filter(lambda x: (x > 0), arr)))

    # * Calculate zero number
    zero_count = len(list(filter(lambda x: (x == 0), arr)))

    # * proportion of positive values
    print(round(positive_count / total_count, 5))

    # * proportion of negative values
    print(round(negative_count / total_count, 5))

    # * proportion of zeros
    print(round(zero_count / total_count, 5))


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)
