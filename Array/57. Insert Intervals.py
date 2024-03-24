class Solution:
    def insert(self, intervals, newInterval):
        res = []
        check = False
        for val in intervals:
            s, e = val[0], val[1]
            ns, ne = newInterval[0], newInterval[1]
            if e < ns:
                res.append([s,e])
            elif ne < s:
                if not check:
                    check = True
                    res.append(newInterval)
                res.append([s, e])
            else:
                newInterval = [min(s,ns),max(e,ne)]
        if not check:
            res.append(newInterval)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.insert([[1,3],[6,9]],[2,5]))
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))