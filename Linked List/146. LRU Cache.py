class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None
        self.head = None
        self.tail = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.cache = ListNode(-1)

    def get(self, key: int) -> int:
        val = self.dic.get(key, -1)
        if val != -1:
            self.traverse(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.traverse(key)
        else:
            if len(self.dic) == self.capacity:
                rem = self.cache.tail
                self.kick_tail(rem)
                del self.dic[rem.val]
                #print(rem.val,self.cache.head.val)
            self.make_head(key)
            print( self.cache.head.val, self.cache.tail.val)
        self.dic[key] = value
        #print(self.dic, self.cache.head.val, self.cache.tail.val)

    def make_head(self, key):
        key = ListNode(key)
        if self.cache.head:
            nex = self.cache.head
            key.next = nex
            nex.prev = key
        else:
            self.cache.tail = key
        self.cache.head = key

    def remove_bonds(self, key):
        prev = key.prev
        nex = key.next
        prev.next = nex
        nex.prev = prev
    def traverse(self, key):
        pointer = self.cache.head
        while key != pointer.val and pointer.next:
            pointer = pointer.next
        if pointer == self.cache.head:
            return
        if pointer == self.cache.tail:
            self.kick_tail(pointer)
        else:
            self.remove_bonds(pointer)
        self.make_head(key)

    def kick_tail(self, pointer):
        prev = pointer.prev
        if prev:
            prev.next = None
        else:
            self.cache.head = None
        self.cache.tail = prev

if __name__ == '__main__':
    obj = LRUCache(1)
    param_1 = obj.get(6)
    print(param_1)
    param_1 = obj.get(8)
    print(param_1)
    obj.put(12, 1)
    param_1 = obj.get(2)
    print(param_1)
    obj.put(15, 11)
    obj.put(5, 2)
    obj.put(1, 15)
    obj.put(4, 2)
    param_1 = obj.get(5)
    print(param_1)
    obj.put(15, 5)
    # obj = LRUCache(3)
    # obj.put(1, 1)
    # obj.put(2, 2)
    # obj.put(3, 3)
    # obj.put(4, 4)
    # param_1 = obj.get(4)
    # print(param_1)
    # print(obj.cache.head.val, obj.cache.tail.val, obj.dic)
    # param_1 = obj.get(3)
    # print(param_1)
    # print( obj.cache.head.val,obj.cache.tail.val, obj.dic)
    # param_1 = obj.get(2)
    # print(param_1)
    # print(obj.cache.head.val,obj.cache.tail.val, obj.dic)
    # param_1 = obj.get(1)
    # print(param_1)
    # print(obj.cache.head.val, obj.cache.tail.val, obj.dic)
    # obj.put(5, 5)
    # param_1 = obj.get(1)
    # print(param_1)
    # param_1 = obj.get(2)
    # print(param_1)
    # param_1 = obj.get(3)
    # print(param_1)
    # param_1 = obj.get(4)
    # print(param_1)
    # param_1 = obj.get(5)
    # print(param_1)
    #print(obj.cache.tail.val, obj.dic)
    # obj = LRUCache(2)
    # obj.put(1, 1)
    # obj.put(2, 2)
    # param_1 = obj.get(1)
    # print(param_1)
    # obj.put(3, 3)
    # param_1 = obj.get(2)
    # print(param_1)
    # obj.put(4, 4)
    # param_1 = obj.get(1)
    # print(param_1)
    # param_1 = obj.get(3)
    # print(param_1)
    # param_1 = obj.get(4)
    # print(param_1)
from collections import OrderedDict
class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)

class LRUCache:
    def __init__(self, MSize):
        self.size = MSize
        self.cache = {}
        self.next, self.before = {}, {}
        self.head, self.tail = '#', '$'
        self.connect(self.head, self.tail)

    def connect(self, a, b):
        self.next[a], self.before[b] = b, a

    def delete(self, key):
        self.connect(self.before[key], self.next[key])
        del self.before[key], self.next[key], self.cache[key]

    def append(self, k, v):
        self.cache[k] = v
        self.connect(self.before[self.tail], k)
        self.connect(k, self.tail)
        if len(self.cache) > self.size:
            self.delete(self.next[self.head])

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.delete(key)
        self.append(key, val)
        return val

    def put(self, key, value):
        if key in self.cache: self.delete(key)
        self.append(key, value)

