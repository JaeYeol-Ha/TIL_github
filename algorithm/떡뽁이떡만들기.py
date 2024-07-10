n, m = 4, 3
떡들 = [4, 4, 5, 5]

def binary_search(떡들, m):
    start = 0
    end = max(떡들)
    result = 0
    while start < end:
        손님용떡 = 0
        절단기높이 = (start + end)//2
        # 1. 손님용 떡 길이 재기
        for 떡 in 떡들:
            if 떡 - 절단기높이 > 0:
                손님용떡 += 떡 - 절단기높이
        print(f'손님용떡:{손님용떡}, 절단기높이:{절단기높이}, start:{start}, end:{end}')
        # 2. 크기 대조
        if 손님용떡 < m:
            end = 절단기높이 - 1
        elif 손님용떡 > m:
            result = m
            start = 절단기높이 + 1
    return result


print(binary_search(떡들, m))
