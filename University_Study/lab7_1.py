"""
챕터: day7
주제: os 모듈 사용
문제:
1. 현재 디렉토리를 출력한 후, 사용자로부터 파일을 생성할 디렉토리를 입력받고,
입력된 디렉토리로 이동한 후 해당 디렉토리 아래에 있는 모든 파일 목록을 한 줄에 하나씩 출력하라.
A. 만약, 입력한 디렉토리가 존재하지 않는다면, "입력한 디렉토리는 존재하지 않습니다."를 출력한다.
Exception으로 처리하라. 일부러 오류를 발생시켜 Exception의 이름을 파악하라.
작성자: 한현수
작성일: 2018.12.4
"""
import os

print("현재 디렉토리: %s" % os.getcwd())
move_dir = input("이동할 디렉토리: ")
try:
    os.chdir(move_dir)
except FileNotFoundError:
    print("입력한 디렉토리는 존재하지 않습니다.")
else:
    result = os.listdir(move_dir)
    if len(result) == 0:
        print("해당 폴더에 파일이 없습니다.")
    else:
        print("===파일 목록===")
        for i in result:
            print(i)