class Solution:
    def subsets(self, nums):
        def explore(chosen,remaining,res):
            if not remaining:
                res.append(chosen[:])
                return
            # choose first item from remaining
            d = remaining.pop(0)
            chosen.append(d)
            #explore when chosen added
            explore(chosen,remaining,res)
            chosen.pop()
            # explore when chosen not added and remaining get smaller
            explore(chosen,remaining,res)
            # add back to remaining as stack rolls back up
            remaining.insert(0,d)
        res = []
        explore([], nums, res)
        return res


#https://leetcode.com/problems/subsets/solutions/429534/general-backtracking-questions-solutions-in-python-for-reference/
# -queen problem:O(n!)
#
# graph coloring problem:O(nm^n)//where n=no. of vertex,m=no. of color used
#
# hamilton cycle:O(N!)
#
# WordBreak and StringSegment:O(2^N)
#
# subset sum problem:O(nW)