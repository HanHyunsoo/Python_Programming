"""
챕터: day4
주제: 반복문(for문)
문제: 사용자가 입력한 영문자를 아래와 같이 출력
(예)
BINGO
 INGO
  NGO
   GO
    O

작성자: 한현수
작성일: 2018.9.27.
"""
name = input()
for i in range(len(name)):
    print(" " * i + name[i:])

for i in range(len(name)): # 문자열 길이만큼 반복
    o = "" # 출력할 문자열 초기화
    for j in range(i): # 공백을 붙이기 
        o += " "
    for k in range(i, len(name)): # 출력할 문자 붙이기
        o += name[k]
    print(o)