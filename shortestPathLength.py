# 847. Shortest Path Visiting All Nodes
# Hard
# 3.9K
# 158
# Companies
# You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.
# Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

# Example 1:
# Input: graph = [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
# Example 2:


# Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
 

# Constraints:
# n == graph.length
# 1 <= n <= 12
# 0 <= graph[i].length < n
# graph[i] does not contain i.
# If graph[a] contains b, then graph[b] contains a.
# The input graph is always connected.


from collections import deque

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        #We determine the number of nodes in the graph and store it in the variable 'n'
        n = len(graph)
    
        # Initialize a memoization table to store the minimum distance for each state.
        # State is represented as (current_node, visited_nodes_mask).
        # visited_nodes_mask is an integer where each bit represents whether a node has been visited.
        # For example, if n = 4, visited_nodes_mask = 1101 means nodes 0, 2, and 3 have been visited.
        memo = [[float('inf')] * (1 << n) for _ in range(n)]
    
        # Initialize the deque with the starting state (node, visited_nodes_mask).
        # The queue is intialized with starting state for each node. 
        # Each state is represented as a tuple '(i,1 <<i) is the bitmask with ith bit set to 1, indicating that the node is visited.
        queue = deque([(i, 1 << i) for i in range(n)])
    
        # Initialize the distance for the starting states as 0.
        # These are the base case for our dynamic programming approach.
        for i, mask in queue:
            memo[i][mask] = 0
        # We start a loop to perform a BFS. We use popleft to dequeue from the left of the queue, ensuring we explore nodes in a breadth-first manner.
        while queue:
            node, mask = queue.popleft()  # Use popleft to pop from the left.
        
            # If all nodes have been visited, return the minimum distance.
            # We check if all nodes have beeen visited by comparing the mask with (1<<n)-1 which is a bitmask with all bite set to 1(indicating all nodes visited).  
            #If all nodes are visited we return the minimum distance for this state.
            if mask == (1 << n) - 1:
                return memo[node][mask]
        
            # Try all neighbors of the current node.
            # We iterate through all the neighbours of the current node and calculate a new bitmask 'new_mask' by setting the bit corresponding to the neighbor node to 1. 
            # If the minimum distance to reach the neighbor using this new state is less than the previously recorded distance, we update the memoization table and enqueue this new state in the queue.
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if memo[neighbor][new_mask] > memo[node][mask] + 1:
                    memo[neighbor][new_mask] = memo[node][mask] + 1
                    queue.append((neighbor, new_mask))
    
        # If all nodes cannot be visited, return -1 (should not happen for a connected graph).
        return -1
