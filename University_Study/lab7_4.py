"""
챕터: day7
주제: file 쓰기
문제:
현재 디렉토리 아래에 fruits.txt 파일을 생성하여, 사용자가 입력하는 과일을 한 줄에 하나씩 3개를 저장하라.
작성자: 한현수
작성일: 2018.12.6
"""

f = open("C:\\temp\\fruits.txt", "w")
for i in range(3):
    fruit = input("%d번째줄 과일 입력: " % (i + 1))
    price = int(input("%s의 가격 입력: " % fruit))
    f.write("%s : %d\n" %(fruit, price))
f.close()