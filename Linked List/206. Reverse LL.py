class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseRecursList(self, head):
        if not head or not head.next:
            return head
        res = self.reverseRecursList(head.next)
        head.next.next = head
        head.next = None
        return res

    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

# how to find kth element from back of linked list: 2 pointer
if __name__ == '__main__':
    ln = ListNode(1, ListNode(2, ListNode(3)))
    print(Solution().reverseList(ln).val)

