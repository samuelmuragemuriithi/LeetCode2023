# 343. Integer Break
# Medium
# 4.4K
# 395
# Companies
# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:

# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

# Constraints:

# 2 <= n <= 58

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Handle base case
        if n == 2:
            return 1

        # Initialize an array to store the maximum product for each number from 2 to n
        dp = [0] * (n + 1)

        # The maximum product for 2 is 1
        dp[2] = 1

        # Iterate from 3 to n
        # This starts a loop from 3 to n, as we have handled the base case for 2 already
        for i in range(3, n + 1):
            # Break the number into two parts and find the maximum product
            # The line calculates the maximum product for the current number i.
            # It does so by considering all possible ways to break the number into 2 parts(j and i-j)and finding the maximum product among those possibilities/
            dp[i] = max(max(j, dp[j]) * max(i - j, dp[i - j]) for j in range(1, i))

        return dp[n]

# Example usage
sol = Solution()
print(sol.integerBreak(2))  # Output: 1
print(sol.integerBreak(10)) # Output: 36