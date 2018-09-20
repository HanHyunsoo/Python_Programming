"""
챕터: day4
주제: 반복문(for문)
문제: 1에서 100까지 3의 배수의 합을 구하여 출력하시오.
작성자: 한현수
작성일: 2018.9.20.
"""
result = 0
for i in range(3, 101, 3):
    result += i
print(result)