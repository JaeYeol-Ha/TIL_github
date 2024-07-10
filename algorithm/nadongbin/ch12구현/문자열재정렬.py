input_string = ['K1KA5CB7', 'FDSARQWER13579']

for i in input_string:
    alpa = []
    num = 0
    for s in i:
        if s.isalpha():
            alpa.append(s)
        else:
            num += int(s)
    print(''.join(sorted(alpa))+str(num))
