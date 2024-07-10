def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def factorial_recursive(n, idx = 1):
    if idx>=n:
        return n
    return idx * factorial_recursive(n, idx+1)

print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))