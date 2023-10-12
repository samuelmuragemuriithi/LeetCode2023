# 1095. Find in Mountain Array
# Hard
# 2.6K
# 104
# Companies
# (This problem is an interactive problem.)

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

# Example 1:

# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
# Example 2:

# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.
 

# Constraints:

# 3 <= mountain_arr.length() <= 104
# 0 <= target <= 109
# 0 <= mountain_arr.get(index) <= 109


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # This line finds the peak index of the mountain array using the find_peak method, which is a binary search for the peak
        peak_index = self.find_peak(mountain_arr)
        
        # Search in the left side of the peak
        # The code performs a binary search on the left side of the peak to find the target. If the target is found, the function returns the result.
        left_result = self.binary_search(mountain_arr, target, 0, peak_index)
        if left_result != -1:
            return left_result
        
        # Search in the right side of the peak
        # The code performs a binary search on the right side of the peak to find the target. The desc=True parameter is used to indicate that this search is on the decreasing part of the mountain. If the target is found, the function returns the result.
        right_result = self.binary_search(mountain_arr, target, peak_index + 1, mountain_arr.length() - 1, desc=True)
        return right_result
    # This method finds the peak index of the mountain array using a binary search. It initializes low and high to be the first and last indices of the array.
    def find_peak(self, mountain_arr):
        low, high = 0, mountain_arr.length() - 1
        # It enters a loop where it calculates the middle index (mid) and retrieves the corresponding value (mid_val) from the array.
        while low < high:
            mid = (low + high) // 2
            mid_val = mountain_arr.get(mid)
            # It checks if the value at the middle index is less than the value at the next index. If true, it means the peak is on the right side, so it updates low to mid + 1. Otherwise, it updates high to mid.
            if mid_val < mountain_arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid

        return low
    # This method performs a binary search on a specified portion of the array. The parameters are the array (mountain_arr), the target value (target), and the indices (low and high) indicating the range of the search. The desc parameter is used to indicate whether the search is on a decreasing part of the array.
    def binary_search(self, mountain_arr, target, low, high, desc=False):
        while low <= high:
            mid = (low + high) // 2
            mid_val = mountain_arr.get(mid)
            # It enters a loop where it calculates the middle index (mid) and retrieves the corresponding value (mid_val) from the array.
            if mid_val == target:
                return mid
            elif (mid_val < target) if not desc else (mid_val > target):
                low = mid + 1
            else:
                high = mid - 1

        return -1


