_input = input().split('-')

answer = sum(list(map(int, _input[0].split('+'))))
for i in _input[1:]:
    answer -= sum(list(map(int, i.split('+'))))

print(answer)
