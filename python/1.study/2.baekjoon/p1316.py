n = int(input())
cnt = 0
eng = [chr(i) for i in range(97,123)]

def isGroupWord(word):
    lastWord = word[0]
    temp = [ word[0] ]
    # 한 단어씩 확인
    for w in word:
        # 직전 단어와 동일하면 그룹단어
        if lastWord == w:
            continue
        else:
            # 직전 단어와 다르면 나왔던 적 있는 단어인지 확인
            # 한번도 안나온 단어라면 temp 단어로 추가
            if w not in temp:
                temp.append(w)
            else:
                return False
            # 직전 단어 변경
            lastWord = w
    return True

for i in range(n):
    word = input()
    if isGroupWord(word):
        cnt += 1
        # print(f'{word}: True')
print(cnt)

