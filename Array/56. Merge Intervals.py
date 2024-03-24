class Solution:
    def merge(self, intervals):
        res = []
        intervals.sort(key=lambda x: x[0])
        curr = intervals[0]
        for val in intervals:
            s, e = val[0], val[1]
            ns, ne = curr[0], curr[1]
            if ne < s:
                res.append(curr)
                curr = [s,e]
            else:
                curr = [ns,max(e,ne)]
        res.append(curr)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge([[1,4],[4,5]]))
    print(s.merge([[1, 4], [5, 6]]))
    #[[1,4], [5,6]]
    print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
    #[1,10]