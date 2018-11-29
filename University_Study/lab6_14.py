"""
챕터: day6
주제: raise exception
문제: 사용자로부터 숫자를 입력받아, 0 이하 또는 100초과의 정수가 입력되면, ValueError 발생(raise)시키고,
"1과 100사이의 수를 입력해 주세요" 출력
작성자: 한현수
작성일: 2018.11.29
"""
try:
    number = int(input("1이상 100 이하 숫자 입력: "))
    if (number <= 0 or number > 100):
        raise ValueError
except:
    print("1과 100사이의 수를 입력해 주세요.")