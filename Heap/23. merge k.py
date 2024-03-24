from heapq import heapify, heappush, heappop
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        store = []
        heapify(store)
        head = head = ListNode(0)

        for i in range(len(lists)):
            if lists[i]:
                heappush(store, (lists[i].val,i,))
                lists[i] = lists[i].next
        while store:
            val, i = heappop(store)
            tail.next = ListNode(val)
            tail = tail.next
            if lists[i]:
                heappush(store, (lists[i].val, i))
                lists[i] = lists[i].next
        return head.next


if __name__ == '__main__':
    #ln = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    #print(Solution().middleNode(ln).val)
    a = ListNode(1, ListNode(4, ListNode(5)))
    b = ListNode(1, ListNode(3, ListNode(4)))
    c = ListNode(2, ListNode(6))
    print(Solution().mergeKLists([a,b,c]).val)
    print(Solution().mergeKLists([a, b, c]).next.next.next.next.val)
    print(Solution().mergeKLists([[],[]]))
    a = ListNode(-1, ListNode(5, ListNode(11)))
    b = ListNode(6, ListNode(10))
    print(Solution().mergeKLists([a, b]).val)
# def mergeKLists_heapq(self, lists):
# 	h = []
# 	head = tail = ListNode(0)
# 	for i in range(len(lists)):
# 		heapq.heappush(h, (lists[i].val, i, lists[i]))
#
# 	while h:
# 		node = heapq.heappop(h)
# 		node = node[2]
# 		tail.next = node
# 		tail = tail.next
# 		if node.next:
# 			i+=1
# 			heapq.heappush(h, (node.next.val, i, node.next))
#
# 	return head.next