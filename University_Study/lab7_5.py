"""
챕터: day7
주제: file 읽기
문제:
fruits.txt 파일에 저장되어 있는 과일 이름들을 출력하라. 몇 줄의 과일이 저장되었든지 상관없이 출력됨을 보장하라.
내가 산 과일의 합.
작성자: 한현수
작성일: 2018.12.6
"""
f = open("C:\\temp\\fruits.txt", "r")
lines = f.readlines()
f.close()
sum = 0
for i in lines:
    test = i.split(" : ")
    print("과일명: %s, 과일가격: %d" % (test[0], int(test[1][:-1])))
    sum += int(test[1][:-1])
print("과일 가격의 총합: %d" % sum)