class Trie:
    def __init__(self):
        self.s = {}
    def insert(self, word: str):
        curr = self.s
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['*'] = {}

    def search(self, word):
        curr = self.s
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        return '*' in curr

    def startsWith(self, prefix):
        curr = self.s
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True


#
# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':
    obj = Trie()
    obj.insert("apple")
    print(obj.search("apple")  )
    print(obj.search("app"))
    print(obj.startsWith("app"))
    obj.insert("app")
    print(obj.search("app"))
