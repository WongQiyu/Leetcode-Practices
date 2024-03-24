class Solution:
    def letterCombinationsMine(self, nums):
        dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'], '5': ["j", "k", "l"], '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        res = []
        n = len(nums)
        def backtrack(i, nums, tmp):
            if i == n:
                if tmp:
                    res.append(tmp)
                return
            values = dic[nums[i]]
            for val in values:
                backtrack(i + 1, nums, tmp + val)
        backtrack(0, nums, "")
        return res

    def letterCombinations(self, digits):
        if not digits:
            return []
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return

            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

        backtrack("", digits)
        return res




# if __name__ == '__main__':
