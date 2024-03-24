class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        def backtrack(candidates, target,path,prev):
            if target == 0:
                res.append(path)
            if target < 0:
                return
            for num in candidates:
                if num >= prev:
                    backtrack(candidates, target-num, path + [num],num)
                # if num <= target and num >= prev:
                #     backtrack(candidates[1:], target, curr_set,prev)
                #     new_set = curr_set[:]
                #     new_set = new_set + (num,)
                #     backtrack(candidates, target - num, new_set,num)
        backtrack(candidates,target,[],0)
        return res

    class Solution:
        def combinationSumDp(self, candidates: List[int], target: int) -> List[List[int]]:
            dp = [[] for _ in range(target + 1)]
            for c in candidates:  # O(N): for each candidate
                for i in range(c, target + 1):  # O(M): for each possible value <= target
                    if i == c: dp[i].append([c])
                    for comb in dp[i - c]: dp[i].append(comb + [c])  # O(M) worst: for each combination
            return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7],7))
    print(s.combinationSum([2, 3, 5], 8))


'''
Time complexity: O(n)
Space complexity:O(n)
In the dp solution, 
1. we create an array with all the range of values up to target
2. We loop through all the candidates
3 if candidate == one value within range of target:
dp[i].append(candidate]) + values (list of combi) in dp[i-1] 
return dp[-1]
'''