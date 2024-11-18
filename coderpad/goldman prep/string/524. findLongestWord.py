class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        def can_form_by_deleting(s, word):
            # i,j= 0,0
            # if len(word) > len(s):
            #     return False
            # while i < len(s) and j < len(word):
            #     if s[i] == word[j]:
            #         j += 1
            #     i += 1
            # if j == len(word):
            #     return True
            # return False
            it = iter(s)
            return all(char in it for char in word)


        dictionary.sort(key=lambda x: (-len(x), x))

        for word in dictionary:
            if can_form_by_deleting(s, word):
                return word

        return ""


    '''
    s = "abcde"
    word = "aec"
    can_form_by_deleting(s, word)
    Here, it is an iterator over "abcde".
For char = 'a', 'a' is found in it.
For char = 'e', 'e' is found in it after 'a'.
For char = 'c', 'c' is not found in the remaining part of it after 'e'.
Since not all characters are found in the iterator it in order, can_form_by_deleting(s, word) returns False.

    '''