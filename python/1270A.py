n = int(input())

for i in range(n):
    input()
    max_a = max(list(map(int, input().split())))
    max_b = max(list(map(int, input().split())))
    print('YES' if max_a > max_b else 'NO')
