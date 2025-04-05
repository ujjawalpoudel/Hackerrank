"""
You are given an unsorted list of integers. Implement the Merge Sort algorithm to sort the list in ascending order.

Merge Sort is a divide-and-conquer algorithm that works by dividing the array into two halves, 
sorting each half recursively, and then merging the sorted halves into a single sorted list.

Steps:
1. Divide the list into two halves until each sublist contains a single element.
2. Merge the sublists back together in a sorted manner.
3. Repeat this process until the entire list is sorted.

Your task is to implement a function that performs this algorithm and returns a sorted version of the original list.

Input:
    arr = [38, 27, 43, 3, 9, 82, 10]
Output:
    [3, 9, 10, 27, 38, 43, 82]

"""

from typing import List
import unittest


def merge(nums: List[int], start: int, mid: int, end: int):
    i = start
    j = mid + 1
    temp = []

    while i <= mid and j <= end:
        if nums[i] < nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1

    while i <= mid:
        temp.append(nums[i])
        i += 1

    while j <= end:
        temp.append(nums[j])
        j += 1

    for idx, val in enumerate(temp):
        nums[start + idx] = val


def mergeSort(nums: List[int], start: int, end: int):
    if start >= end:
        return
    mid = (start + end) // 2
    mergeSort(nums, start, mid)
    mergeSort(nums, mid + 1, end)
    merge(nums, start, mid, end)


# ------------------------
# ✅ Test Cases
# ------------------------


class TestMergeSort(unittest.TestCase):
    def test_unsorted_array(self):
        arr = [38, 27, 43, 3, 9, 82, 10]
        expected = sorted(arr)
        mergeSort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        mergeSort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        mergeSort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_duplicates(self):
        arr = [4, 5, 1, 2, 5, 3, 4]
        expected = sorted(arr)
        mergeSort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_single_element(self):
        arr = [42]
        expected = [42]
        mergeSort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_empty_array(self):
        arr = []
        expected = []
        mergeSort(arr, 0, len(arr) - 1)  # This won't crash due to base case
        self.assertEqual(arr, expected)


if __name__ == "__main__":
    unittest.main()
