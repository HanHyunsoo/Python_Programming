"""
챕터: day5
주제: lambda 함수
문제:
* 무명함수(익명함수)
* 매개변수를 받을 수 있다.
* 한줄 계산
* 반환값이 1개, 한줄 계산의 결과가 반환값
작성자: 한현수
작성일: 2018.10.11.
"""

# 합을 구하는 lambda 함수
sum = lambda x, y: x + y # lambda 함수의 시작값이 sum에 저장됨. 실행되는 것은 아님
k = sum(5, 8) # lambda 함수 호출
print(sum(1, 2))
print(k)