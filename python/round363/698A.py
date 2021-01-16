n = int(input())

a = list(map(int, input().split()))

dp = [[0] * 3 for _ in range(n)]

if a[0] == 1 or a[0] == 3:
    dp[0][1] = 1
if a[0] == 2 or a[0] == 3:
    dp[0][2] = 1

for i in range(1, n):
    t = max(dp[i-1])
    contest = max(dp[i-1][0], dp[i-1][2])
    gym = max(dp[i-1][0], dp[i-1][1])
    if a[i] == 0:
        dp[i] = [t, t, t]
    elif a[i] == 1:
        dp[i] = [t, contest+1, t]
    elif a[i] == 2:
        dp[i] = [t, t, gym+1]
    elif a[i] == 3:
        dp[i] = [t, contest+1, gym+1]
print(n - max(dp[n-1]))

