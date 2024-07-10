n, m = map(int, input().split())

card = list(map(int, input().split()))

sum = -1
for a in range(n):
    for b in range(a+1,n):
        for c in range(b+1, n):
            tmp = card[a] + card[b] + card[c]
            if sum < tmp <= m:
                sum = tmp
            
print(sum)