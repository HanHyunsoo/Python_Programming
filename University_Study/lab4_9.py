"""
챕터: day4
주제: 반복문(for문)
문제: 밑변이 5개의 *로 구성된 직각 삼각형 출력
      거꾸로 된 직각 삼각형 출력
작성자: 한현수
작성일: 2018.9.20.
"""
for i in range(1, 6):
    print("*" * i)
print('\n')
for j in range(5, 0, -1):
    print("*" * j)