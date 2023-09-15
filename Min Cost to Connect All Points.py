#This line imports the heapq module which provides function to implement a priority queue(min-heap in this case), which is used to efficiently find the closest unconnected points.
import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #this line calculates the number of points in the input list points and stores it in a variable n. This will be used to keep track of the number of points and determine when all points have been connected.
        n = len(points)
        
        # Calculate the Manhattan distance between two points
        #The Manhattan distance is the sum of the absolute deference in x and y coordinates.
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        # Initialize the minimum cost and the set of connected points
        #It starts at zero since we have not connected any points
        min_cost = 0
        #This initializes an empty set connected to keep track of the points that have been connected so far.
        connected = set()
        
        # Initialize the priority queue with edges sorted by distance
        #It uses a list comprehension to calculate the Manhattan distance between the first point and all other points.
        #The result is a list of turples where each turple contains the distance and the index of the point it connected to (starting from the second point). 
        #heapq.heapfy(edges) convertsthis list into a min-heap, so the smallest distance is always at the top
        edges = [(manhattan_distance(points[0], points[i]), i) for i in range(1, n)]
        heapq.heapify(edges)
        
        # Start with the first point
        #Representing that we have started with the first point in our MInimum Spannig Tree(MST)
        connected.add(0)
        #This line starts a while loop that continues until all points are connected (len(connected) is equal to n).
        while len(connected) < n:
            # Get the closest unconnected pointThis line pops the edge with the smallest distance from the min-heap edges. It retrieves the distance as cost and the index of the point as i.
            #This line pops the edge with the smallest distance from the min-heap edges. It retrieves the distance as cost and the index of the point as i.
            cost, i = heapq.heappop(edges)
            
            # If it's not connected, add it to the MST
            #These lines check if the point with index i is not already in the connected set. If it's not connected, it means we can add it to the MST. In that case, we increment the min_cost by the distance cost and add the index i to the connected set to mark it as connected.
            if i not in connected:
                min_cost += cost
                connected.add(i)
                
                # Add new edges from the newly connected point
                #These lines check if the point with index i is not already in the connected set. If it's not connected, it means we can add it to the MST. In that case, we increment the min_cost by the distance cost and add the index i to the connected set to mark it as connected.
                for j in range(n):
                    if j not in connected:
                        heapq.heappush(edges, (manhattan_distance(points[i], points[j]), j))
        
        return min_cost

# Example usage
solution = Solution()
points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(solution.minCostConnectPoints(points1))  # Output: 20

points2 = [[3,12],[-2,5],[-4,1]]
print(solution.minCostConnectPoints(points2))  # Output: 18
