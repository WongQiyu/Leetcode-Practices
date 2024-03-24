class Solution:
    def threeSum(self, nums):
        neg = []
        pos = []
        is_zero = []
        res = []
        for i in nums:
            if i < 0:
                neg.append(i)
            elif i > 0:
                pos.append(i)
            else:
                is_zero.append(i)
        if len(is_zero) >= 3:
            res.append((0,0,0))
        if not pos and neg:
            return res
            #return [[a for a in item] for item in res]
        if not neg and pos:
            return res
            #return [[a for a in item] for item in res]
        n_set = set(neg)
        p_set = set(pos)
        res = set(res)
        for i in range(len(neg)):
            if -neg[i] in p_set and is_zero:
                res.add((neg[i], 0, -neg[i]))
            for j in range(i+1, len(neg)):
                if -(neg[i] + neg[j]) in p_set:
                    if neg[i] <= neg[j]:
                        res.add((neg[i], neg[j], -neg[i] - neg[j]))
                    else:
                        res.add((neg[j], neg[i], -neg[i] - neg[j]))
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                if -(pos[i] + pos[j]) in n_set:
                    if pos[i] <= pos[j]:
                        res.add((-pos[i] - pos[j], pos[i] , pos[j]))
                    else:
                        res.add((-pos[i] - pos[j], pos[j], pos[i]))
        return res
        #return [[a for a in item] for item in res]
if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1,-4]))
    print(Solution().threeSum([0,1,1]))
    print(Solution().threeSum([0, 0, 0]))