"""
You are given an unsorted list of integers. Implement the Insertion Sort algorithm to sort the list in ascending order.

Insertion Sort works by iterating through the list and picking each element one by one. It compares the current element with the previous elements and places it in the correct position in the sorted part of the list. This process continues until the entire list is sorted.

Time Complexity:
- Worst-case: O(n²) (when the list is in descending order)
- Best-case: O(n) (when the list is already sorted)
- Average-case: O(n²)

Example:
Input:
arr = [12, 11, 13, 5, 6]
Output:
[5, 6, 11, 12, 13]
"""

from typing import List

def insertion_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    
    for i in range(1, n):
        curr = nums[i]  # The element to be placed in the correct position
        j = i - 1  # Start comparing from the previous index
        
        while j >= 0 and nums[j] > curr:
            nums[j + 1] = nums[j]  # Shift element to the right
            j -= 1
        
        nums[j + 1] = curr  # Place the current element at the correct position
    
    return nums  # Return the sorted list

# Test Cases

# Test 1: Regular test case
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))  # Expected: [5, 6, 11, 12, 13]

# Test 2: Already sorted array
arr = [1, 2, 3, 4, 5]
print(insertion_sort(arr))  # Expected: [1, 2, 3, 4, 5]

# Test 3: Reverse sorted array
arr = [5, 4, 3, 2, 1]
print(insertion_sort(arr))  # Expected: [1, 2, 3, 4, 5]

# Test 4: Array with duplicates
arr = [4, 3, 2, 4, 1, 2]
print(insertion_sort(arr))  # Expected: [1, 2, 2, 3, 4, 4]

# Test 5: Single element array
arr = [10]
print(insertion_sort(arr))  # Expected: [10]

# Test 6: Empty array
arr = []
print(insertion_sort(arr))  # Expected: []
