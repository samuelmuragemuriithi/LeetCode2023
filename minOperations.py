class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        #Calculate the target as the difference between the sum of all elements in the nums array and the given x.
        # This is the value we want to reach by removing elements from the array.
        target = sum(nums) - x
        #Initializes n as the length of the nums array, left as the left pointer for the sliding window. curr_sum to keep track of the current sum of elements in the window, and main_ops as a variable to store the minimum number of operations.
        #We set min ops intially to positive infinity(float(inf)) to keep track of the minimum operations.
        n = len(nums)
        left = 0
        curr_sum = 0
        min_ops = float('inf')
        #Start a for loop that iterates through the nums array with the right pointer.
        for right in range(n):
            # Add the value of 'nums[right]' to the curr_sum to keep track of the current sum of elements in the sliding window.
            curr_sum += nums[right]
            #Enter a while loop that continues as long as cur_sum is greater than the target and left pointer is less than or equal to the right pointer. 
            #This loop adjusts the sliding window size.
            while curr_sum > target and left <= right:
                #Inside the while loop, subtract nums[left] from curr_sum and move the left pointer one step to the right.
                #This adjusts the sliding window by removing elements from the left side untill 'curr_sum' is no longer greater than the target.
                curr_sum -= nums[left]
                left += 1
            #Check if curr-sum is equal to the target. If they are equal, it means we have found a subarray with a sum equal to the target, which correspond to the number of operation needed to reach the x value.
            if curr_sum == target:
                #Calculate the number op operations needed to remove  elements in the current subarray, which is 'n - (right - left +1).
                #Updates min ops  with the minimum of the current value and the calculated value.
                min_ops = min(min_ops, n - (right - left + 1))
        # return min_ops if its not equal to positive infinity, otherwise return -1
        return min_ops if min_ops != float('inf') else -1
