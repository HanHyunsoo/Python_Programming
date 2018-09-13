"""
챕터: day3
주제: 리스트
작성자: 한현수
작성일: 2018.9.11
"""
# l에 [2, 4, 6, 8, 10]을 저장한 후 출력한다.
l = [2, 4, 6, 8, 10]
print(l)

# 0번째 요소값을 출력한다.
print(l[0])

# 3번째 요소값을 -8로 변경한다.
l[3] = -8
print(l)

# l에 12를 뒤에 붙여 추가한 후, l을 출력한다.
l.append(12)
print(l)

# l의 1의 위치에 -3을 삽입한 후, l을 출력한다.
l.insert(1, -3)
print(l)

# l의 1번째 요소를 삭제한 후, l을 출력한다.
del l[1]
print(l)

# l에 있는 -8 값을 제거한 후, l을 출력한다.
l.remove(-8) # 8이 리스트 내에 여러개인 경우, 첫번째 -8만 삭제
print(l)

# l에서 가장 마지막에 있는 요소를 꺼내어(리스트에서도 제거) 반환 받은 후 해당 요소를 출력한다. (pop() 함수)
print(l.pop())
print(l)

# 정렬 테스트를 위해 마지막에 작은 숫자 넣기
l.append(3)
print(l)

# l을 정렬하여 출력한다.
l.sort() # sort() 리턴값이 없다. l 자체가 정렬되어 변한다.
print(l)

# l을 거꾸로 출력한다.
l.reverse() # l 자체의 순서가 바뀐다.
print(l)

# l의 길이 출력
print(len(l))

# l의 2번째 요소 출력. 함수 이용
print(l.index(2))