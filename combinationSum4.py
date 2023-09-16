# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:

# Input: nums = [9], target = 3
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
class Solution(object):
    #This line defines a method within the 'solution' class named 'combinationSum4'. It takes three arguments: 'self', 'nums', and 'target'. 'self' is a reference to the instance of class, 
    # while 'nums' is a list of distinct integers, and 'target' is the integer we want to reach with combination
    def combinationSum4(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #This line initializes a list 'dp' of size 'target + 1' with all elements set to 0. The purpose of this list is to store the number of combination to reach each value from 0 to 'target'.
        dp = [0]*(target +1)
        #This line sets the first element of the 'dp' list(corresponding to 0) to 1. This represent that there's one way to make a sum of 0, which is not selecting any number from the 'nums' array
        dp[0]=1
        #This line starts a loop that iterates from 1 to 'target', inclusive. The loop will calculate the number of combination for each target value
        for i in range(1,target+1):
            #This line starts another loop that iterates through the 'nums' list. Its used to consider each number in 'nums' as potential candidate for forming combinations
            for num in nums:
                #This line checks if the current target value 'i' is greater than or equal to the number 'num' from the 'nums' list. This check is essential to ensure that we can use 'num' to form combination for the current target value.
                if i>= num:
                    #if the condition is met(i.e., 'i' is greater than or equal to 'num'), it means we can use 'num' to contribute to the combination for the current target value 'i'. We update 'dp[i]' by adding  the value of 'dp[i-num]'. This step accumulates the number of combination for the current target value by considering  the combination for the previous target value with 'i -num'. 
                    dp[i]+=dp[i-num]
        #finally, this line returns the value of 'dp[target]', which represent the number of combination to reach the target value specified in the input
        return dp[target]

if __name__=='__main__':
    solution = Solution()
    num =[1,2,3]
    target = 4
    result = solution.combinationSum4(num,target)
    print(result)