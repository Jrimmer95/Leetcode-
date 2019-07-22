"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Note: You may assume the string contain only lowercase letters.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        repeat = []
        for indx, char in enumerate(s):
            if char not in unique.keys() and char not in repeat:
                unique[char] = indx
            elif char in repeat:
                pass
            else:
                unique.pop(char)
                repeat.append(char)
        if len(unique) > 0:
            return list(unique.values())[0]
        else:
            return -1

# This was a poor solution, revisit with collections library
