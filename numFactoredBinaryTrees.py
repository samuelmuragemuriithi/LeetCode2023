# 823. Binary Trees With Factors
# Medium
# 2.9K
# 212
# Companies
# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

 

# Example 1:

# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
# Example 2:

# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

# Constraints:

# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 109
# All the values of arr are unique.


from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()  # Sort the array in ascending order
        n = len(arr)
        dp = [1] * n  # Initialize a dynamic programming array with all 1s
        
        index = {x: i for i, x in enumerate(arr)}  # Create a dictionary to store the index of each element
        
        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    factor = arr[i] // arr[j]
                    if factor in index:
                        dp[i] += dp[j] * dp[index[factor]]
                        dp[i] %= MOD
        
        return sum(dp) % MOD

        