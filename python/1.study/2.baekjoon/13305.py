n = int(input())
load = list(map(int, input().split()))
price = list(map(int, input().split()))

# print(n, load, price, sep="\n")

row_price = price[0]
for i in range(1, n):
    if price[i] > row_price:
        price[i] = row_price
    elif price[i] < row_price:
        row_price = price[i]

hap = 0
for i in range(n-1):
    hap += load[i]*price[i]
print(hap)