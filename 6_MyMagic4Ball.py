# MyMagic4Ball

import random #random 모듈을 부름, c언어 헤더파일을 include 하는 것과 비슷?

ans1 = "슬픔"
ans2 = "기쁨"
ans3 = "행복"
ans4 = "화남"

your_name = input("당신의 이름을 입력하고 엔터 키를 누르세요.\n") #입력 받은 문자열을 저장
print("당신의 감정을 보는중...\n" *4)

emotion = random.randint(1,4) # 1~4중에 하나의 정수를 뽑고 emotion이라는 변수에 저장

if emotion == 1:
    print(your_name, "의 감정은 ", ans1, "입니다\n")
elif emotion == 2:
    print(your_name, "의 감정은 ", ans2, "입니다\n")
elif emotion == 3:
    print(your_name, "의 감정은 ", ans3, "입니다\n")
else:
    print(your_name, "의 감정은 ", ans4, "입니다\n")

input("마치려면 엔터 키를 누르세요.")
