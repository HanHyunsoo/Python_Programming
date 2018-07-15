# 파이썬 계산기의 함수 모듈(미완성본)
    
# 팩토리얼 함수:
def factorial(n):
    try:
        n = int(n)
    except:
        return "--> Error!" # 아래 오류들을 제외한 오류들.

    if n == 0:
        return 1 # 0! = 1
    
    if n > 40:
        return "--> Error!(표현할수 있는 최댓값 초과)" # 값이 너무 많음

    if n < 0:
        return "--> Error!(음수값 X)" # 팩토리얼은 음수가 안됨

    # 팩토리얼 알고리즘
    result = 1
    for i in range(1, n+1): # 1~n까지 result에 계속 i를 곱셈한다.
        result *= i
    return result
    
# 로마 숫자로 변환하는 함수:
def to_roman(n):
    return "-> roman"

# 10진수를 2진수로 변환하는 함수:
def to_binary(n):
    return "-> binary"

# 2진수를 10진수로 변환하는 함수:
def from_binary(n):
    return "binary -> 10"
