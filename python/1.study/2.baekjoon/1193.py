# 1 2 3 4 5 6...
# 1: 1/1
# 2: 1/2
# 3: 2/1
# 4: 3/1
# ...

def solve(i):
    max_num = 1
    line = 1
    while i > max_num:
        line += 1
        max_num += line
    # i = 3, line = 2, max_num = 3
    gap = max_num - i
    if line % 2 == 0:
        top = line - gap
        bot = gap + 1  
    else:
        top = gap 
        bot = line - gap + 1 
    return f'{top}/{bot}'


for i in range(10):
    print( str(i) + ":" + solve(i))
