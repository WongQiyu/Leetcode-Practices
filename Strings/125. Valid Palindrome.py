class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome('"A man, a plan, a canal: Panama"'))