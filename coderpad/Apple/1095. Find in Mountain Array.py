# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        peak = self.find_peak_index(1, n -2, mountain_arr)

        up_i = self.binary_search(0, peak, target, mountain_arr, False)
        if mountain_arr.get(up_i) == target:
            return up_i

        down_i = self.binary_search(peak + 1, n - 1, target, mountain_arr, True)
        if mountain_arr.get(down_i) == target:
            return down_i
        return -1

    def find_peak_index(self, low, high, mountain_arr):
        while low != high:
            mid = low + (high - low) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
        return low

    def binary_search(self, low, high, target, mountain_arr, is_rev):
        while low != high:
            mid = low + (high - low) // 2
            if is_rev:
                if mountain_arr.get(mid) > target:
                    low = mid + 1
                else:
                    high = mid
            else:
                if mountain_arr.get(mid) < target:
                    low = mid + 1
                else:
                    high = mid
        return low