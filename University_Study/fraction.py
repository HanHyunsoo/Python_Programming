def gcm(x, y):
    if y > x:
        temp = y
        y = x
        x = temp

    # 유클리드 호제법에 의해 최대공약수를 구함
    while y > 0:
        r = x % y
        x = y
        y = r

    return x

class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __str__(self):
        return "%d/%d" % (self.n, self.d)

    def __add__(self, other):
        d = self.d * other.d
        n = self.n * other.d + other.n * self.d
        g = gcm(n ,d)
        result = Fraction(n // g, d // g)
        return result

    def __eq__(self, other):
        g1 = gcm(self.n, self.d) # 약분을 위해 분모와 분자의 gcm 구하기
        g2 = gcm(other.n, other.d) # 다른 분수의 약분을 위해 분모와 분자의 gcm 구하기
        if (self.n//g1 == other.n//g2) and (self.d//g1, other.d//g2): # 최대 공약수로 나누어 약분한 후 분자, 분모 모두 같으면 True
            return True
        else:
            return False

f1 = Fraction(4, 5)
f2 = Fraction(3, 5)
print(f1.__add__(f2))

f3 = Fraction(8, 10)

print(f1.__eq__(f3))
print(f2.__eq__(f3))