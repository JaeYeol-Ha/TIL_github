n,m = map(int,input().split())
strings = []
checks = []
for i in range(n):
    strings.append(input())
for i in range(m):
    checks.append(input())
count = 0
for check in checks:
    if check in strings:
       count +=1
print(count) 
