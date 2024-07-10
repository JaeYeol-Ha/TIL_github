card = list(range(1,25))

print(card)

# 9~13번째 뒤집기
start = 9
end = 13

card[start-1:end] = card[end-1:start-2:-1]

print(card)

