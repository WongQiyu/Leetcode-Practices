# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

'''
⏰ Time complexity: O(1)O(1)O(1), as we're only modifying the current node
🧺Space complexity: O(1)O(1)O(1), no extra space is used.
'''