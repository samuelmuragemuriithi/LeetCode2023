# 3. Longest Substring Without Repeating Characters
# Medium
# 37.4K
# 1.7K
# Companies
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}  # To store the last index of each character
        start = 0  # Start of the current window
        max_length = 0  # Maximum length of the substring without repeating characters

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1

            char_index[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length

# Test cases
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(sol.lengthOfLongestSubstring("bbbbb"))  # Output: 1
print(sol.lengthOfLongestSubstring("pwwkew"))  # Output: 3