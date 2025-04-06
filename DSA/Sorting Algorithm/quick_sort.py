"""
You are given an unsorted list of integers. 
Implement the Quick Sort algorithm to sort the list in ascending order.

Quick Sort is a divide-and-conquer algorithm that works by selecting a 'pivot' element from the list and partitioning the other elements into two sublists:
- one with elements less than the pivot,
- and one with elements greater than or equal to the pivot.

The process is then recursively applied to the sublists.

Steps:
1. Choose a pivot element from the list.
2. Partition the list into two sublists: elements less than the pivot and elements greater than or equal to the pivot.
3. Recursively apply the above steps to the sublists.
4. Combine the results to form a sorted list.

Your task is to implement a function that performs this algorithm and returns a sorted version of the original list.

Input:
    arr = [10, 7, 8, 9, 1, 5]
Output:
    [1, 5, 7, 8, 9, 10]

"""

from typing import List


def partition(nums: List[int], start: int, end: int) -> int:
    pivot = nums[end]
    i = start - 1

    for j in range(start, end):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[end] = nums[end], nums[i + 1]
    return i + 1


def quickSort(nums: List[int], start: int, end: int) -> None:
    if start < end:
        partitionIndex = partition(nums, start, end)
        quickSort(nums, start, partitionIndex - 1)
        quickSort(nums, partitionIndex + 1, end)


arr = [10, 7, 8, 9, 1, 5]
quickSort(arr, 0, len(arr) - 1)


def test_quick_sort():
    # Test 1: Basic unsorted list
    arr1 = [10, 7, 8, 9, 1, 5]
    quickSort(arr1, 0, len(arr1) - 1)
    assert arr1 == [1, 5, 7, 8, 9, 10], "Test 1 Failed"

    # Test 2: Already sorted list
    arr2 = [1, 2, 3, 4, 5]
    quickSort(arr2, 0, len(arr2) - 1)
    assert arr2 == [1, 2, 3, 4, 5], "Test 2 Failed"

    # Test 3: Reverse sorted list
    arr3 = [5, 4, 3, 2, 1]
    quickSort(arr3, 0, len(arr3) - 1)
    assert arr3 == [1, 2, 3, 4, 5], "Test 3 Failed"

    # Test 4: List with duplicates
    arr4 = [3, 6, 8, 3, 2, 7, 2]
    quickSort(arr4, 0, len(arr4) - 1)
    assert arr4 == [2, 2, 3, 3, 6, 7, 8], "Test 4 Failed"

    # Test 5: List with all identical elements
    arr5 = [5, 5, 5, 5, 5]
    quickSort(arr5, 0, len(arr5) - 1)
    assert arr5 == [5, 5, 5, 5, 5], "Test 5 Failed"

    # Test 6: Empty list
    arr6 = []
    quickSort(arr6, 0, len(arr6) - 1)
    assert arr6 == [], "Test 6 Failed"

    # Test 7: Single element
    arr7 = [42]
    quickSort(arr7, 0, len(arr7) - 1)
    assert arr7 == [42], "Test 7 Failed"

    print("All test cases passed!")


# Run the tests
test_quick_sort()
