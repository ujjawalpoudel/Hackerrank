"""
Question:
You are given an array of integers:
arr = [10, 23, 45, 70, 11, 15]
Write a function that takes this array and a target value as input and returns the index of the target using Linear Search.
If the target is not found, return -1.
"""

from typing import List

def linear_search(nums: List[int], target: int) -> int:
    """
    Perform linear search on the list of integers to find the target value.

    :param nums: List of integers to search through
    :param target: The target value to find in the list
    :return: The index of the target if found, otherwise -1
    """
    if not isinstance(nums, list):
        raise ValueError("The first argument must be a list.")
    
    for idx, num in enumerate(nums):
        if num == target:
            return idx
    return -1


# Test Cases

# 1. Regular test case where the target is in the array.
arr = [10, 23, 45, 70, 11, 15]
target = 70
print(f"Test 1 (Target is 70): {linear_search(arr, target)}")  # Expected: 3

# 2. Test case where the target is not in the array.
arr = [10, 23, 45, 70, 11, 15]
target = 90
print(f"Test 2 (Target is 90): {linear_search(arr, target)}")  # Expected: -1

# 3. Test case where the target is the first element.
arr = [10, 23, 45, 70, 11, 15]
target = 10
print(f"Test 3 (Target is 10): {linear_search(arr, target)}")  # Expected: 0

# 4. Test case where the target is the last element.
arr = [10, 23, 45, 70, 11, 15]
target = 15
print(f"Test 4 (Target is 15): {linear_search(arr, target)}")  # Expected: 5

# 5. Test case with only one element, where the target is present.
arr = [100]
target = 100
print(f"Test 5 (Target is 100, single element): {linear_search(arr, target)}")  # Expected: 0

# 6. Test case with only one element, where the target is absent.
arr = [100]
target = 50
print(f"Test 6 (Target is 50, single element): {linear_search(arr, target)}")  # Expected: -1

# 7. Edge case: Empty array.
arr = []
target = 10
print(f"Test 7 (Empty array): {linear_search(arr, target)}")  # Expected: -1

# 8. Test case where the target is repeated multiple times.
arr = [1, 3, 5, 7, 7, 7, 9]
target = 7
print(f"Test 8 (Target is 7, repeated): {linear_search(arr, target)}")  # Expected: 3 (first occurrence)

# 9. Test case with large array and target at the end.
arr = list(range(1, 1000000))
target = 999999
print(f"Test 9 (Target is 999999 in large array): {linear_search(arr, target)}")  # Expected: 999998 (index of 999999)
