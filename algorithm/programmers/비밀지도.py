n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
# result = ["#####", "# # #", "### #", "# ##", "#####"]


# def solution(n, arr1, arr2):
#     answer = []
#     map1 = []
#     map2 = []
#     for num in arr1:
#         map1.append(num_to_bin(n, num))
#     for num in arr2:
#         map2.append(num_to_bin(n, num))
#     for i in range(n):
#         row = ""
#         for j in range(n):
#             if map1[i][j] == "1" or map2[i][j] == "1":
#                 row += "#"
#             else:
#                 row += " "
#         answer.append(row)
#     print(answer)
#     return answer


# def num_to_bin(n, num):
#     value = ''
#     while num > 1:
#         num, mod = divmod(num, 2)
#         value = str(mod) + value
#     value = str(num) + value
#     while len(value) < n:
#         value = "0" + value
#     return value


# print(solution(n, arr1, arr2))
# print(result)


########################미친놈들풀이########################

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        row = str(bin(i | j)[2:])
        row = row.rjust(n, '0')
        row = row.replace('1', '#')
        row = row.replace('0', ' ')
        answer.append(row)
    return answer


print(solution(n, arr1, arr2))
