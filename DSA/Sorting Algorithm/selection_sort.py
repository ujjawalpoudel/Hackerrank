"""
You are given an unsorted list of integers. Implement the Selection Sort algorithm to sort the list in ascending order.

Selection Sort works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first unsorted element. 
This process continues until the entire list is sorted.

Example:
Input: arr = [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]
"""

from typing import List


def selection_sort(nums: List[int]) -> List[int]:
    n = len(nums)

    # Loop through the entire list except the last element
    for i in range(n - 1):
        min_idx = i

        # Find the smallest element in the unsorted part of the list
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        # Swap the found minimum element with the element at index i
        nums[min_idx], nums[i] = nums[i], nums[min_idx]

    return nums


# Test Case 1: Standard case
arr1 = [64, 25, 12, 22, 11]
print(
    f"Test Case 1 (Sorted): {selection_sort(arr1)}"
)  # Expected output: [11, 12, 22, 25, 64]

# Test Case 2: Already sorted array
arr2 = [1, 2, 3, 4, 5]
print(
    f"Test Case 2 (Already sorted): {selection_sort(arr2)}"
)  # Expected output: [1, 2, 3, 4, 5]

# Test Case 3: Array with negative numbers
arr3 = [5, -1, 3, -7, 2]
print(
    f"Test Case 3 (With negative numbers): {selection_sort(arr3)}"
)  # Expected output: [-7, -1, 2, 3, 5]

# Test Case 4: Array with duplicate values
arr4 = [10, 20, 20, 10, 30]
print(
    f"Test Case 4 (With duplicates): {selection_sort(arr4)}"
)  # Expected output: [10, 10, 20, 20, 30]

# Test Case 5: Single element array (edge case)
arr5 = [42]
print(f"Test Case 5 (Single element): {selection_sort(arr5)}")  # Expected output: [42]

# Test Case 6: Empty array (edge case)
arr6 = []
print(f"Test Case 6 (Empty array): {selection_sort(arr6)}")  # Expected output: []
