n = int(input())
title = []
for i in range(3006666):
    if str(i).find('666') >= 0:
        title.append(i)
print(title[n-1])
