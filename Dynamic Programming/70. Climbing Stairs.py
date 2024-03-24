class Solution:
    def climbStairs(self, n):
        #bottom up
        one = two = 1
        for _ in range(n):
            one, two = two, one + two
        return one


if __name__ == '__main__':
    print(Solution().climbStairs(5))