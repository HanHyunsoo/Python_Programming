"""
챕터: day5
주제: 재귀함수(recursion)
자기 자신을 호출하는 함수
문제:
곱하기를 더하기 반복문으로 구현한 함수 prod를 정의하여 prod(3, 6)을 계산하여 출력
작성자: 한현수
작성일: 2018.10.11.
"""
# 곱셉을 더하기로 구현한 함수
def prod(a, b):
    result = 0
    for i in range(b):
        result += a
    return result

# 재귀함수를 이용하여 구현한 함수 r_prod
def r_prod(a, b):
    if b == 1: return a
    else: return a + r_prod(a, b - 1)

print(prod(3, 6))
print(r_prod(3, 6))