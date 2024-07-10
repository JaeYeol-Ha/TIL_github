def star(i, n):
    if i == 0:
        star = '*'
    space = star.replace('*', ' ')
    print(star * n)
    print((star + space + star) * n//3)
    print(star * n)
