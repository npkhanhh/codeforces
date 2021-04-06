from sys import stdin

for _ in range(int(stdin.readline())):
    a = stdin.readline().strip()
    b = stdin.readline().strip()
    n = len(a)
    m = len(b)
    dp = [[0] * m for _ in range(n)]
    longest = 0
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                if i > 0 and j>0:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 1
                if dp[i][j] > longest:
                    longest = dp[i][j]
    print(n - longest + m - longest)
