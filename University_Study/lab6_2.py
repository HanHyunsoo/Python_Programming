"""
챕터: day6
주제: class
문제:
좌표를 표현하는 클래스 Coordinate를 정의한다.
1. __init__는 x, y 좌표를 받아서 self의 x, y에 배정
2. c. 거리를 구하는 distance 메소드를 정의한다. self와 다른 좌표 other를 매개변수로 받는다.
(거리는 x좌표 사이의 차의 제곱(**2)과 y좌표 사이 차의 제곱의 합의 제곱근이다. )
작성자: 한현수
작성일: 2018.10.18.
"""
class Coordinate :
    def __init__(self, x, y):
        """
        python에서는 __init__함수를 한 클래스 당 하나만 정의할 수 있음.
        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def distance(self, other):
        """
        두 좌표의 거리를 계산하여 반환
        :param other: 다른 좌표
        :return: self와 other와의 거리를 반환
        """
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5

# 실행 코드 시작

c = Coordinate(3, 4)
origin = Coordinate(0,0)
c1 = Coordinate(10, 9)

print("거리: %f" % c.distance(origin))# origin이 self, c가 other에 전달됨
print("거리: %f" % c1.distance(c)) #c1이 self c가 other에 전달됨
print("거리: %f" % Coordinate.distance(c1, origin)) #class 이름과 함께 메소스 호출 가능. 이때는 self에 해당되는 매개변수를 보내야 한다.
