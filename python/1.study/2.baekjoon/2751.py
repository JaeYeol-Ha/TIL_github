import sys
n = int(input())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()

s = ""
for i in a:
    s += str(i) + '\n'
print(s)

