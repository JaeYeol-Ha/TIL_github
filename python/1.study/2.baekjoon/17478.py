intro = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'

quest = '"재귀함수가 뭔가요?"'

main1 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
main2 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
main3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'

main_last = '"재귀함수는 자기 자신을 호출하는 함수라네"'

end = '라고 답변하였지.'

inline = '____'

# [1 2 [1 2 [1 3 4] 4] 4]
def rerereply(i,n):
    print(inline*i + quest)
    if n>i:
        print(inline*i + main1)
        print(inline*i + main2)
        print(inline*i + main3)
        rerereply(i+1, n)
    else:
        print(inline*i + main_last) # '"재귀함수는 자기 자신을 호출하는 함수라네"'
    print(inline*i + end)

n = int(input())
print(intro)
rerereply(0,n)