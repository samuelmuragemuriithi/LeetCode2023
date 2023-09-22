# 392. Is Subsequence
# Easy
# 8.6K
# 463
# Companies
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 
# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0  # Pointer for string s
        j = 0  # Pointer for string t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move to the next character in s
            j += 1  # Always move to the next character in t

        # If i reached the end of s, it means s is a subsequence of t
        return i == len(s)
