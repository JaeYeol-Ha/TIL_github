def solution(names, callings):
    idx = {i: name for i, name in enumerate(names)}  # idx 딕셔너리
    names = {name: i for i, name in enumerate(names)}  # names 딕셔너리

    for i in callings:
        loc = names[i]
        loc2 = loc - 1
        i2 = idx[loc2]

        idx[loc], idx[loc2] = i2, i  # idx 치환
        names[i], names[i2] = loc2, loc  # name 치환

    return list(idx.values())
