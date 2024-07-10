s="aabbaccc"
def soultion(s):
    l = len(s)
    minLen = l
    if l <= 3:
        return l
    for unit in range(1, (l//2 + 1)):
        for i in range(l):
            while i+unit:i+(2*unit) < l:
                if s[i:i+unit] == s[i+unit:i+(2*unit)]:
                    
