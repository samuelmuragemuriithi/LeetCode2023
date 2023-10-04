# 706. Design HashMap
# Easy
# 4.6K
# 409
# Companies
# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

# Constraints:

# 0 <= key, value <= 106
# At most 104 calls will be made to put, get, and remove.

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.buckets = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def find_node(self, index, key):
        if self.buckets[index] is None:
            self.buckets[index] = ListNode(-1, -1)  # Dummy node to simplify code
        
        prev = self.buckets[index]
        while prev.next is not None and prev.next.key != key:
            prev = prev.next
        
        return prev

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self.hash_function(key)
        prev = self.find_node(index, key)

        if prev.next is None:
            prev.next = ListNode(key, value)
        else:
            prev.next.value = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = self.hash_function(key)
        prev = self.find_node(index, key)

        return -1 if prev.next is None else prev.next.value

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.hash_function(key)
        prev = self.find_node(index, key)

        if prev.next is not None:
            prev.next = prev.next.next

# Example usage:
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))  # Output: 1
print(obj.get(3))  # Output: -1
obj.put(2, 1)
print(obj.get(2))  # Output: 1
obj.remove(2)
print(obj.get(2))  # Output: -1
