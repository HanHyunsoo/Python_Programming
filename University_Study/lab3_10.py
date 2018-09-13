"""
챕터: day 3
주제: set(특징: mutable)
작성일: 2018.9.13
작성자: 한현수
"""
s = {7, 8, 9} # set은 순서 의미 없음. 중복은 허용하지 않는다.
fruits = {'a':'사과', 'b':'배', 'c':'복숭아', 'd':'딸기'}
print(s)

# 딕셔너리를 set으로 변환하기
print(set(fruits)) #키 값만 set으로 변환된다.

# [3, 4, 5]를 set으로 형변환하여 s에 저장하고, 이를 출력하라.
print(set([3, 4, 5]))

# 인덱스를 사용할 수 없음. 위치가 의미 없으므로.
s.add(10)
print(s)

# remove로 삭제
s.remove(10)
print(s)

# 정렬한 결과가 넘어옴
print(sorted(s))