import sys
from collections import deque, defaultdict
from math import sqrt, gcd
from itertools import product, permutations

# 標準入力から最後まで読み取るツール
def input_lines():
    lines = []
    for l in sys.stdin:
        if l == '\n':
            break
        line = list(l.rstrip().split())
        lines.append(line)
    return lines


# -----algorithms-----

# 組み込み関数powと変わらん
def pow_(x, y, m):
    if y == 0:
        return 1
    a = 1 # 指数が奇数の時のコミ箱
    while y > 1:
        if y % 2 == 1:
            a *= x
            a %= m
        y = y // 2
        x *= x
        x %= m
    return a*x % m

# 素因数分解した時の要素の数 ex. 44 = 2*2*11 -> 3個
def get_prime_factor(n):
    res = 0
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            res += 1
            n = n // i
    if n != 1:
        res += 1
    return res

# 尺取法の例 典型90の76の場合
def two_pointers(n, A, obj):
    r = 0
    sumA = 0
    for l in range(n):
        while r - l < n and sumA < obj:
            r += 1
            sumA += A[r-1]
        if sumA == obj:
            return True
        else:
            sumA -= A[l]
    return False

# 桁数を求める
def calc_digits(x):
    d = 0
    while x > 0:
        x = x // 10
        d += 1
    return d


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n
        self.size = [1] * n

    def root(self, x):
        if self.parent[x] == -1: return x
        else:
          self.parent[x] = self.root(self.parent[x])
          return self.parent[x]

    def is_same_root(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.size[rx] += self.size[ry]
        return
    
    def calc_size(self, x):
        return self.size[self.root(x)]