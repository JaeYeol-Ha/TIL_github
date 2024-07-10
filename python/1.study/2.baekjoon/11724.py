import sys
input = sys.stdin.readline

maps = {}

n, m = map(int, input().split())

for i in range(m):
    a, b = map(int, input().split())
    maps[a] = [maps[a], b]
    maps[b] = [maps[b], a]

print(maps)
