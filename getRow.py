# 

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize the result with the first element, which is always 1.
        result = [1]

        # Generate the next elements in the row using the previous row.
        for i in range(1, rowIndex + 1):
            # Calculate the next element using the previous row.
            # The element at index i is the sum of elements at indices i-1 and i in the previous row.
            # We use zip to pair elements from the beginning and end of the row.
            row = [x + y for x, y in zip(result + [0], [0] + result)]
            result = row

        return result

# Example usage:
solution = Solution()
print(solution.getRow(3))  # Output: [1, 3, 3, 1]
print(solution.getRow(0))  # Output: [1]
print(solution.getRow(1))  # Output: [1, 1]