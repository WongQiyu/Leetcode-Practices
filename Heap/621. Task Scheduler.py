from collections import Counter
class Solution:
    def leastInterval(self, tasks, n) :
        if n == 0:
            return len(tasks)
        counter = Counter(tasks)
        max_occurrence = max(counter.values())
        no_max_occurrence = sum((1 for task, occurrence in counter.items() if occurrence == max_occurrence))
        max_interval = (max_occurrence-1) * (n+1) + no_max_occurrence
        return max(max_interval, len(tasks))
if __name__ == '__main__':
    for i in range(9, 3, -1):
        print(i)
    #print(Solution().leastInterval(["A","A","A","B","B","B"], 2))
    #print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 0))
    #print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))