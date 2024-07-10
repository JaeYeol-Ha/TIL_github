k = int(input())

a = []
for _ in range(k):
    i = int(input())
    if i != 0:
        a.append(i)
    else:
        a.pop()

print(sum(a))
