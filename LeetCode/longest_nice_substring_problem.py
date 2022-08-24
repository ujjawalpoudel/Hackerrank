"""
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase.
For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. 
However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. 
If there are multiple, return the substring of the earliest occurrence. 
If there are none, return an empty string.
"""

# * For logical parts i followed different youtube channel to get fast and efficient solution of it


class Solution:
    def longest_nice_substring(self, s: str) -> str:

        if len(s) < 2:
            return ""

        unorder_set = set(s)

        for i in range(len(s)):
            if s[i].swapcase() not in unorder_set:
                left_divide = self.longest_nice_substring(s[:i])
                right_divide = self.longest_nice_substring(s[i + 1 :])

                return max(left_divide, right_divide, key=len)

        return s
