n = 6
text = "hi"
# second = 6

def solution(n, text, second):
    space = "_" * n
    answer = space + text.replace(" ", "_")
    second %= (n+len(text))
    answer = answer[second:n+second]
    if len(answer) < n:
       answer += ("_" * (n - len(answer)) )
    return answer

for second in range(14):
    print(f'{second} : {solution(n,text,second)}')