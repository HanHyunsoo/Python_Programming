"""
챕터: day6
주제: 정규식
문제: 정규식 기호 연습
작성자: 한현수
작성일: 2018.11.15, 2018.11.20
"""
import re # regular expression 모듈을 수입

# 테스트할 각종 문자열 정의
s = "teeeest"
s2 = "tetst"
s3 = "tst"
s4 = "apple"
s5 = "test1234Test"
s6 = "나는 \"왕\"이다."
s7 = "abc\\d"

r = re.compile('[\d]') # 숫자를 찾아서 반환
print(r.search(s))
print(r.search(s5))

r = re.compile('[\D]') # 숫자를 아닌 것 찾아서 반환
print(r.search(s))
print(r.search(s5))

r = re.compile('[a-zA-Z]') # 알파벳을 찾아서 반환
print(r.search(s))
print(r.search(s5))

# 25 ~ 27까지 코드를 함수인 search를 이용하여 다시 쓰기
print(re.search('[a-zA-Z]', s))
print(re.search('[a-zA-Z]', s5))

# s5에서 알파벳 또는 숫자 찾기
print(re.search('[a-zA-Z0-9]', s5))

# s5에서 숫자 찾기
print(re.search('[0-9]', s5))

# s5에서 대문자 찾기
print(re.search('[A-Z]', s5))

# s5에서 소문자 찾기
print(re.search('[a-z]', s5))

# s6에서 "와 \의 위치 찾기
print(re.search('\"', s6))
print(re.search("\\\\", s6))

# escape 문자 출력
print(s7)
print(re.search("\\\\", s7)) # 패턴을 명시할 때는 \를 찾고 싶으면, \\\\로 명시한다.