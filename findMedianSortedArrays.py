# 4. Median of Two Sorted Arrays
# Hard
# 25.9K
# 2.8K
# Companies
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #This conditional statement checks if the length og 'nums1' is greater than the length of num2. 
        #id num1 is longer it swaps the 2 array to ensure that num1 is the shorter array.
        #This optimization reduces the number of iteration in the binary search.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is the shorter array
        #These lines calculate and initialize verious variables:
        #m and n stores the length of nums1 and nums2
        #imin and imax represent the range in num1 where binary search will be performed. 
        #half_len calculates half the combined length of the 2 arrays (rounded up). 
        #median is initially set to 0.0
        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        median = 0.0
        # This line starts a while loop that continues as long as imin is less than or equal to imax. 
        # The loop is the core of the binary search algorithm.
        while imin <= imax:
            #inside the loop, it calculates two indices, i and j which represent the partition of nums1 and nums2, respectively. 
            #These indices are used to divide the array into left and right parts
            i = (imin + imax) // 2
            j = half_len - i
            #These lines contain conditional statement that adjust th imin and imax pointer based on the value in the partitions. 
            #These adjustments ensure that the binary search narrows down the search for the correct partition efficiently.
            if i < m and nums2[j - 1] > nums1[i]:
                # Increase i to make the left part of the combined array larger
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # Decrease i to make the left part of the combined array smaller
                imax = i - 1
            #when the correct partition is found(i.e., when imim and imax meet), it calculates the median based on the maximum of the left part(max_of_left) and the minimum of the right part (min_of_right). 
            # If the total length is odd(checked by (m+n)%2 == 1), it returns the maximum of the left part as the median. 
            #Otherwise, it returns the average of 'max_of_left' and 'min_of_right' as the median.    
            else:
                # Found the correct partition
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return float(max_of_left)

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

        return median
