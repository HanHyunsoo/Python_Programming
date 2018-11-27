"""
챕터: day6
주제: 정규식
문제: 정규식 기호 연습
작성자: 한현수
작성일: 2018.11.22
"""
import re
"""
1. apple에 a가 들어있는지 확인
2. apple에 b가 들어있는지 확인
3. 정규식을 이용하여, 사용자가 입력한 영어 문장에서 a, e, i, o, u가 포함되어 있는지 찾아서 출력하시오. 만족하는 첫번째만 출혁한다.
<입력> This is a test.
"""
r = re.compile("a")
print(r.search("apple"))
r = re.compile("b")
print(r.search("apple"))
r = re.compile("[aeiou]")
print(r.search(input("<입력> ")))

"""
4. 입력한 단어가 a로 시작하는지 확인
5. 입력한 단어가 e로 끝나는지 검사
"""
r = re.compile("^a")
print(r.search(input("<입력> ")))
r = re.compile("e$")
print(r.search(input("<입력> ")))

"""
7. 입력된 문장에서 숫자부분을 모두 출력하라.
A. 입력 예: 2017년 3월 8일 5000원
B. 출력 예:
2017
3
8
5000
"""
result = re.findall("\d*\d", input("<입력> "))
print("출력 ")
for i in result:
    print(i)

"""
10. 입력된 문장에서 <이후에 나오는 단어들을 출력하라.
A. 입력 예: <2015> <김일수> <성공회대학교>
"""
r = re.compile("<+\w*>")
result = re.findall(r, input("<입력> "))
print("출력: ")
for j in result:
    print(j)