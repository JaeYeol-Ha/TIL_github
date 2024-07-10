# N = int(input()) # 개수
# req = list(map(int, input().split())) # 요구량
# M = int(input()) # 예산

N =4
req = [120, 110, 140, 150]
M = 485

lo = 0
hi = max(req)
mid = (lo+hi)//2
ans = 0

def is_possible(mid):
    return sum(min(r,mid) for r in req) <= M

print(f"{lo, hi, mid, ans}")
while lo<=hi:
    # 업이냐(혹은 딱맞냐)
    if is_possible(mid):
        lo = mid + 1
        ans = mid
    # 다운이냐
    else:
        hi = mid - 1
    mid = (lo+hi)//2
    print(f"{lo, hi, mid, ans}")

print(ans)