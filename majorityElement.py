
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow up: Could you solve the problem in linear time and in O(1) space?


from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        # Use a hash map to count the occurrences of each element
        # This line uses the Counter class to create a dictionary-like object (counts) where keys are the unique elements in the nums list, and values are their respective counts (how many times they appear).
        counts = Counter(nums)

        # Find elements that appear more than n/3 times
        # This is a list comprehension that iterates through the items in the counts dictionary. For each item, it checks if the count is greater than len(nums) // 3. If it is, the element (num) is included in the result list.
        result = [num for num, count in counts.items() if count > len(nums) // 3]

        return result

# Test cases
solution = Solution()
print(solution.majorityElement([3, 2, 3]))  # Output: [3]
print(solution.majorityElement([1]))  # Output: [1]
print(solution.majorityElement([1, 2]))  # Output: [1, 2]