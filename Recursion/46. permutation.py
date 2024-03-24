class Solution:
    def permute(self, nums):
        res = []
        used = [False] * len(nums)
        def dfs(path, res, used):
            print(path,used)
            if len(path) == len(nums):
                #deep copy
                res.append(path[:])
                return
            for i, val in enumerate(nums):
                #skip used letters
                if used[i]:
                    continue
                #add letter to permute, mark as done
                path.append(val)
                used[i] = True
                dfs(path, res, used)
                # remove latest letter from permute at that position, 'push it to next'
                path.pop()
                used[i] = False
        dfs([],res , used)
        return res


if __name__ == '__main__':
    print(Solution().permute([1,2,3]))
    #[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    #print(Solution().permute([0,1]))
    #print(Solution().permute([1]))