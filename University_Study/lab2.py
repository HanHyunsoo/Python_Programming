# 이름을 직접 출력하세요.
print("한현수")

# 이름을 변수 name에 저장하여, name을 출력하세요.
name = "한현수"
print(name)

# 나이를 변수 age에 저장하여, age를 출력하세요.
age = 20
print(age)

# 이름을 입력 받아 변수에 저장한 후 출력하세요.
name = input()
print("이름: %s" % name)

# 나이를 입력 받아 변수에 저장한 후 출력하세요.
age = input()
print("나이: %s" % age)

# 이름과 나이를 입력받아, "나의 이름은 홍길동이고, 21세입니다." 형식으로 출력하세요. 변수와 서식문자를 이용해야 합니다. 출력문자열도 변수로 저장하여 처리한다.
name, age = input(), input()
print("나의 이름은 %s이고, %s세입니다." % (name, age))