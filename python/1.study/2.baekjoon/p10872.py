# 학습을 위해 재귀를 사용하자

def factorial_method(a,b):
    if b==0:
        return 1
    elif a==b:
        return b
    else:
        return a*factorial_method(a+1,b)

n = int(input())

print( factorial_method(1, n) )
