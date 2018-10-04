"""
챕터: day5
주제: 함수
문제:
이름, 학번, 학과를 매개변수로 받아서 이를 출력하는 함수 print_me 함수를 정의한다. 이때. 학과가 매개변수로 넘어오지 않으면, "소프트웨어공학과"를 디폴트 값으로 한다.
작성자: 한현수
작성일: 2018.10.4.
"""
def print_me(name, student_number, department='소프트웨어공학과'):
    print("이름: %s, 학번: %s, 학과: %s" % (name, student_number, department))

print_me('한현수', '201814043')
print_me('한현수', '201814043', '영어학과')