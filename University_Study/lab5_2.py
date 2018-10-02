"""
챕터: day5
주제: 함수
문제:
문자열의 튜플을 매개변수로 받아서, 해당 문자열들을 ','로 한 줄에 연결하여 출력하는 함수 print_string을 정의한다.
소프트웨어공학과, 정보통신공학과, 글로컬IT학과, 컴퓨터공학과를 요소로 가지는 튜플을 매개변수로 해서 print_string을 호출한다.
작성자: 한현수
작성일: 2018.10.2.
"""
# 튜플을 ','로 한 줄로 출력하는 함수
def print_string(string): # string: 튜플, 이 함수는 튜플, 리스트, 딕셔너리만 사용 가능(인덱스를 이용한 함수 이기 때문이다.)
    for i in range(len(string)): # string의 끝부분 까지 반복한다.
        if len(string) - 1 == i: # 마지막 인덱스는 뒤에 ', '가 필요없으므로 if와 break로 튜플의 문자만 출력하게한다.
            print(string[i])
            break
        print(string[i], end=', ') # 순서대로 string의 문자를 출력하고 뒤에 ', '를 붙인다.

# 튜플을 ','로 한 줄로 출력하는 함수 두번째 방법
def print_string2(string):
    result = '' # result라는 변수에 ''를 저장
    for i in string:
        result += i + ', ' # i 뒤에 ', '를 붙이고 result에 더한다.
    return result[:-2] # 마지막에 ', '가 있으므로 슬라이스로 잘라서 리턴한다.

# 실행 코드 시작
t = ('소프트웨어공학과', '정보통신공학과', '글로컬IT학과', '컴퓨터공학과')
print_string(t)
print(print_string2(t))