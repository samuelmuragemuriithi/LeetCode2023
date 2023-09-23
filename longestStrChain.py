class Solution(object):
    def longestStrChain(self, words):
        # Sort the words by their lengths in ascending order
        words.sort(key=lambda x: len(x))
        
        # Create a dictionary to store the length of the longest chain for each word
        dp = {}
        
        # Initialize the maximum chain length to 1
        max_chain_length = 1
        
        # Iterate through each word in the sorted list
        for word in words:
            # Initialize the chain length for the current word to 1
            dp[word] = 1
            
            # Generate all possible predecessors of the current word by removing one character
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                
                # Check if the predecessor exists in the dictionary
                if predecessor in dp:
                    # Update the chain length for the current word
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            
            # Update the maximum chain length
            max_chain_length = max(max_chain_length, dp[word])
        
        return max_chain_length

        