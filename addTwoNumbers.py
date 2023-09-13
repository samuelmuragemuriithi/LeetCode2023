# 2. Add Two Numbers
# Medium
# 28.2K
# 5.4K
# Companies
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

class Solution(object):
    #This method takes 3 parameters self, which refer to the instance of the class and 2 linked list node 'l1' and 'l2'
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #This creates a dummy header node with a value 0, Its used as a place holder for the result linked list, which represent the 2 numbers we want together.
        dummy_head = ListNode(0)
        #Initializes the current pointer to the dummy head.This pointer will be used to traverse and build theresult linked list
        current = dummy_head
        #Initialize the carry variable to store any carry value when adding digits. Its initially set to 0
        carry = 0
        #This line starts a while loop that continues untill either l1 and l2 or both havenodes left to process
        while l1 or l2:
            #Extract the value of the current node l1 and l2. If none we assume the value is 0
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            #Calculate the total sum of the current digit from l1,l2 and any carry from the previous step
            total_sum = x + y + carry
            #Calculate the carry for the next iteration.If the total sum is greater than 10 or equal to 10, we have a carry so we set carry to 1.otherwise remains zero
            carry = total_sum // 10
            #Create a new node with a value of totalsum%10(the last digit of the total sum) and attach it to the next attribute of the current node. This part becomes part of result linked list 
            current.next = ListNode(total_sum % 10)
            #Move the current pointer to the newly created node for the next itteration
            current = current.next
            #Move l1 and l2 to the next node if they exist, preparing for the next iteration
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        #After the iteration we check for the remaing carry
        if carry > 0:
            #If there is a carry,wecreate a new node with the carry value and attach it to the result linked list without the dummy head node
            current.next = ListNode(carry)
        #return next node of the dummy head. This is the actual result linked list without the dummy head node. 
        return dummy_head.next
