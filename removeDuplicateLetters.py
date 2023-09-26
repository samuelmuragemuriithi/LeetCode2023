# 316. Remove Duplicate Letters
# Medium
# 7.7K
# 497
# Companies
# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order
#  among all possible results.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.
 

# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution(object):
    def removeDuplicateLetters(self, s):
        stack = []
        seen = set()
        char_count = [0] * 26  # A list to keep count of characters in s
        
        # Count the frequency of each character in s.
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        
        for char in s:
            # Decrement the count of the current character since we are considering it.
            char_count[ord(char) - ord('a')] -= 1
            
            if char in seen:
                continue
            
            # Pop characters from the stack if they are greater and there are more of them later.
            while stack and char < stack[-1] and char_count[ord(stack[-1]) - ord('a')] > 0:
                seen.remove(stack.pop())
            
            # Add the current character to the stack and seen set.
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)

# Example usage:
solution = Solution()
s1 = "bcabc"
s2 = "cbacdcbc"
print(solution.removeDuplicateLetters(s1))  # Output: "abc"
print(solution.removeDuplicateLetters(s2))  # Output: "acdb"
