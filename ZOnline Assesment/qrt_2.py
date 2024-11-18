class SumTable:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.m = len(arr[0]) if arr else 0
        self.sum_table = self._build_sum_table()

    def _build_sum_table(self):
        # Build a 2D prefix sum table
        if self.n == 0 or self.m == 0:
            return [[0]]

        sum_table = [[0] * (self.m + 1) for _ in range(self.n + 1)]

        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                sum_table[i][j] = (self.arr[i - 1][j - 1] +
                                   sum_table[i - 1][j] +
                                   sum_table[i][j - 1] -
                                   sum_table[i - 1][j - 1])

        return sum_table

    def get_sum(self, i1, j1, i2, j2):
        # Calculate the sum of submatrix from (i1, j1) to (i2, j2)
        if i1 < 0 or j1 < 0 or i2 >= self.n or j2 >= self.m:
            return None

        return (self.sum_table[i2 + 1][j2 + 1] -
                self.sum_table[i1][j2 + 1] -
                self.sum_table[i2 + 1][j1] +
                self.sum_table[i1][j1])

    def set_value(self, i, j, k):
        # Set value at position (i, j) to k
        if i < 0 or j < 0 or i >= self.n or j >= self.m:
            return False

        diff = k - self.arr[i][j]
        self.arr[i][j] = k

        # Update the sum table
        for r in range(i + 1, self.n + 1):
            for c in range(j + 1, self.m + 1):
                self.sum_table[r][c] += diff

        return True


def performQueries(a, queries):
    table = SumTable(a)
    result = []

    for q_type, q_params in queries:
        if q_type == "get":
            i1, i2, j1, j2 = q_params
            res = table.get_sum(i1, j1, i2, j2)
            result.append(res)
        elif q_type == "set":
            i, j, k = q_params
            table.set_value(i, j, k)

    return result


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    a = [[int(v) for v in input().split()] for _ in range(n)]

    queries = []
    q = int(input())
    for _ in range(q):
        q_tuple = input().split()
        q_type = q_tuple[0]
        q_params = [int(p) for p in q_tuple[1:]]
        queries.append((q_type, q_params))

    results = performQueries(a, queries)
    for res in results:
        print(res)
