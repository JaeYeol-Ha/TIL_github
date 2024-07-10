# list comprehention 이용
array = [i*i for i in range(20) if i % 2 == 1]

print(array)

# for문 이용 list append
array = []
for i in range(20): 
    if i % 2 == 1:
        array.append(i*i)

print(array)


###### 리스트 컴프리헨션은 2차원 리스트를 초기화 할 때 효과적임
###### 특히 N*M 크기의 2차원 리스트 한 번에 초기화 할 때 매우 유용하다.
n, m = 2, 2
array = [[0] * m for _ in range(n)]
print(array)