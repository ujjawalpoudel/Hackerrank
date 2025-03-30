"""
You are given an unsorted list of integers. Implement the Bubble Sort algorithm to sort the list in ascending order.

Bubble Sort works by repeatedly swapping adjacent elements if they are in the wrong order. It compares two elements at a time and moves the larger one towards the end of the list. This process is repeated until the list is completely sorted.

Optimization:
A swapped flag is used to optimize performance by stopping early if the list becomes sorted before all iterations are completed.

Input:
    arr = [64, 34, 25, 12, 22, 11, 90]
Output:
    [11, 12, 22, 25, 34, 64, 90]
"""

from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    """
    Perform Bubble Sort on the given list of integers.

    :param nums: List of unsorted integers
    :return: The sorted list in ascending order
    """
    n = len(nums)

    for i in range(n - 1):  # Outer loop runs n-1 times
        swapped = False  # Flag to check if swapping happened
        for j in range(n - i - 1):  # Inner loop runs up to n-i-1
            if nums[j] > nums[j + 1]:  # Swap if out of order
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:  # If no swaps, list is already sorted
            break

    return nums


# Test Cases
arr1 = [64, 34, 25, 12, 22, 11, 90]
print(f"Test 1: {bubble_sort(arr1)}")  # Expected: [11, 12, 22, 25, 34, 64, 90]

arr2 = [5, 1, 4, 2, 8]
print(f"Test 2: {bubble_sort(arr2)}")  # Expected: [1, 2, 4, 5, 8]

arr3 = [1, 2, 3, 4, 5]
print(f"Test 3: {bubble_sort(arr3)}")  # Expected: [1, 2, 3, 4, 5] (Already sorted)

arr4 = [10, 9, 8, 7, 6, 5]
print(f"Test 4: {bubble_sort(arr4)}")  # Expected: [5, 6, 7, 8, 9, 10] (Reverse order)

arr5 = [100]
print(f"Test 5: {bubble_sort(arr5)}")  # Expected: [100] (Single element)

arr6 = []
print(f"Test 6: {bubble_sort(arr6)}")  # Expected: [] (Empty list)
