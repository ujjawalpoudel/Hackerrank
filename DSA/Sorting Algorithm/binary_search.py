"""
Binary Search Algorithm

You are given a sorted array of integers `arr` and a target integer `x`. Implement a function that 
performs binary search to determine the index of `x` in `arr`. If `x` is found, return its index. 
Otherwise, return -1.

Your solution should have a time complexity of O(log n).

Example:
arr = [1, 3, 7, 10, 14, 20]
x = 7
Expected output: 2
"""

from typing import List

def binary_search(nums: List[int], target: int) -> int:
    """
    Performs binary search on a sorted array to find the index of the target.

    Parameters:
    nums (List[int]): A sorted list of integers.
    target (int): The integer to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage
arr = [1, 3, 7, 10, 14, 20]
x = 7
print(f"Index of {x}: {binary_search(arr, x)}")  # Expected output: 2

# Additional test cases to validate the implementation
test_cases = [
    ([1, 3, 7, 10, 14, 20], 7, 2),   # Target exists in the middle
    ([1, 3, 7, 10, 14, 20], 1, 0),   # Target is the first element
    ([1, 3, 7, 10, 14, 20], 20, 5),  # Target is the last element
    ([1, 3, 7, 10, 14, 20], 5, -1),  # Target does not exist
    ([1], 1, 0),                     # Single element array, target present
    ([1], 2, -1),                    # Single element array, target absent
    ([], 5, -1)                      # Empty array
]

# Running test cases
for arr, x, expected in test_cases:
    result = binary_search(arr, x)
    print(f"binary_search({arr}, {x}) = {result} | Expected: {expected}")
