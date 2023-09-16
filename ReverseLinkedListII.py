# 92. Reverse Linked List II
# Medium
# 10.8K
# 495
# Companies
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node just before the left position
        for _ in range(left - 1):
            prev = prev.next

        # Initialize pointers for reversing the sublist
        current = prev.next
        next_node = None

        # Reverse the sublist from left to right
        for _ in range(right - left + 1):
            temp = current.next
            current.next = next_node
            next_node = current
            current = temp

        # Connect the reversed sublist back to the original list
        prev.next.next = current
        prev.next = next_node

        return dummy.next

if __name__ == "__main__":
    # Example usage within the __main__ block
    head = ListNode(1)
    current = head
    for val in [2, 3, 4, 5]:
        current.next = ListNode(val)
        current = current.next

    left = 2
    right = 4

    solution = Solution()
    reversed_head = solution.reverseBetween(head, left, right)

    # Print the reversed linked list
    while reversed_head:
        print(reversed_head.val, end=" -> ")
        reversed_head = reversed_head.next
