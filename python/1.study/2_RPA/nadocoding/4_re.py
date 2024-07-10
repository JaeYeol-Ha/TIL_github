import re

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe | caffe
# ^ (^de) : 문자열의 시작 > desk, destination | fade
# $ (se$) : 문자열의 끝 > case, base | face

p = re.compile("ca.e") 

m = p.match("care cafe case coca")
print(m.group())

m = p.search("care cafe case coca")
print(m.group())

lst = p.findall("care cafe case coca")
print(lst)