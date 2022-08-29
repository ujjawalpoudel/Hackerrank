"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""


class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        map_st = {}
        map_ts = {}

        for i in range(len(s)):
            si, ti = s[i], t[i]

            if (si in map_st and map_st[si] != ti) or (ti in map_ts and map_ts[ti] != si):
                return False
            map_st[si] = ti
            map_ts[ti] = si
        return True
