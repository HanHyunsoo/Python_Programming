"""
챕터: day 3
주제: 여러 타입을 포함한 리스트
작성일: 2018.9.13
작성자: 한현수
"""
# l에 [1, 2, [3, 'John', 4], 'Hi']를 저장한다.
l = [1, 2, [3, 'John', 4], 'Hi']

# l의 세번째 요소를 출력한다,
print(l[3])

# l의 두번째 요소를 출력한다.
print(l[2])

# 2라는 값이 있는 위치 출력.
print(l.index(2))

# l의 두번째 요소의 첫번째 요소를 출력한다.
print(l[2][1])

# l의 두번째 요소의 첫번째 요소의 앞의 세글자만 출력한다.
print(l[2][1][:3])

# in 연산 연습
print(2 in l)

# l에 3이 있으면 True 아니면, False를 출력하라.
print(3 in l)

# l의 두번째 요소안에 3이 있으면 True 아니면 False를 출력하라.
print(3 in l[2])

l[1] = 8 # mutable하다. list는 mutable한 데이터 타입이다.
print(l)