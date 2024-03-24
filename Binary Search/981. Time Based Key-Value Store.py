from collections import defaultdict
from bisect import bisect


class TimeMap:

    def __init__(self):
        self.meta = defaultdict(list)
        self.val = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.val[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect(self.meta[key], timestamp)
        if idx == 0:
            return ''
        return self.val[key][idx - 1]

#bisect similar to bisect right
# Your TimeMap object will be instantiated and called as such:
if __name__ == '__main__':
    obj = TimeMap()
    #obj.set(key,value,timestamp)
    #param_2 = obj.get(key,timestamp)