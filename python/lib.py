import queue
import math


def sieve(size):
    sie = [-1] * size
    for i in range(2, int(size ** 0.5) + 1):
        if sie[i] != -1:
            continue
        for j in range(i * i, size, i):
            if sie[j] == -1:
                sie[j] = i
    return sie


def factorize(n):
    result = []
    for i in [2, 3, 5]:
        while n % i == 0:
            result.append(i)
            n //= i
    increments = [4, 2, 4, 2, 4, 6, 2, 6]
    d = 7
    inc = 0
    while d * d <= n:
        while n % d == 0:
            result.append(d)
            n //= d
        d += increments[inc]
        inc += 1
        if inc == 8:
            inc = 0
    if n > 1:
        result.append(n)
    return result


def factorize_dict(n):
    result = {}
    for i in [2, 3, 5]:
        while n % i == 0:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
            n //= i
    increments = [4, 2, 4, 2, 4, 6, 2, 6]
    d = 7
    inc = 0
    while d * d <= n:
        while n % d == 0:
            if d not in result:
                result[d] = 1
            else:
                result[d] += 1
            n //= d
        d += increments[inc]
        inc += 1
        if inc == 8:
            inc = 0
    if n > 1:
        result[n] = 1
    return result


class DSU:
    def __init__(self, n):
        self.n = n
        self.p = [0] * (n + 1)
        self.d = {}
        for i in range(1, n + 1):
            self.p[i] = i
            self.d[i] = 1

    def get_set(self, a, shorten=True):
        t = a
        leaves = []
        while self.p[t] != t:
            leaves.append(t)
            t = self.p[t]
        if shorten:
            for v in leaves:
                self.p[v] = t
        return t

    def union(self, a, b):
        set_a = self.get_set(a)
        set_b = self.get_set(b)
        if set_a != set_b:
            if self.d[set_a] < self.d[set_b]:
                set_a, set_b = set_b, set_a
            self.p[set_b] = set_a
            self.d[set_a] += self.d[set_b]
            self.d[set_b] = 0

    def __getitem__(self, item):
        return self.get_set(item)


def min_reverse(a, n):
    start = list(map(str, a))
    a = sorted(a)
    destination = list(map(str, a))
    q = queue.Queue()
    q.put((start, 0))
    if "".join(start) == "".join(destination):
        return 0
    d = {}
    while not q.empty():
        p = q.get()
        t = p[0]
        for j in range(2, n + 1):
            r = t[:]
            r[:j] = r[:j][::-1]
            print(r)
            if "".join(r) == "".join(destination):
                return p[1]
            if "".join(r) not in d:
                d["".join(r)] = 1
                q.put((r, p[1] + 1))

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


def suffix_array(s):
    s += '$'
    n = len(s)
    p = []
    c = [0] * n
    a = []
    for idx, value in enumerate(s):
        a.append((value, idx))
    a.sort(key=lambda x: x[0])

    for val in a:
        p.append(val[1])
    c[p[0]] = 0
    for i in range(1, n):
        if a[i][0] == a[i - 1][0]:
            c[p[i]] = c[p[i - 1]]
        else:
            c[p[i]] = c[p[i - 1]] + 1
    k = 0
    while (1 << k) < n:
        for i in range(n):
            a[i] = ((c[i], c[(i + (1 << k)) % n]), i)
        a.sort()
        for idx, val in enumerate(a):
            p[idx] = val[1]
        c[p[0]] = 0
        for i in range(1, n):
            if a[i][0] == a[i - 1][0]:
                c[p[i]] = c[p[i - 1]]
            else:
                c[p[i]] = c[p[i - 1]] + 1
        k += 1
    # for i in range(n):
    #     print(s[p[i]:])
    return p


print(suffix_array('aaaa'))
