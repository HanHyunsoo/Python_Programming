number = "Hi" # number 변수에 str형 문자열 저장
print(number) # 문자열 출력
number = 10 # number 변수에 int형(숫자에 따라 float형으로 저장되기도 함) 정수 저장
print(number) # 정수형 출력

# 변수 a, b에 값을 저장한 후, 합을 c 변수에 저장 후, c를 출력
a, b = 4, 5
c = a + b
# 4 + 5 = 9 와 같이 출력하라
msg = "%d + %d = %d" # 출력하려는 문자열을 변수로 정의할 수도 있다.
print(msg % (a, b, c)) # 서식문자가 여러개가 있을경우 괄호를 이용해 구분한다.

# 문자열 출력
money = 100000
print("나는 현재 %d원이 있습니다." % money) # 서식문자를 이용할 수 있다. , 없이 변수이름 앞에 %를 붙인다.(c언어와 용도는 같지만 방법이 다름)

# 입력
money = input("얼마를 가지고 계세요?") # input함수는 따로 형변환을 안하면 문자열로 저장됨.(int(input()):int형,float(input()):float형)
print("입력하신 값은 %s입니다." % money) # money의 타입이 문자열이므로 %s를 사용