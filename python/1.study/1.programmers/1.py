# Assumption: 0 <= m <= n, bigrand() 는 랜덤한 int value 하나를 반환 하는 함수
import random
# def bigrand(a,b):
#     return random.randint(a, b)

def randselect(m, n):
    if m > 0:
        if (100 % n) < m:
            print(n - 1)
            randselect(m-1, n-1)
        else:
            randselect(m, n-1)

randselect(13,18)