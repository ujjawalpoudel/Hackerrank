"""
Given five positive integers, 
find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""

def mini_max_sum(arr):
    # * Total sum value of array
    total_val = sum(arr)
    
    # * Get maximum value from array
    max_val = max(arr)
    
    # * Get minimum value from array
    min_val = min(arr)
    
    # * Print minimum sum and maximum sum from array
    print(total_val-max_val, total_val-min_val)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    mini_max_sum(arr)
