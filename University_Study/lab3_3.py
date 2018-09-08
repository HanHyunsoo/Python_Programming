"""
챕터: day 3
주제: 문자열 함수
작성자: 한현수
작성일: 2018.9.6.
"""
s = "Test your Python debugging skills"
print(s.upper()) # 대문자로 변환
print(s.lower()) # 소문자로 변환

# 문자열 안의 t의 개수를 출력
print(s.count('t'))
print(s.count('T'))

# 사용자로부터 문자를 입력 받아, 대소문자 구분 없이 해당 문자의 개수를 출력
c = input("문자 입력: ") # 사용자로부터 문자 입력 받기
s1 = s.upper() # 비교되는 문자열을 대문자로 변환하여 s1에 저장
print(s)
print(s1)
print(s1.count(c.upper())) # 비교되는 문자를 대문자로 변환하여 개수를 계산

# t가 있는 위치를 출력
print(s.index('t'))
print(s.index('t', 4)) # 두번째 매개변수는 검색 시작 위치

# index() 함수는 찾으려는 문자가 없으면 오류 방생
# print(s.index('x'))

# 대상 문자를 찾을 수 있는 또 다른 함수
print(s.find('t'))
print(s.find('x')) # 찾고자하는 문자가 해당 문자열에 없으면 -1을 반환

# strip() 함수 테스트
print(s)
# 왼쪽 공백 제거후 출력
print(s.lstrip())
# 오른쪽 공백 제거후 출력
print(s.rstrip())
# 양쪽 공백 제거후 출력
print(s.strip())

# 내용 바꾸기
# 문장에서 Python을 Java로 바꾸어 출력
print(s.replace('Python', 'Java')) # replace가 s 자체를 변경하지는 않는다.
print(s)

# 문장에서 e를 i로 모두 바꾸어 출력
print(s.replace('e', 'i', 1)) # 세번째 매개변수는 변경할 최대 개수를 지정

# split 연습
# 앞 뒤 공백을 제거한 후 빈칸을 기준으로 단어를 모두 나누기
print(s.strip().split(" "))
print(s.strip().split(" ", 2)) # 두 개만 떼어 내기

# s의 길이 출력
print(len(s))

s = 'test'
s = 'kkk'
s = '''
Kim
Yee
Hi
'''

i = input("문자열: ") # i의 데이터 타입은 문자열. input은 문자열을 반환하기 때문.
i = int(input("정수: ")) # i의 데이터 타입은 int형. input은 정수를 반환하기 때문.

j = 100 # j는 int
s1 = str(j) # s1은 str타입