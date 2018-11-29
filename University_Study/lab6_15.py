"""
챕터: day6
주제: raise exception
문제: 사용자로부터 2개의 정수를 입력받은 후 아래와 같은 메뉴를 선택하게 하여 그 결과를 출력하라.
1. 덧셈
2. 뺄셈
3. 나눗셈
4. 곱셈
만약 메뉴 입력시 사용자가 1~4 사이의 수가 아니면, "메뉴를 다시 선택해 주세요"를 출력한 후 다시 입력받는다.
나눗셈의 경우, 두번째 수가 0이면 "0으로 나눌 수 없습니다."를 출력한다.
만약 2개의 정수를 입력받을 때, 정수가 아닌 수를 입력하면 "정수를 입력하세요"를 출력한다.
위 세가지 경우를 exception을 이용하여 처리하라.
작성자: 한현수
작성일: 2018.11.29
"""
# while 1:
#     try:
#         a = int(input("a의 값: "))
#         b = int(input("b의 값: "))
#         break
#     except ValueError:
#         print("정수를 입력하세요.")
print("""1. 덧셈
2. 뺄셈
3. 나눗셈
4. 곱셈""")
while 1:
    try:
        menu = int(input())
        if (menu < 1 or menu > 4):
            raise ValueError

        while 1:
            try:
                a = int(input("a의 값: "))
                b = int(input("b의 값: "))
                break
            except ValueError:
                print("정수를 입력하세요.")

        if menu == 1:
            print("%d + %d = %d" % (a, b, a + b))
        elif menu == 2:
            print("%d - %d = %d" % (a, b, a - b))
        elif menu == 3:
            if b == 0:
                raise ZeroDivisionError
            print("%d / %d = %f" % (a, b, a % b))
        else:
            print("%d * %d = %d" % (a, b, a * b))
        break
    except ValueError:
        print("메뉴를 다시 선택해 주세요.\n메뉴선택: ", end = '')
    except ZeroDivisionError:
        print("0으로 나눌수 없습니다.\n메뉴선택: ", end = '')