def change1():
	a=2

def change2():
	global a
	a=2

a=1
print(a)
change1()
print(a)
change2()
print(a)