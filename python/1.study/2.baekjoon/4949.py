while True:
    s = input()
    if s == '.':
        break
    valance = []
    is_valanced = 'yes'
    for i in s:
        if i == '(' or i == '[':
            valance.append(i)
        elif i == ')' or i == ']':
            if len(valance):
                p = valance.pop()
                if p == '(' and i == ')' or p == '[' and i == ']':
                    continue
                else:
                    is_valanced = 'no'
                    break    
            else:
                is_valanced = 'no'
                break
    if len(valance) != 0 :
        is_valanced = 'no'
    print(is_valanced)