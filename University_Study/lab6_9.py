"""
챕터: day6
주제: 정규식
문제: 정규식 기호 연습
작성자: 한현수
작성일: 2018.11.15
"""
import re # regular expression 모듈을 수입

# 테스트할 각종 문자열 정의
s = "teeeest"
s2 = "tetst"
s3 = "tst"
s4 = "apple"
s5 = "test1234"

r = re.compile('[\d]') # 숫자를 찾아서 반환
print(r.search(s))
print(r.search(s5))

r = re.compile('[\D]') # 숫자를 아닌 것 찾아서 반환
print(r.search(s))
print(r.search(s5))

r = re.compile('[a-zA-Z]') # 알파벳을 찾아서 반환
print(r.search(s))
print(r.search(s5))