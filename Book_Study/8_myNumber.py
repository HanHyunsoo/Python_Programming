import random

computer_number = random.randint(1, 100) #1~100 에서 정수 하나를 변수에 저장

def is_same(target, number):
    if target == number:
        result = "Win"
    elif target < number:
        result = "High"
    else:
        result = "Low"
    return result

print("1~100에서 숫자 하나를 골랐습니다.")

guess = int(input("숫자를 입력하고 엔터를 누르면 게임을 시작합니다.\n"))

higher_or_lower = is_same(computer_number, guess)

while higher_or_lower != "Win":
    if higher_or_lower == "High":
        guess = int(input("Down\n"))
    else:
        guess = int(input("Up\n"))

    higher_or_lower = is_same(computer_number, guess)

input("정답입니다!\n마치려면 엔터 키를 누르세요.")
