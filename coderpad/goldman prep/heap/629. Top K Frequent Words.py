import heapq
from collections import Counter
class Solution:
    def topKFrequent(self,words,k):
        freq = Counter(words)
        #return sorted(freq, key=freq.get, reverse=True)[:k]
        return sorted(freq, key=lambda x: (-freq[x],x))[:k]

    def topKFrequentHeap(self, words, k):
        freq = Counter(words)
        heap = [(-count, word) for word, count in freq.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
print(Solution().topKFrequent(['i','love','leetcode','love','i','leetcode'],2))