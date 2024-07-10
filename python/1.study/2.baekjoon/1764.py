import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

not_hear = set()
not_see = set()

for _ in range(n):
    not_hear.add(input().strip())
for _ in range(m):
    not_see.add(input().strip())

result = sorted(list(not_hear & not_see))

print(len(result))
for i in result:
    print(i)