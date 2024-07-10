
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input().strip())
cards = list(map(int, input().strip().split()))
counts = Counter(cards) #dict
m = int(input().strip())
calc = list(map(int, input().strip().split()))
answer = ""
for i in calc:
    answer += str(counts[i]) + ' '

print(answer)
