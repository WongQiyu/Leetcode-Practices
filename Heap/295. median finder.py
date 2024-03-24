import heapq
from heapq import heapify, heappush, heappop


class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        heappush(self.lo, -num) # max heap
        heappush(self.hi, -self.lo[0]) #min heap
        heappop(self.lo)
        if len(self.lo) < len(self.hi):
            heappush(self.lo, -heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return (self.hi[0]-self.lo[0])/2

if __name__ == '__main__':
# Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()
    obj.addNum(-1)
    obj.addNum(-2)
    param_2 = obj.findMedian()
    print(param_2)