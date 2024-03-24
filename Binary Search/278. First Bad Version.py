# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
from bisect import bisect_left

class StatusArray:
  def __getitem__(self, k):
    return isBadVersion(k)

class Solution:
  def firstBadVersion(self, n):
      return bisect_left(StatusArray(), True, 1, n)

      # 278. First Bad Version
      def firstBadVersionOther(self, n: int) -> int:
          return bisect_left(range(n), True, key=isBadVersion)

      def firstBadVersionIter(self, n: int) -> int:
          # good solution but does not take into account if item not found
          low = 0
          high = n
          while low < high:
              mid = low + (high - low) // 2
              if isBadVersion(mid):
                  high = mid
              else:
                  low = mid + 1
          return low
          # l, r = 1, n
          # while l <= r:
          #     m = (l + r) // 2
          #     if l == m == r:
          #         return m
          #     if isBadVersion(m):
          #         r = m
          #     else:
          #         l = m + 1
          #
          # return - 1