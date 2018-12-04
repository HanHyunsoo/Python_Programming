"""
챕터: day7
주제: os 모듈 사용
문제:
사용자가 입력한 디렉토리(1)로 이동한 후, 사용자가 입력한 이름의 새 디렉토리(2)를 생성하라.
사용자가 입력한 디렉토리(2) 아래에 test 디렉토리를 생성하라.
사용자가 입력한 디렉토리를 포함하여 해당 디렉토리(2)와 test 디렉토리를 삭제하라.
삭제가 끝난 후, 사용자가 입력한 디렉토리(1)의 부모 디렉토리의 파일 목록을 출력하라.
작성자: 한현수
작성일: 2018.12.4
"""
import os
import time

move_dir = input("이동할 디렉토리: ")
try:
    os.chdir(move_dir)
except FileNotFoundError:
    print("입력한 디렉토리는 존재하지 않습니다.")
else:
    make_dir = input("생성할 폴더명: ")
    try:
        os.mkdir(make_dir)
        os.mkdir("test")
    except FileExistsError:
        print("\n생성할 폴더명이 이미 존재합니다.")
    else:
        print("\n%s, %s폴더를 삭제합니다" % (make_dir, "test"), end='')
        os.rmdir(make_dir)
        os.rmdir("test")
        for i in range(3):
            print(".", end='')
            time.sleep(0.75)
        print("\n삭제 완료.")
        time.sleep(1)
    finally:
        os.chdir("..")
        result = os.listdir(os.getcwd())
        if len(result) == 0:
            print("\n이동된 디렉토리의 부모 디렉토리에서 파일이 존재하지 않습니다.")
        else:
            print("\n====이동된 디렉토리의 부모 디렉토리 파일 목록====")
            for i in result:
                print(i)