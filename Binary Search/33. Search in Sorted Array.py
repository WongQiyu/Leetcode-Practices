from bisect import bisect_left
class Solution:
    def search(self, nums, target):
        k = bisect_left(nums, True, key= lambda x: x < nums[0])
        if target < nums[0]:
            right = bisect_left(nums, target, lo=k)
            return right if nums[right] == target else -1
        left = bisect_left(nums, target, hi=k-1)
        return left if nums[left] == target else -1

    #best result
    def searchRecurse(self, nums, target):
        def get_search(lst, int1, low, high):
            if low > high:
                return -1
            else:
                mid = low + (high - low) // 2
                low1, mid1, high1 = lst[low], lst[mid], lst[high]
                if mid1 == int1:
                    return mid
                elif low1 <= mid1:
                    if (int1 <= mid1 and int1 >= low1):
                        return get_search(lst, int1, low, mid - 1)
                    return get_search(lst, int1, mid + 1, high)
                else:
                    if (int1 >= mid1 and int1 <= high1):
                        return get_search(lst, int1, mid + 1, high)
                    return get_search(lst, int1, low, mid - 1)

        return get_search(nums, target, 0, len(nums) - 1)


    def searchIter(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 8, 1, 2, 3], 8))

    #print(Solution().searchTest([4,5,6,7,0,1,2], 0))
    #print(Solution().searchTest([4, 5, 6, 7, 0, 1, 2], 3))
