# 파이썬 계산기의 함수 모듈(완성본)
    
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
    try:
        n = int(n)
    except:
        return "--> Error!"

    if n > 4999:
        return "--> Error!(표현할수 있는 최댓값 초과)" # 값이 로마숫자로 표현할 수 없을 정도로 큼.

    # 튜플과 사전 생성:
    numberBreaks = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
    letters = {
    1000 : "M", 900 : "CM", 500 : "D", 400 : "CD", 100 : "C", 90 : "XC", 50 : "L", 40 : "XL",
    10 : "X", 9 : "IX", 5 : "V", 4 : "IV",
    1 : "I" }

    # 알고리즘 시작:
    result = ""
    for value in numberBreaks:
        while n >= value:
            result = result+letters[value]
            n = n-value
    return result

# 10진수를 2진수로 변환하는 함수:
def to_binary(n):
    try:
        n = int(n)
        return bin(n)[2:]
    except:
        return "--> Error!"


# 2진수를 10진수로 변환하는 함수:
def from_binary(n):
    try:
        return int(n, 2)
    except:
        return "--> Error!"
