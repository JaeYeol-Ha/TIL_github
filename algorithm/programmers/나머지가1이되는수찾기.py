n = 10


def solution(n):
    for x in range(999999):
        if n % x == 1:
            return x
