class Solution:
    def trap(self, height) -> int:
        if len(height) <= 2:
            return 0
        l, r = 0, len(height) - 1
        lmax, rmax = height[0], height[-1]
        area = 0
        while l <= r:
            if height[l] > lmax:
                lmax = height[l]
            if height[r] > rmax:
                rmax = height[r]
            if lmax <= rmax:
                area += lmax - height[l]
                l += 1
            else:
                area += rmax - height[r]
                r -= 1

        return area

if __name__ == '__main__':
    s = Solution()
    #print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    #print(s.trap([4,2,0,3,2,5]))
    print(s.trap([5, 2, 0, 3, 2, 4]))