strings = ["sun", "bed", "car"]


def solution(strings, n):
    strings.sort(key=lambda x: x[n])
    return strings


print(solution(strings, 1))
