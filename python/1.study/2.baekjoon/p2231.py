n = int(input())
result = 0
for i in range(1,n+1):
    s = sum(map(int,str(i)))+ i
    if(s == n):
        result = i
        break
print(result)