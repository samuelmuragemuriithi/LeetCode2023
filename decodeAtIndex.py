class Solution(object):
    def decodeAtIndex(self, s, k):
        size = 0

        # Calculate the size of the decoded string without actually constructing it
        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1

        # Iterate backward through the string to find the kth letter
        for char in reversed(s):
            k %= size  # Reduce k to its corresponding position within the current size

            if k == 0 and char.isalpha():
                return char

            if char.isdigit():
                size /= int(char)
            else:
                size -= 1

# Example usage:
solution = Solution()
print(solution.decodeAtIndex("leet2code3", 10))  # Output: "o"
print(solution.decodeAtIndex("ha22", 5))         # Output: "h"
print(solution.decodeAtIndex("a2345678999999999999999", 1))  # Output: "a"
