def calc(alp, cop, problem):
    global cost_table, max_alp, max_cop
    alp_rwd = problem[2]
    cop_rwd = problem[3]
    cost = problem[4]
    if max_alp > alp+alp_rwd and max_cop > cop+cop_rwd:
        if cost_table[alp+alp_rwd][cop+cop_rwd] > cost_table[alp][cop]+cost:
            print(str(alp+alp_rwd) + "," + str(cop+cop_rwd))
            print(cost_table[alp+alp_rwd][cop+cop_rwd], cost_table[alp][cop]+cost)
            cost_table[alp+alp_rwd][cop+cop_rwd] = min(cost_table[alp+alp_rwd][cop+cop_rwd], cost_table[alp][cop]+cost)
            for i in range(len(cost_table)):
                print(cost_table[i])


def solution(alp, cop, problems):
    global cost_table, max_alp, max_cop
    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])
    # alp, cop 를 좌표로 표현

    cost_table = [[nalp+ncop for nalp in range(max_alp+1)] for ncop in range(max_cop+1)]
    for i in range(len(cost_table)):
        print(cost_table[i])
    for problem in problems:
        min_alp = problem[0]
        min_cop = problem[1]
        for now_alp in range(min_alp, max_alp):
            for now_cop in range(min_cop, max_cop):
                calc(now_alp, now_cop, problem)

    for i in range(len(cost_table)):
        print(cost_table[i])
    return ""


cost_table = []
max_alp, max_cop = 0, 0
alp, cop = 0, 0
problems = [[2, 2, 2, 1, 2], [5, 5, 3, 3, 4]]

print(solution(alp, cop, problems))
