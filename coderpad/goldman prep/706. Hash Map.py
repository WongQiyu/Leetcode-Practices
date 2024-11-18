class MyHashMap:

    def __init__(self):
        self.d = {}

    def put(self, key: int, value: int) -> None:
        self.d[key] = value

    def get(self, key: int) -> int:
        return self.d.get(key, -1)

    def remove(self, key: int) -> None:
        self.d.pop(key, None)


class MyHashSet:

    def __init__(self):
        self.d = set()

    def add(self, key: int) -> None:
        self.d.add(key)

    def remove(self, key: int) -> None:
        if key in self.d:
            self.d.remove(key)
        return

    def contains(self, key: int) -> bool:
        return key in self.d
