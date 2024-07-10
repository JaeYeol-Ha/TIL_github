n = input()

left = sum(map(int, n[:len(n)//2]))
right = sum(map(int, n[len(n)//2:]))

if left == right:
    print("LUCKY")
else:
    print("READY")