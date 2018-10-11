"""
챕터: day5
주제: 재귀함수(recursion)
자기 자신을 호출하는 함수
문제:
팩토리얼 계산 함수 factorial을 재귀함수로 정의하여, factorail(5)를 호출한 결과를 출력하라.
작성자: 한현수
작성일: 2018.10.11.
"""
def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)

print(factorial(5))