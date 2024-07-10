## 구현문제
import math


def solution(fees, records):
    차량별_진입시간 = {}  # {5961: '05:34'}
    차량별_총시간 = {}  # {5961: 14600}
    차량별_총요금 = {}
    for record in records:
        record2 = record.split()  # ['05:34', '5961', 'IN']
        hm = record2[0]
        carNum = record2[1]
        if record2[2] == "IN":
            차량별_진입시간[carNum] = hm
        elif record2[2] == "OUT":
            h2, m2 = map(int, hm.split(":"))
            h1, m1 = map(int, 차량별_진입시간[carNum].split(":"))
            주차시간 = (h2 - h1) * 60 + (m2 - m1)
            if 차량별_총시간.get(carNum):
                차량별_총시간[carNum] += 주차시간
            else:
                차량별_총시간[carNum] = 주차시간
            # 초기화
            차량별_진입시간[carNum] = None

    for carNum in 차량별_진입시간:
        if 차량별_진입시간[carNum]:
            h2, m2 = map(int, "23:59".split(":"))
            h1, m1 = map(int, 차량별_진입시간[carNum].split(":"))
            주차시간 = (h2 - h1) * 60 + (m2 - m1)
            if 차량별_총시간.get(carNum):
                차량별_총시간[carNum] += 주차시간
            else:
                차량별_총시간[carNum] = 주차시간

        if 차량별_총시간[carNum] > fees[0]:  # 주차시간 > 기본시간
            추가납부시간 = math.ceil((차량별_총시간[carNum] - fees[0]) / fees[2])
            차량별_총요금[carNum] = 추가납부시간 * fees[3] + fees[1]
        else:
            차량별_총요금[carNum] = fees[1]

    # 작은번호순 나열
    # orderd_dict = list(dict(sorted(차량별_총요금.items())).values())
    orderd_dict = list(map(lambda x: x[1], sorted(차량별_총요금.items())))
    return orderd_dict


# 기본시간, 기본요금, 단위시간, 단위요금
fees = [180, 5000, 10, 600]

records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]

result = [14600, 34400, 5000]

answer = solution(fees, records)
assert answer == result, f"{answer} != {result}"
