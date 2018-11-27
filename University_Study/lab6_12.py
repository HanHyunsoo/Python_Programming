"""
챕터: day6
주제: exception
문제: 사용자로부터 숫자를 입력받아, 1부터 해당 숫자까지의 합을 구하라.
만약 숫자가 아닌 값이 입력, "숫자를 입력하세요"라는 문장을 출력한 후
다시 입력을 받는다.
작성자: 한현수
작성일: 2018.11.27
"""
import re

# excption을 사용하지 않고 프로그래밍
r = re.compile("\d*\d") # 숫자를 확인하기위한 컴파일러 생성
while 1:
    number = input("숫자 입력: ")
    if r.search(number) == None: # 숫자가 없으면 다시 입력
        print("숫자를 입력하세요")
        continue
    break

# 입력받은 숫자까지 합을 구하기 위한 for문
result = 0
for i in range(1, int(number) + 1):
    result += i

print("숫자 합: %d" % result)