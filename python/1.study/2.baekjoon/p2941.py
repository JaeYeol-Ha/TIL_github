croatia = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
count = 0

for i in croatia:
    while True:
        if i in word:
            count += 1
            word = word.replace(i," ", 1)
        else:
            break
word = word.replace(" ", "")
print(count + len(word))

######### 최적화된 코드 #############

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))