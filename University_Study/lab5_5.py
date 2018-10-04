"""
챕터: day5
주제: min 함수 이용
문제:
작성자: 한현수
작성일: 2018.10.4.
"""

"""
l 변수에 [4, 7, 9, 11, -5]를 저장한다.
l에서 최소값을 출력한다.
"""
l = [4, 7, 9, 11, -5] # iterable한 값
print(min(l)) # min의 첫번째 매개변수는 iterable한 값을 넘긴다.
print(max(l))

"""
fruits 변수에 'apple', 'orange', 'banana'를 tuple로 배정한다.
fruits에서 최소값과 최대값을 출력한다.
"""
fruits = ('apple', 'orange', 'banana')
print(min(fruits))
print(max(fruits))

"""
fruits 변수의 orange를 Orange로 변경한다.
fruits에서 최소값과 최대값을 출력한다.
"""
fruits = ('apple', 'Orange', 'banana')
print(min(fruits))
print(max(fruits))

"""
대소문자를 구분하지 않고 최대, 최소를 얻기위해 min, max 함수의 마지막 key 매개변수로
str.lower(모두 소문자로 바꾸어 비교)를 전달한다. (min(fruits, key=str.lower))
"""
fruits = ('apple', 'Orange', 'banana')
print((min(fruits, key=str.lower)))
print((max(fruits, key=str.lower)))

"""
1부터 50까지의 수 중 최대, 최소값을 출력한다.
"""
print(min(range(1,51)))
print(max(range(1,51)))

"""
min 함수에 직접 1, 3, 6 값을 전달하여 최소값 출력
"""
print(min(1, 3, 6))