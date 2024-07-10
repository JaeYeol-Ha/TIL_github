def getTest2(idx, nn, reply, k):
    if k == 0:
        return 0
    for i in range(idx):  # ABA ,BAB ,ABA ...
        if reply[i:i+nn] == reply[i+nn:i+nn*2]:
            print(f'{reply}:중복{reply[i:i+nn]}, {reply[i+nn:i+nn*2]}')
            return getTest2(idx, nn, reply, k-1)
        else:
            print(f'{reply}:중복아님{reply[i:i+nn]}, {reply[i+nn:i+nn*2]}')

def getTest(reply, nlen, n, k):
    for nn in range(n, nlen):  # 길이 3, 4, 5....
        idx = len(reply)-(nn*(k-1))
        if getTest2(idx, nn, reply, k) == 0:
            return 0
    return 1

def solution(replies, n, k):
    result = []
    for reply in replies:  # "AFFDEFDEFDEEC"
        nlen = len(reply)-(n*k)
        result.append(getTest(reply, nlen, n, k))
    return result


print(solution(["AFFDEFDEFDEEC", "ABABABABBCCEF", "FFFFFFFFFFFFF", "FCBBBFCBBECBB"], 3, 2))
