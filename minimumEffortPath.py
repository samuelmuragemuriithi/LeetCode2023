# 1631. Path With Minimum Effort
# Medium
# 5.3K
# 176
# Companies
# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

# Example 1:
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
# Example 2:

# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
# Example 3:

# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.
 
# Constraints:
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 106
# This line imports the heap q module , which is used for creating and managing min heaps (priority queues)
import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        #This line calculates the number of rows and columns in the input grid heights and store them in the variable rows and cols respectively.
        rows, cols = len(heights), len(heights[0])
        #This line defines a list 'directions' that contains turples representing the four possible directions to move in the grid: down, up, right, and left. 
        #This tulples represent changes in row and column indices.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        #This line defines a list 'directions' thatcontains tuples representing the four possible directions  to move in the grid: down,up,right, and left.
        #These  tuples represent changes in row and column indices.
        minEffort = [[float('inf')] * cols for _ in range(rows)]
        #This line initializes a 2D list minEffort with initially infinite values
        #It will be used to store the minimum effort required to reach each cell in the grid.
        #We set all values to infinity as starting point.
        minEffort[0][0] = 0
        #This line intializes a min heap 'minHeap' with asingle element '(0.0.0)' where the first value is the effort, and the second and third values represent the row and column indices. 
        #We also use 'heapq.heapify()' to turn the list into a valid min heap.
        minHeap = [(0, 0, 0)]  # (effort, row, col)
        heapq.heapify(minHeap)

        #This line starts a while loop that continues as long as the minHeap is not empty, indicating there are cells to explore
        while minHeap:
            #This line pops the cell with the minimum effort from the 'minHeap'.'effort' is the minimum effort, and 'r' and 'c' are the row and column indices of the current cell.
            effort, r, c = heapq.heappop(minHeap)
            #This block checks if we have reached the bottom-right cell of the grid (rows -1' and 'col-1'). If we have, it returns the 'effort', as we have found the minimum effort path to the destination.
            if r == rows - 1 and c == cols - 1:
                return effort
            #This Line starts a loop to explore all possible directions (up,down,left,right) from the current cell.
            for dr, dc in directions:
                #This line calculates the new row(nr) and column('nc')indices based on the current cells indices and the direction we are exploring.
                nr, nc = r + dr, c + dc
                #This line checks if the new row and column indices are within the bonds of the grid.
                if 0 <= nr < rows and 0 <= nc < cols:
                    #This line calculates the new effort required to move from the current cell to the neighboring cell.
                    #It takes the maximum of the current effort and the absolute diference in heights between the 2 cells.
                    newEffort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    #This line checks if the new effort is less than the priviously recorded minimum effort for the neighboring cell.
                    if newEffort < minEffort[nr][nc]:
                        #If the new effort is indeed smaller,this line updates the minimum effort for the neighboring cell.
                        minEffort[nr][nc] = newEffort
                        #This line pushes the neighboring cell into the min heap with its new effort value , row, and column indices.
                        heapq.heappush(minHeap, (newEffort, nr, nc))

# Example usage:
solution = Solution()
heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
print(solution.minimumEffortPath(heights))  # Output: 2
