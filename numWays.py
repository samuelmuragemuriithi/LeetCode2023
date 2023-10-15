class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        maxPos = min(arrLen - 1, steps // 2 + 1)
        
        # Initialize a 2D array to store the number of ways
        dp = [[0] * (maxPos + 1) for _ in range(steps + 1)]
        dp[0][0] = 1  # Initial position
        
        # Dynamic programming
        for i in range(1, steps + 1):
            for j in range(maxPos + 1):
                dp[i][j] = dp[i - 1][j]  # Stay in the same place
                
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD  # Move to the left
                
                if j < maxPos:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % MOD  # Move to the right
        
        return dp[steps][0]  # The final result is the number of ways to be at index 0 after 'steps' steps

# Example usage:
solution = Solution()
print(solution.numWays(3, 2))  # Output: 4
print(solution.numWays(2, 4))  # Output: 2
print(solution.numWays(4, 2))  # Output: 8