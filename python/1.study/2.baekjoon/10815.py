n = int(input())
cards = set(map(int,input().split()))
m = int(input())
checks = list(map(int,input().split()))

for check in checks:
    if check in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')


