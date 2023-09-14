# 332. Reconstruct Itinerary
# Hard
# 5K
# 1.7K
# Companies
# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

# Example 1:


# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
# Example 2:


# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

# Constraints:

# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi

class Solution(object):
    def findItinerary(self, tickets):
        #This line defines an inner function called 'dfs'. This function is a depth-first search(DFS) helper function that will be used to explore and find the itinerary
        def dfs(current_airport):
            #if len(itinerary)==len(ticket)+1: This line checks if the length of 'itinerary' list is equal to the total number of tickets plus 1. If it is, it means we have successfully constructed a valid itinerary that includes all tickets, so it returns a copy of the itinerary'.
            if len(itinerary) == len(tickets) + 1:
                return itinerary[:]
            # This line checks if the current_airport is not in the graph dictionary. If it's not , it means there are not outgoing flights from this airport, so it returns 'None' to signal that we cannot continue itinerary from this point.
            if current_airport not in graph:
                return None
            # This line starts a loop that iterates over the destination(next airports) from current_airport. The enumerate function is used to get both index i and the next airport itself from the list of destinations
            for i, next_airport in enumerate(graph[current_airport]):
                #This line checks if flight from current_airport to next_airport has not been visited yet. It uses a 2D visited matrix to keep track of visited flights.If it hasn't been visited, it marks it as visited('True') and appends the the next_airport to the itinerary.
                if not visited[current_airport][i]:
                    visited[current_airport][i] = True
                    itinerary.append(next_airport)
                    #This line recursively calls the dfs function with next airport as the new starting point to continue building the itinerary. It stores the result ofthis recursive call in the result  variable.
                    result = dfs(next_airport)
                    #This line checks if a valid itinerary has been found during the recursive call
                    if result:
                        return result
                    #If a valid itinerary was not found when exploring the current next_airport, it means we need to backtrack. This remove the last added airport ('next_airport') from the itinerary.
                    itinerary.pop()
                    #This marks the flight from
                    visited[current_airport][i] = False
            
            return None
        #This section initializes the graph dictionary to represent the airline ticket connection.
        #It itterates through each ticket, extracts the depature ('from_airport")and arrival ('to_airpot')airports, and adds them to the graph dictionary as key value pairs.
        #If the deputure is not already in the dictionary, it creates an empty list for it and then appends the arrival airport to the list
        graph = {}
        for ticket in tickets:
            from_airport, to_airport = ticket
            if from_airport not in graph:
                graph[from_airport] = []
            graph[from_airport].append(to_airport)
        #This loop iterates through each key in the graph dictionary (representing departure airports) and sort the corresponding list of destination (arrival airport) in lexical order.
        #This ensures that we explore the destination in the correct orderduring the DFS
        for key in graph:
            graph[key].sort()
        #This code initializes the the itinerary list with the starting airport, which is always "JFK".
        #It also initializes the visited matrix as a dictionary with airports as keys and lists of 'False' values as values. Each list has a length of false values as value.
        # Each has a length equal to the number of destination from the corresponding airport in the graph.  
        itinerary = ["JFK"]
        visited = {airport: [False] * len(destinations) for airport, destinations in graph.items()}
        # The finditernerary method is called with "JFK" as the starting airport to intiate the depth-first search process.
        return dfs("JFK")
