"""
챕터: day4
주제: 반복문(for문)
문제: 백준 알고리즘 10871
작성자: 한현수
작성일: 2018.9.20.
"""
n, x = map(int,input().split())
a = list(map(int,input().split()))
result = ''
for i in range(n):
    if x > a[i]:
        result += str(a[i]) + ' '
print(result)