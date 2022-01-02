from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    idx = 0
    same_char = True
    for i in range(n):
        idx = i
        if i + 1 < n:
            if s[i+1] > s[i]:
                break
            elif s[i+1] < s[i]:
                same_char = False
            else:
                if same_char:
                    break

    res = s[:idx+1]
    res += res[::-1]
    print(res)


