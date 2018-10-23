"""
챕터: day6
주제: class
문제:
fraction 클래스는 애트리뷰트로 numer(분자)와 denom(분모)를 가진다. 초기화하는 메소드를 정의하라.
attribute(속성) = member(variable)
작성자: 한현수
작성일: 2018.10.23.
"""
# 분수 클래스 정의
class Fraction:
    def __init__(self, n, d):
        """
        분수를 초기화하는 메소드
        :param n: 분자에 해당하는 값
        :param d: 분모에 해당하는 값
        """
        self.numer = n
        self.denom = d
    
    # 분수를 출력하는 함수
    def print(self):
        print("%d/%d" % (self.numer, self.denom))
    
    # 분수를 문자열로 반환하는 함수
    def string(self):
        return "%d/%d" % (self.numer, self.denom)

    # 분자를 반환하는 메소드 getNumer 정의
    def getNumber(self):
        return self.numer

    # 분모를 반환하는 메소드 getDenom 정의
    def getDenom(self):
        return self.denom

    # 값을 수정하는 메소드 setNumer, setDenom 정의
    def setNumer(self, n):
        self.numer = n

    def setDenom(self, d):
        self.denom = d

    # 분수의 더하기
    def add(self, other):
        """
        self에 o를 더하여 결과 값을 반환.
        self 값을 변경하지 않는다.
        :param other: self와 더할 분수
        :return: 더한 결과 값을 반환
        """
        # 결과의 분모 계산
        d = self.denom * other.denom
        # 결과의 분자 계산
        n = self.numer * other.denom + other.numer * self.denom
        
        # 결과의 분모, 분자 result 변수에 저장
        result = Fraction(n, d)
        
        # result 반환
        return result

    # 분수의 빼기
    def sub(self, other):
        """
        :param other: self에 빼는 분수
        :return: 뺀 결과 값을 반환
        """
        # 분모 계산
        d = self.denom * other.denom
        # 분자 계산
        n = self.numer * other.denom - other.numer * self.denom

        # 결과의 분모, 분자 result 변수에 저장.
        result = Fraction(n, d)

        # result 반환
        return result

    # 분수의 곱셈
    def mul(self, other):
        """
        :param other: self와 곱하는 함수
        :return: 곱한 결과 값은 반환
        """
        # 분모 계산
        d = self.denom * other.denom
        # 분자 계산
        n = self.numer * other.numer

        # 결과의 분모, 분자 result 변수에 저장.
        result = Fraction(n, d)

        # result 반환
        return result

    # 분수의 나눗셈
    def div(self, other):
        """
         :param other: self를 나누는 함수
         :return: 나눈 결과 값은 반환
         """
        # 나눗셈 방식 예: (1/2) / (2/3) = (1/2) * (3/2)

        # 분모 계산
        d = self.denom * other.numer
        # 분자 계산
        n = self.numer * other.denom

        # 결과의 분모, 분자 result 변수에 저장.
        result = Fraction(n, d)

        # result 반환
        return result

    # 분수의 약분
    def reduce(self):
        """
        :return: 약분한 결과값 반환
        """
        # n, d, i 변수 저장
        n = self.numer
        d = self.denom
        i = min(n, d)  # 분자와 분모 둘중에 작은것을 i에 저장한다.

        # 최대 공약수를 구하기 위한 while 문.
        while 1:
            if (n % i == 0 and d % i == 0) or i == 1:  # i가 분자와 분모 모두 나누어 떨어진다면 최대공약수가 구해졌으므로 while문을 멈춘다.(또는 i가 1이면)
                break
            if i > 0: # i가 양수면
                i -= 1  # i를 1씩 빼면서 반복한다.
            else: # i가 음수면
                i += 1 # i를 1씩 증가하면서 반복한다.

        if i < 0: # i가 음수면 양수로 바꾼다(분모에 -가 앞에 붙어있을 수 있기 때문)
            i = -i

        # 분자와 분모를 구한 최대공약수로 나누고 반환한다.
        return Fraction(n / i, d / i)

# 클래스 정의 끝

case = int(input("1: 수업 시간 내용, 2: 과제\n입력: "))
if case == 1:
    # 실행 코드 시작
    half = Fraction(1, 2) # 1/2 분수 객체 생성하여 half에 저장, class Fraction의 __init__메소드가 호출됨
    half.print() # self 매개변수에는 half가 직접 전달된다.

    # 분수 2/7을 저장하는 변수 f1 정의
    f1 = Fraction(2, 7)

    # 분수 2/7을 저장하는 변수 f1을 출력
    f1.print()
    f1.print()

    # 분수 1/8을 저장하는 변수 f2를 정의
    f2 = Fraction(1, 8)

    # f2의 분자를 가져와서 다음 형식으로 출력
    # 분자: 1
    print("분자: %d" % f2.getNumber())

    # f2의 분모를 가져와서 다음 형식으로 출력
    print("분모: %d" % f2.getDenom())

    # f2의 타입을 출력
    print(type(f2))

    # 어떤 타입의 인스턴스인지 불리언 값을 반환하는 isinstance() 함수 호출하여 출력.
    print(isinstance(f2, Fraction))

    # f2를 2/8로 수정하여 출력
    f2.setNumer(2)
    f2.print()

    # f1과 f2를 더한 결과를 출력
    f1.add(f2).print() # f1.add()의 반환 타입이 Fraction이므로 클래스 안에있는 print()함수를 사용가능.
elif case == 2:
    # f1, f2 클래스 Fraction 정의
    f1 = Fraction(1, 2)
    f2 = Fraction(5, 4)

    # FourCalculation이라는 딕셔너리를 만들고 사칙연산의 4개의 클래스 객체를 reduce 함수로 먼저 약분한다음 키로 저장하고 각각 맞는 기호를 밸류 값으로 저장.
    FourCalculation = {f1.add(f2).reduce():'+', f1.sub(f2).reduce():'-', f1.mul(f2).reduce():'*', f1.div(f2).reduce():'/'}

    for i in FourCalculation:  # 1번째 문자열: f1의 분자(문자열), 2번째 문자열: 밸류값(+, -, *, /), 3번째 문자열: f2의 분자(문자열), 4번째 문자열: 각각 키들에 대한 사칙연산으로 구한 분자(문자열)
        print("%s %s %s = %s" % (f1.string(), FourCalculation[i], f2.string(), i.string()))
else:
    print("오류")
