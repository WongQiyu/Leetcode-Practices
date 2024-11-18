from heapq import heapify, heappop, heappush
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        heapify(nums1)
        half = len(nums1) // 2
        odd = False
        if len(nums1) % 2:
            odd = True

        val = 0
        for _ in range(half):
            val = heappop(nums1)
        if not odd:
            tmp = heappop(nums1)
            val = (tmp+val) / 2
        else:
            val = heappop(nums1)
        return val
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        allnums = sorted(nums1 + nums2)
        if len(allnums) % 2 != 0:
            return allnums[len(allnums)//2]
        else:
            return (allnums[len(allnums)//2-1] + allnums[len(allnums)//2]) / 2