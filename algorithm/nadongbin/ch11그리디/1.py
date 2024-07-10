n = 5
users = [2, 3, 1, 2, 2]
users.sort()


result = 0
cnt = 0
for user in users:
    cnt += 1
    if cnt >= user:
        result += 1
        cnt = 0

print(result)
