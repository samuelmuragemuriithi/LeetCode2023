# 1512. Number of Good Pairs
# Easy
# 4.6K
# 211
# Companies
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    count += 1

        return count

# Test cases
solution = Solution()

nums1 = [1, 2, 3, 1, 1, 3]
nums2 = [1, 1, 1, 1]
nums3 = [1, 2, 3]

output1 = solution.numIdenticalPairs(nums1)
output2 = solution.numIdenticalPairs(nums2)
output3 = solution.numIdenticalPairs(nums3)

print("Example 1:", output1)  # Output: 4
print("Example 2:", output2)  # Output: 6
print("Example 3:", output3)  # Output: 0
