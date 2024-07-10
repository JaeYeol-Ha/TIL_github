keys = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
key_dict = dict()
for x in range(4):
    for y in range(3):
        key_dict[keys[x][y]] = [x, y]


def closed_hand(number, lhand, rhand):
    curPos = key_dict[number]
    lPos = key_dict[lhand]
    rPos = key_dict[rhand]
    ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
    rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])
    if ldist < rdist:
        return 'L'
    elif ldist > rdist:
        return 'R'
    else:
        return None


def solution(numbers, hand):
    answer = ''
    left_hand = '*'
    right_hand = '#'

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_hand = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right_hand = number
        else:  # [2,5,8,0]
            which_hand = closed_hand(number, left_hand, right_hand)
            if which_hand == 'L':
                answer += 'L'
                left_hand = number
            elif which_hand == 'R':
                answer += 'R'
                right_hand = number
            else:  # 둘다 거리가 같다면
                if hand == "left":
                    answer += 'L'
                    left_hand = number
                else:
                    answer += 'R'
                    right_hand = number
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
result = "LRLLLRLLRRL"

chk = solution(numbers, hand)
print(chk)
if chk == result:
    print('okay')
