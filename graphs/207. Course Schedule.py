# cycle
from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        adj_lst = [[] for _ in range(numCourses)]
        #v is the prerequisite
        for u, v in prerequisites:
            adj_lst[v].append(u)
        state = [0] * numCourses
        def has_cycle(v):
            # have taken this prereq alr
            if state[v] == 1:
                return False
            #circles back
            if state[v] == -1:
                return True
            state[v] = -1
            for i in adj_lst[v]:
                if has_cycle(i):
                    return True
            state[v] = 1
            return False
        for v in range(numCourses):
            if has_cycle(v):
                return False
        return True

    def canFinishTopo(self, numCourses, prerequisites):
        adj_lst = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj_lst[v].append(u)
        state = [0] * numCourses
        for u, v in prerequisites:
            state[u] += 1
        q = deque([u for u in range(numCourses) if state[u] == 0])
        count = 0
        while q:
            v = q.popleft()
            count += 1
            for w in adj_lst[v]:
                state[w] -= 1
                if state[w] == 0:
                    q.append(w)
        if count != numCourses:
            return False
        return True
