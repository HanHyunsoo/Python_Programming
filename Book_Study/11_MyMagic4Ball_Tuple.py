# MyMagic4Ball_Tuple

import random

answers = ("슬픔", "기쁨", "행복", "화남")

your_name = input("당신의 이름을 입력하고 엔터 키를 누르세요.\n")
print("당신의 감정을 보는중...\n" *4)

emotion = random.randint(0,3)

print(your_name, "의 감정은 ",answers[emotion], "입니다\n")

input("마치려면 엔터 키를 누르세요.")
