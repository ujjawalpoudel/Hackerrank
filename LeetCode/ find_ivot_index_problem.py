"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""


class Solution:
    def pivot_index(self, nums) -> int:
        total = sum(nums)

        for key, val in enumerate(nums):
            if key == 0:
                left_sum = 0
            else:
                left_sum = sum(nums[:key])

            right_sum = total - left_sum - val

            if left_sum == right_sum:
                return key
        return -1
