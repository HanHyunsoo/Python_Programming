# 15_GuessMyPassword.py
# 변수,조건문, 함수, 반복문, 모듈 복습

import random

# 변수 초기화
response1 = "걱정말고 다시 시도해보세요."
response2 = "그럴 듯하지만 내 비밀번호는 아니에요. 다시 입력해보세요."
response3 = "내 비밀번호가 아니에요. 내 비밀번호는 정말 쉬워요"
response4 = "잘했어요!"
MY_PASSWORD = "my password"

# 플레이어가 입력한 비밀번호가 올바른지 확인하는 함수
def is_correct(guess, password):
    if guess == password:
        guess_correct = True
    else:
        guess_correct = False
    return guess_correct

# 게임 시작
users_guess = input("안녕하세요.\n추측한 내 비밀번호를 입력하세요.\n")

# 함수를 사용하여 입력한 비밀번호가 일치하는지 확인
true_or_false = is_correct(users_guess, MY_PASSWORD)

# 사용자가 입력한 비밀번호가 일치할 때까지 게임 실행
while true_or_false == False:
    computer_response = random.randint(1, 3)
    if computer_response == 1:
        print(response1)
    elif computer_response == 2:
        print(response2)
    else:
        print(response3)

    # 사용자에게 다시 시도할 비밀번호 입력 요청
    users_guess = input("\n다음 비밀번호는 무엇입니까?\n")

    # 비밀번호가 일치하는지 재확인
    true_or_false = is_correct(users_guess, MY_PASSWORD)

# 게임 종료
print(response4)
input("\n\n\n엔터 키를 눌러 종료하세요.")

