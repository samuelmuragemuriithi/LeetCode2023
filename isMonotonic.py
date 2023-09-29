# 896. Monotonic Array
# Easy
# 2.6K
# 76
# Companies
# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

# Example 1:

# Input: nums = [1,2,2,3]
# Output: true
# Example 2:

# Input: nums = [6,5,4,4]
# Output: true
# Example 3:

# Input: nums = [1,3,2]
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105

class Solution(object):
    def isMonotonic(self, nums):
        increasing = decreasing = True
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            elif nums[i] < nums[i - 1]:
                increasing = False
        
        return increasing or decreasing

# Example usage:
solution = Solution()
nums1 = [1, 2, 2, 3]
nums2 = [6, 5, 4, 4]
nums3 = [1, 3, 2]

print(solution.isMonotonic(nums1))  # Output: True
print(solution.isMonotonic(nums2))  # Output: True
print(solution.isMonotonic(nums3))  # Output: False
