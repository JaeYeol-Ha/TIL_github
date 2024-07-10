# M = 5
# global cards
# cards = [6, 3, 2, 10, -10]
# N = 8
# quesses = [10, 9, -5, 2, 3, 4, 5, -10]

M = int(input())
global cards
cards = list(map(int,input().split()))
N = int(input())
quesses = list(map(int,input().split()))
cards.sort() # NlogN <= 10^6 
def check(quess):
    lo = 0
    hi = len(cards)
    mid = hi//2
    while lo <= hi: #logN
        if cards[mid] < quess:
            lo = mid +1
        elif cards[mid] == quess:
            return 1
        else:
            hi = mid -1
        mid = (hi+lo)//2
        if len(cards) <= mid:
            return 0
    return 0

for quess in quesses: # N
    print(check(quess), end=" ")