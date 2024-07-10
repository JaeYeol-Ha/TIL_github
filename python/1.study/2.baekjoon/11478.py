S = input()

sub_strings = set()

l = 1
while l <= len(S):
    for idx in range(len(S)): # 0 1 2 3 4
        if idx+l <= len(S):
            sub_strings.add(S[idx:idx+l])
    l+=1

print(len(sub_strings))
