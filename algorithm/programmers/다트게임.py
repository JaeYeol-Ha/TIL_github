def solution(dartResult):
    answer = 0
    # S, D, T : 1제곱, 2제곱, 3제곱
    # *: 현재와 바로 전 점수 2배, #: 현재 뺄셈
    # *: 0번째 순서는 현재만
    # *#: 중첩 가능
    results = []  # ['1S', '2D*', '3T']
    idx = 0
    for i in range(len(dartResult)-1):
        if (dartResult[i].isalpha() or dartResult[i] in ['*', '#']) and dartResult[i+1].isdecimal():
            results.append(dartResult[idx:i+1])
            idx = i+1
    results.append(dartResult[idx:])
    double_score = False
    scores = []
    for result in results:
        score = 0
        if '10' in result:
            score += 10
            idx = 2
        else:
            score += int(result[0])
            idx = 1
        if result[idx] == 'S':
            pass
        elif result[idx] == 'D':
            score = score**2
        else:
            score = score**3
        if result[idx+1:]:
            if result[idx+1] == '*':
                score *= 2
                double_score = True
            elif result[idx+1] == '#':
                score = -score
        scores.append(score)
        if double_score:
            if len(scores) > 1:
                scores[-2] *= 2
            double_score = False
    return sum(scores)


dartResults = ['1S2D*3T', '1D2S#10S', '1D2S0T',
               '1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*']

for dartResult in dartResults:
    print(solution(dartResult))
