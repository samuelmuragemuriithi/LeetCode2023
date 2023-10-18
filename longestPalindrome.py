# 5. Longest Palindromic Substring
# Medium
# 27.5K
# 1.6K
# Companies
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # Create a table to store results of subproblems
        dp = [[False] * n for _ in range(n)]

        start, max_length = 0, 1

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check for sub-string of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

        # Check for lengths greater than 2
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1  # Ending index of substring

                # Check if substring is palindrome
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    start = i
                    max_length = k

        return s[start:start + max_length]

# Example usage:
sol = Solution()

s1 = "babad"
output1 = sol.longestPalindrome(s1)
print(output1)  # Output: "bab" or "aba"

s2 = "cbbd"
output2 = sol.longestPalindrome(s2)
print(output2)  # Output: "bb"

        