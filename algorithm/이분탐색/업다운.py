# guess를 넘지않는 최대 정수값 찾기
guess = 13.5

lo = 0
hi = 50
mid = hi//2
ans = 0

def is_up_or_ok(mid):
    return mid < guess

while lo <= hi:
    if is_up_or_ok(mid):
        lo = mid + 1
        ans = mid
        print("up :", end="")
    else:
        hi = mid - 1
        print("down :", end="")
    mid = (lo+hi)//2
    print(f"{lo, hi, mid, ans}")

print(ans)