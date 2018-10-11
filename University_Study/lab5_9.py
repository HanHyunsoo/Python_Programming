"""
챕터: day5
주제: 매개변수의 전달 방식 비교(call-by-reference), 전역변수(global variable)
문제:
1. list를 받아서, 마지막 리스트의 요소의 개수를 요소로 추가하는 함수 addNum을 정의한다. 반환되는 값은 없다.
2. [5, 9, 14, 3]을 저장하는 list를 변수 l를 정의한다.
3. 을 인수로 addNum함수를 호출한 후 l을 출력한다.
작성자: 한현수
작성일: 2018.10.11.
"""
# 매개변수의 수정 여부 확인을 위한 함수 정의
# call-by-reference 방식으로 매개변수 값을 전달
global_v = 100 # 전역 변수

def addNum(l):
    global global_v
    global_v = 200
    l.append(len(l))

l = [5, 9, 14, 3]
addNum(l)
print(l)
print(global_v)