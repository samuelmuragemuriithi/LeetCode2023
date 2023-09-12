class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the input array to make it easier to find triplets
        
        result = [] # This line intializes an empty list called 'result' to store the unique triplets that sum up to zero
        # This for loop iterates through the input list 'nums', but stop at the third -to-last element.
        for i in range(len(nums) - 2):
            # This 'if' statement checks if the current element 'nums[i]' is equal to the previous element 'nums[i-1]' and ensures that 'i' is greater than 0. If this condition is true,it means that we have encountered a duplicate value, so weto the next iteration of the loop to skip it.
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate values to avoid duplicate triplets
            #This line initializes two pointers, 'left' and 'right' , which are used to scan the element from the left and right ends of the sorted array
            left, right = i + 1, len(nums) - 1
            #This while loop continues as long as the 'left' pointer is less than the right pointer. Its the core of the algorithm where we search  for tripllets that sum up to zero.
            while left < right:
                #This line calculates the sum of the current elements pointed to by 'i','left', and 'right'.
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    #This  line appends the triplets 'num[i],nums[left], nums[right])': This line appends the triplets '[nums[i],nums[left],nums[right]])'
                    result.append([nums[i], nums[left], nums[right]])
                    #We move the 'left' pointer one step to the right and the right pointer one step to the left to search for the next triplets.
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for left and right pointers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                #If the sum is less than zero, we increment the 'left' pointer to move towards larger values in the sorted array 
                elif total < 0:
                    left += 1
                #If the sum is greater than zero, we decrement the 'right' pointer to move towards smaller values in the sorted array.
                else:
                    right -= 1
        
        return result
if __name__=="__main__":
    solution = Solution()   
    nums = [-1,0,1,2,-1,-4]
    arr=solution.threeSum(nums)
    print(arr)