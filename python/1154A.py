ab, bc, ac, abc = sorted(list(map(int, input().split())))
print(*[abc - ab, abc - bc, abc - ac])
