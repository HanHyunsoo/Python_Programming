"""
과제번호: 19
문제: 클래스 상속
Shape를 계승하는 Circle, Triangle, Rectangle 클래스를 만든다.
"""
class Shape:
    # 면적 클래스
    def area(self):
        return 0

    # 둘레 클래스
    def perimeter(self):
        return 0
    
    def __str__(self):
        return "도형"

class Circle(Shape): # 원 클래스
    PI = 3.1415 # 클래스 변수

    def __init__(self, radius):
        """
        :param radius: 원의 반지름
        """
        self.radius = radius

    def area(self): # 원의 넓이
        return self.radius ** 2 * Circle.PI

    def perimeter(self): # 원의 둘레
        return self.radius * 2 * Circle.PI

    def __str__(self):
        return "<원> 반지름:%d" % self.radius

    def getRadius(self):
        return self.radius

class Triangle(Shape): # 삼각형 클래스
    def __init__(self, a, b, c, height):
        """
        :param a: 밑변
        :param b: 왼쪽 변
        :param c: 오른쪽 변
        :param height: 높이
        """
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def area(self): # 삼각형의 넓이
        return self.a * 0.5 * self.height

    def perimeter(self): # 삼각형의 둘레
        return self.a + self.b + self.c

    def __str__(self):
        return "<삼각형> 밑변:%d 높이:%d" % (self.a, self.height)

    def getHeight(self): # 높이를 반환하는 메소드
        return self.height

    def getWidth(self): # 밑변을 반환하는 메소드
        return self.a

    def getSides(self): # 변의 길이를 시계방향으로 list 형태로 반환하는 메소드
        return [self.a, self.b, self.c]

class Rectangle(Shape): # 직사각형 클래스
    def __init__(self, width, height):
        """
        :param width: 밑변
        :param height: 높이
        """
        self.width = width
        self.height = height

    def area(self): # 직사각형의 넓이
        return self.width * self.height

    def perimeter(self): # 직사각형의 둘레
        return (self.width + self.height) * 2

    def __str__(self):
        return "<직사각형> 밑변:%d 높이:%d" % (self.width, self.height)

    def getHeight(self): # 높이를 반환하는 메소드
        return self.height

    def getWidth(self): # 밑변을 반환하는 메소드
        return self.width

    def getSides(self):  # 변의 길이를 시계방향으로 list 형태로 반환하는 메소드
        return [self.width, self.height, self.width, self.height]

# 실행 코드
s = Shape() # s 변수는 도형
c = Circle(5) # c 변수는 반지름이 5인 원
r = Rectangle(5, 10) # r 변수는 가로, 세로가 5, 10인 직사각형
t = Triangle(3, 4, 5, 4) # t 변수는 세변이 3(밑변), 4, 5이고, 높이가 4인 삼각형

# c, r, t의 면적과 둘레 출력
print("c의 면적:%f, 둘레:%d" % (c.area(), c.perimeter()))
print("r의 면적:%d, 둘레:%d" % (r.area(), r.perimeter()))
print("t의 면적:%d, 둘레:%d" % (t.area(), t.perimeter()))

# t의 세변 리스트로 출력
print("t의 리스트:%s" % t.getSides())

# 리스트 l을 정의하여, s, c와 r을 요소로 추가
l = []
l.append(s)
l.append(c)
l.append(r)

# l의 각 요소에 대해, 해당 요소를 출력하고, 면적과 둘레를 계산하여 출력
for i in l:
    if str(i) == "도형": # s는 area(), perimeter() 메소드가 정의되지 않아서 오류가남
        print(i)
    else:
        print(i, ", 면적:%f, 둘레:%d" % (i.area(), i.perimeter()))

# for문 안에서 테스트: getRadius() 메쏘드를 수행한다.(오류 발생)
for i in l:
    try:
        print("원의 반지름:%d" % i.getRadius()) # c의 클래스에는 getRadius 메소드가 있어서 정상적으로 작동되지만 나머지 변수는 메소드가 정의가 안되있어 오류가 난다.
    except:
        print("%s 은(는) getRadius() 함수를 사용할 수 없습니다." % i) # 오류가 나는 부분을 예외처리한다.