# 34. Find First and Last Position of Element in Sorted Array
# Medium
# 18.9K
# 457
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109


from typing import List

class Solution:
    # This line declares a method named searchRange inside the Solution class. It takes two parameters: nums, which is a list of integers, and target, which is an integer. The method returns a list of integers. The type hints (List[int] and -> List[int]) indicate the expected types of the parameters and the return value.
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # This line defines a helper function named find_start that takes the nums list and the target as parameters.
        def find_start(nums, target):
            # These lines initialize variables start and end to represent the search range within the array. result is initialized to -1, and it will store the index of the found target.
            start, end = 0, len(nums) - 1
            # This line starts a while loop that continues until the search range is valid (i.e., start is less than or equal to end).
            result = -1

            while start <= end:
                # This line calculates the middle index of the current search range, avoiding potential integer overflow.
                mid = start + (end - start) // 2
                # These lines update the search range based on whether the middle element is greater than or equal to the target. If it is, the end is updated to mid - 1, and the result is set to mid. If the middle element is less than the target, the start is updated to mid + 1.
                if nums[mid] >= target:
                    end = mid - 1
                    result = mid
                else:
                    start = mid + 1

            return result
        # This line defines a similar helper function named find_end for finding the ending index of the target in the array.
        def find_end(nums, target):
            start, end = 0, len(nums) - 1
            result = -1

            while start <= end:
                mid = start + (end - start) // 2

                if nums[mid] <= target:
                    start = mid + 1
                    result = mid
                else:
                    end = mid - 1

            return result
        # This line calls the find_start helper function to get the starting index of the target in the array.
        start_index = find_start(nums, target)
        
        # Check if the target is not found in the array
        # These lines check if the starting index is valid (-1 indicates that the target is not in the array) or if the element at the starting index is not equal to the target. If either condition is true, it means the target is not present in the array, so the function returns [-1, -1].
        if start_index == -1 or nums[start_index] != target:
            return [-1, -1]

        end_index = find_end(nums, target)

        return [start_index, end_index]

# Example usage:
solution = Solution()

nums = [2, 2]
target = 3
print(solution.searchRange(nums, target))  # Output: [-1, -1]