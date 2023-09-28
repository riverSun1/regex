# 자주 사용하는 정규식 정리
# 정규식을 알게되면 많은것들을 할 수 있는데
# 특히 전처리가 가능하다.

# 데이터를 수집을 하면 중간에 이상한 데이터가 끼어있는 경우가 있다.
# 이때 정규식을 많이 알고 있으면 쉽게 전처리를 할 수 있다.
# 정규식 - 문자를 검사하는 식
# 이 글자에 a라는 문자있냐
# 이 글자에 숫자있냐
# 이 글자에 특수기호 있냐

import re

# re.search('이글자가', '여기에있는가')
# 있으면 object 자료를 뱉어주고 없으면 None을 뱉는다.
a = re.search('정규식', '안녕하세요정규식')
print(a) # 출력결과 ['정규식']

# 중복되는걸 다 찾아준다.
b = re.findall('정규식', '안녕하세요정규식')
print(b) # 출력결과 ['정규식']

# a로 시작하는가?
c = re.findall('^a', 'abcdefg')
print(c) # 출력결과 ['a']

# g로 끝나는가?
d = re.findall('g$', 'abcdefg')
print(d) # 출력결과 ['g']

# 특수문자 찾으려면?
e = re.findall('\$', 'abcde$f^g')
print(e) # 출력결과 ['$']

# a 또는 b 를 찾으려면 [이거저거]
f = re.findall('[ab]', 'abcde$f^g')
print(f) # 출력결과 ['a', 'b']

# 소문자 알파벳 중에 일치하는것
g = re.findall('[a-z]', 'abcde$f^g')
print(g) # 출력결과 ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 대/소문자 알파벳 중에 일치하는것
h = re.findall('[a-zA-Z]', 'AbCde$f^g')
print(h) # 출력결과 ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 모든 한글 중 일치하는것
i = re.findall('[가-힣]', 'AbC안녕')
print(i) # 출력결과 ['안', '녕']

# 모든 한글 중 일치하는것
j = re.findall('[가-힣ㄱ-ㅎ]', 'AbC안녕ㅋㅋ')
print(j) # 출력결과 ['안', '녕', 'ㅋ', 'ㅋ']

# 모든 숫자 중 일치하는것
k = re.findall('[0-9]', 'AbC안녕ㅋㅋ')
print(k) # 출력결과 []

# [] 안에서 ^ 쓰면 not. 0부터 9가 아닌 것들을 찾아준다.
l = re.findall('[^0-9]', 'AbC안녕ㅋㅋ')
print(l) # 출력결과 ['A', 'b', 'C', '안', '녕', 'ㅋ', 'ㅋ']

# 한글이 아닌 것들을 찾아준다.
m = re.findall('[^가-힣]', 'AbC안녕ㅋㅋ')
print(m) # 출력결과 ['A', 'b', 'C', 'ㅋ', 'ㅋ']

# 한글이 아닌 것들을 찾아준다.
n = re.findall('[^가-힣]', 'AbC안녕ㅋㅋ')
print(n) # 출력결과 ['A', 'b', 'C', 'ㅋ', 'ㅋ']

# 모든 숫자를 나타내고 싶으면 '\d', 숫자인 것들을 찾아준다.
o = re.findall('\d', 'AbC안녕123')
print(o) # 출력결과 ['1', '2', '3']

# 숫자 뒤에 숫자가 오는 거을 찾아준다. 두자리 숫자
p = re.findall('\d\d', 'AbC456안녕123')
print(p) # 출력결과 ['45', '12']

# 숫자 뒤에 숫자 뒤에 숫자가 오는 거을 찾아준다. 세자리 숫자
q = re.findall('\d\d\d', 'AbC456안녕123')
print(q) # 출력결과 ['456', '123']

# 모든 숫자를 나타내고 싶으면 \d
# 숫자가 아닌건 \D
# 스페이스바 찾고 싶으면 \s
# 스페이스바가 아닌건 \S (그냥 모든 문자)

# 반복되는 문자를 찾을 때. 문자+ (greedy 하게 찾아줌)
r = re.findall('ㅋ+', '안녕ㅋㅋㅋㅋ')
print(r) # 출력결과 ['ㅋㅋㅋㅋ']

# 대소문자 구문하지 않고 찾아준다.
s = re.findall('abc', 'AbC안녕ㅋㅋ', re.IGNORECASE)
print(s) # 출력결과 ['AbC']

# 찾아서 다른문자로 바꾸기도 가능. re.sub('이걸찾아서', '이걸로바꿔', '문장')
# re.sub('이걸찾아서', '이걸로바꿔', '문장')
t = re.sub('\-', '.', '2022-1-1')
print(t) # 출력결과 2022.1.1

# 숫자만 제거
u = re.sub('\d', '', 'Abcde$f^g3545')
print(u) # 출력결과 Abcde$f^g

# 숫자만 남기고 다 제거
v = re.sub('\D', '', 'Abcde$f^g3545')
print(v) # 출력결과 Abcde$f^g