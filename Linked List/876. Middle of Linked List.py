class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head) :
        temp = head
        while temp and temp.next:
            head = head.next
            temp = temp.next.next
        return head



if __name__ == '__main__':
    ln = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    print(Solution().middleNode(ln).val)