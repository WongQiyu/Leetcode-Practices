import math
from heapq import heapify, heappush, heappop

class Solution:
    def kClosest(self, points, k):
        res = []
        final = []
        def euclidean_distance(point1, point2):
            return math.sqrt((point1 ** 2 + point2 ** 2))
        for point in points:
            res.append((euclidean_distance(point[0], point[1]),point))
        heapify(res)
        for _ in range(k):
            final.append(heappop(res)[1])
        return final
if __name__ == '__main__':
    print(Solution().kClosest([[3,3],[5,-1],[-2,4]],2))

