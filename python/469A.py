n = int(input())
a = set(list(map(int, input().split()))[1:])
b = set(list(map(int, input().split()))[1:])
print(['Oh, my keyboard!', 'I become the guy.'][len(a.union(b)) == n])