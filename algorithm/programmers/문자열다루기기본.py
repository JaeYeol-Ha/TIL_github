s = "1234"


def solution(s):
    if len(s) in [4, 6] and s.isdecimal():
        return True
    return False


print(solution(s))
