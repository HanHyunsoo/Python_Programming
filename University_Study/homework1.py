"""
과제제출시스템 번호: 14
문제: Fraction 클래스(분수) 정의 하기
__str__, 사칙연산 기능(+,-,*,/)과 비교 연산(==,!=,<,<=,>,>=) 오버라이딩(재정의) 하기
음수 작동되게 하기(예: 1/-3 -> -1/3)
"""
# 클래스 정의
class Fraction:
    def __init__(self, n, d):
        """
        분수를 초기화하는 메소드
        :param n: 분자에 해당하는 값
        :param d: 분모에 해당하는 값
        """
        if n > 0 and d < 0: # 분모가 음수, 분자가 양수라면 분모를 양수, 분자를 음수로 바꾸어 -가 분자 앞으로 가게 한다.(예: 1/-3 -> -1/3)
            self.numer = -n
            self.denom = -d
        else:
            self.numer = n
            self.denom = d

    # 분수를 출력하는 함수
    def print(self):
        print("%d/%d" % (self.numer, self.denom))

    # 분수를 문자열로 반환하는 함수
    def __str__(self):
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
    def __add__(self, other):
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
    def __sub__(self, other):
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
    def __mul__(self, other):
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
    def __truediv__(self, other):
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

    # 분수의 비교(==)
    def __eq__(self, other):
        """
        :param other: self와 비교하는 함수
        :return: True 또는 False
        """
        # 분모와 분자를 통분시키면 두 분모의 값은 같다. 따라서 분자만 비교하면 되므로 분모까지 변수를 선언할 필요가없다.
        # self의 분자 통분
        n1 = self.numer * other.denom

        # other의 분자 통분
        n2 = other.numer * self.denom

        if n1 == n2: # 통분한 두 분수의 분자가 같으면 True를 반환하고 그외에는 False를 반환한다.
            return True
        else:
            return False

    # 분수의 비교(!=)
    def __ne__(self, other):
        """
        :param other: self와 비교하는 함수
        :return: True 또는 False
        """
        # self의 분자 통분
        n1 = self.numer * other.denom

        # other의 분자 통분
        n2 = other.numer * self.denom

        if n1 == n2: # 통분한 두 분수의 분자가 같으면 False를 반환하고 그외에는 True를 반환한다.
            return False
        else:
            return True

    # 분수의 비교(<)
    def __lt__(self, other):
        """
        :param other: self와 비교하는 함수
        :return: True 또는 False
        """
        # self의 분자 통분
        n1 = self.numer * other.denom

        # other의 분자 통분
        n2 = other.numer * self.denom

        if n1 < n2: # 통분한 두 분수에서 other의 값이 더 많으면 True를 반환 아니면 False를 반환한다.
            return True
        else:
            return False
        
    # 분수의 비교(<=)
    def __le__(self, other):
        """
        :param other: self와 비교하는 함수
        :return: True 또는 False
        """
        # self의 분자 통분
        n1 = self.numer * other.denom

        # other의 분자 통분
        n2 = other.numer * self.denom

        if n1 <= n2: # 통분한 두 분수에서 other의 값이 더 많거나 같으면 True를 반환 아니면 False를 반환한다.
            return True
        else:
            return False

    def __gt__(self, other):
        """
        :param other: self와 비교하는 함수 
        :return: True 또는 False
        """
        # self의 분자 통분
        n1 = self.numer * other.denom

        # other의 분자 통분
        n2 = other.numer * self.denom
    
        if n1 > n2: # 통분한 두 분수에서 self의 값이 더 많으면 True를 반환 아니면 False를 반환한다.
            return True
        else:
            return False

    def __ge__(self, other):
        """
        :param other: self와 비교하는 함수 
        :return: True 또는 False
        """
        # self의 분자 통분
        n1 = self.numer * other.denom

        # other의 분자 통분
        n2 = other.numer * self.denom

        if n1 >= n2:  # 통분한 두 분수에서 self의 값이 더 많거나 같으면 True를 반환 아니면 False를 반환한다.
            return True
        else:
            return False

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
            if i > 0:  # i가 양수면
                i -= 1  # i를 1씩 빼면서 반복한다.
            else:  # i가 음수면
                i += 1  # i를 1씩 증가하면서 반복한다.

        if i < 0: # i가 음수면 양수로 바꾼다.(음수에서 의도치 않은 값 변화가 일어날 수 있기 때문)
            i = -i

        # 분자와 분모를 구한 최대공약수로 나누고 반환한다.
        return Fraction(n / i, d / i)


# 프로그램 시작

# 변수 정의
a1, b1 = Fraction(-4, 5), Fraction(3, 2)
a2, b2 = Fraction(8, 31), Fraction(2, 3)
a3, b3 = Fraction(3, 5), Fraction(3, 7)
a4, b4 = Fraction(4, 8), Fraction(1, 2)
a5, b5 = Fraction(2, 81), Fraction(3, 9)

# 출력
print("%s * %s = %s" % (a1, b1, (a1 * b1).reduce()))
print("%s - %s = %s" % (a2, b2, (a2 - b2).reduce()))
print("%s + %s = %s" % (a3, b3, (a3 + b3).reduce()))
print("%s == %s의 결과: " % (a4, b4), a4 == b4)
print("%s >= %s의 결과: " % (a5, b5), a5 == b5)