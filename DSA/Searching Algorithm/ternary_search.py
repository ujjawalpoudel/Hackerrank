"""
Ternary Search Algorithm

You are given a sorted array of integers `arr` and a target integer `x`. Implement a function that performs 
ternary search to determine the index of `x` in `arr`. If `x` is found, return its index; otherwise, return -1.

Ternary search works by dividing the search space into three parts (instead of two, like binary search) 
and recursively or iteratively narrowing the search space. The time complexity of ternary search in the worst 
case is **O(log₃ n)**.

Example:
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
x = 23
Expected Output: 5
"""

from typing import List


def ternary_search(nums: List[int], target: int) -> int:
    """
    Perform an iterative ternary search on a sorted list to find the target value.

    :param nums: List of sorted integers
    :param target: The value to search for
    :return: The index of the target if found, otherwise -1
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3

        if nums[mid1] == target:
            return mid1
        if nums[mid2] == target:
            return mid2

        if target < nums[mid1]:
            r = mid1 - 1  # Search in the left part
        elif target > nums[mid2]:
            l = mid2 + 1  # Search in the right part
        else:
            l, r = mid1 + 1, mid2 - 1  # Search in the middle part

    return -1


# Test Cases

# 1. Regular test case where the target is in the array.
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
print(f"Test 1 (Target is 23): {ternary_search(arr, target)}")  # Expected: 5

# 2. Test case where the target is the first element.
target = 2
print(f"Test 2 (Target is 2): {ternary_search(arr, target)}")  # Expected: 0

# 3. Test case where the target is the last element.
target = 91
print(f"Test 3 (Target is 91): {ternary_search(arr, target)}")  # Expected: 9

# 4. Test case where the target is not in the array.
target = 50
print(f"Test 4 (Target is 50): {ternary_search(arr, target)}")  # Expected: -1

# 5. Edge case: Empty array.
arr = []
target = 10
print(f"Test 5 (Empty array): {ternary_search(arr, target)}")  # Expected: -1

# 6. Test case with only one element, where the target is present.
arr = [100]
target = 100
print(
    f"Test 6 (Target is 100, single element): {ternary_search(arr, target)}"
)  # Expected: 0

# 7. Test case with only one element, where the target is absent.
target = 50
print(
    f"Test 7 (Target is 50, single element): {ternary_search(arr, target)}"
)  # Expected: -1

# 8. Test case with a large sorted array.
arr = list(range(1, 100000))
target = 56789
print(
    f"Test 8 (Target is 56789 in large array): {ternary_search(arr, target)}"
)  # Expected: 56788
