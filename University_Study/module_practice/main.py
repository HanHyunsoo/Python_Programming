"""
실행부
A. s 변수는 도형이다.
B. 반지름이 5인 원을 정의하여 c 변수에 저장한다.
C. 가로, 세로가 5, 10인 직사각형을 정의하여 r에 저장한다.
D. 세변이 3(밑변), 4, 5이고, 높이가 4인 삼각형을 정의하여 t에 저장한다.
E. c의 면적과 둘레를 출력한다.
F. r의 면적과 둘레를 출력한다.
G. t의 면적과 둘레를 출력한다.
H. t의 변들을 리스트로 받아 출력한다.
"""
# 필요한 모듈 수입하기
import shape

s = shape.Shape() # shape.의 의미는 "shape.ps에서 정의된" 을 의미
                  # Shape가 shape.ps에 정의된 클래스임을 의미
c = shape.Circle(5)
r = shape.Rectangle(5, 10)
t = shape.Triangle(3, 4, 4, 5)
print(c.area())
print(c.perimeter())
print(r.area())
print(r.perimeter())
print(t.area())
print(t.perimeter())
print(r.getSides())

l = [s, c, r, t]
for i in l:
    print(i)