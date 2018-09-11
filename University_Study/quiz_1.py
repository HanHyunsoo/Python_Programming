# 1. 다음 중 Python에서 제공하는 데이터 타입을 모두 고르시오
# int       O
# float     O
# str       O
# bool      O
# double    X
# char      X

# 2. var = input() 이 수행되었을 때, 사용자가 1을 입력했다고 가정하자. var 변수의 타입은?
# str       O
# int       X
# float     X
# 알 수 없음 X

# 3. str = "127345767"이라 가정할 때, str[2:4]를 쓰시오.
str = "127345767"
print(str[2:4])

# 4.위의 3에서 정의한 str에 s.count("7", 3)의 결과는?
print(str.count("7", 3))

#5. 위의 3에서 정의한 str의 5를 3으로 대체하는 문장을 써라.
print(str.replace("5", "3"))