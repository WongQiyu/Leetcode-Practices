from heapq import heapify, heappush, heappop
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        store = []
        heapify(store)
        head = tail = ListNode(0)

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
'''
To analyze the time and space complexity of the mergeKLists function:

Let's denote:

k as the number of linked lists in the input lists.
n as the total number of nodes across all linked lists.
Time Complexity Analysis:
Building the Heap (heapify): This step takes O(k) time as it iterates over the lists array to add the first element of each list to the heap.
Populating the Heap: In the worst-case scenario, each node in each list will be added to the heap once. Since there are n nodes in total, this step takes O(n log k) time, where log k is the time complexity of heap operations.
Building the Merged List: Each node is popped from the heap once and added to the merged list. This step also takes O(n log k) time as there can be at most n nodes to be processed.
Therefore, the overall time complexity is O(n log k).

Space Complexity Analysis:
store heap is used to store at most k nodes, therefore, it takes O(k) space.
Additionally, the merged linked list will take O(n) space as it consists of n nodes.
Hence, the overall space complexity is O(n + k), but since k can be at most n (if each list contains only one element), we can simplify it to O(n).
'''

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