"""
챕터: day4
주제: 조건문(elif 이용)
문제: 사용자로부터 정수를 입력받는다.
      0보다 크면 "양수", 0이면 "0", 0보다 작으면 "음수"를 출력한다.
작성자: 한현수
작성일: 2018.9.18.
"""
# 정수 입력 받기
a = int(input("정수 입력"))

# 정수가 0보다 크면 양수 출력
if (a > 0):
    print("양수")
# 그렇지 않고, 정수가 0이면 0출력
elif (a == 0):
    print(0)
# 그렇지 않으면 음수 출력
else:
    print("음수")