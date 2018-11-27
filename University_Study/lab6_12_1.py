"""
챕터: day6
주제: exception
문제: 사용자로부터 숫자를 입력받아, 1부터 해당 숫자까지의 합을 구하라.
만약 숫자가 아닌 값이 입력, "숫자를 입력하세요"라는 문장을 출력한 후
다시 입력을 받는다.
작성자: 한현수
작성일: 2018.11.27
"""
# exception을 사용하여 프로그래밍
sum = 0
while 1:
    try:
        number = int(input("숫자 입력: "))
        for i in range(1, number + 1):
            sum += i
        print("숫자 총합: %d" % sum)
        break
    except:
        print("숫자를 입력하세요.")