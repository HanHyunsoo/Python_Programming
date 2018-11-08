"""
챕터: day6
주제: class, 상속/계승
문제: 정수집합 클래스
작성자: 한현수
작성일: 2018,11,8
"""
"""
1. 사람 클래스를 정의한다.  이름과 나이를 (data) attribute로 가지고 있다.
A. 이름과 나이를 배개변수로 받는 생성자가 있다.
B. 나이를 1살 더하는 getOlder 메소드가 있다.
C. 문자열 반환, 프린트 메소드
"""
class Person:
    def __init__(self, name, age):
        """
        :param name: 이름
        :param age: 나이
        """
        self.name = name
        self.age = age

    def getOlder(self):
        self.age += 1

    def __str__(self):
        return "이름: " + self.name + ", 나이: " + str(self.age)

    def print(self):
        """
        내용을 출력
        """
        print(self)

"""
3. 사람을 계승하는 학생 클래스를 정의한다. 학교와 학년, 학번을 data attribute로 가지고 있다.
A. 이름, 나이, 학년, 학번을 받는 생성자가 있다. 생성자 내에서 사람의 생성자(Person, __init__)을 호출한다.
B. 학년을 진급하는 upgrade() 메소드가 있다
C. 문자열 반환(override), 프린트 메소드
"""

class Student(Person):
    def __init__(self, name, age, grade, tag):
        """
        생성자 내에서 사람의 생성자(Person.__init__)을 호출한다.
        Student도 일종의 Person이다.
        Person이라서 가지고 있는 attribute면 age와 name은
        Person의 생성자를 통해 초기화한다.
        """
        Person.__init__(self, name, age)
        self.grade = grade
        self.tag = tag
        self.school = "성공회대학교"

    def upgrade(self):
        self.grade += 1

    def __str__(self):
        """
        :return: Person에서 정의한 __str__ + 학년, 학번
        """
        return Person.__str__(self) + ", 학교: " + self.school + ", 학년: " + str(self.grade) + ", 학번: " + str(self.tag)

    def print(self):
        """
        Person 클래스에서 정의된 print()를 overriding 한다
        """
        print(self)
        

# 실행부
# 두 명의 Person instance를 만들어서 나이를 한살 올린 후 출력한다,

p1 = Person("주동석", 21)
p1.getOlder()
print(p1)

p2 = Person("한현수", 20)
p2.getOlder()
print(p2)

# 두 명의 Student instance를 만든다.
s1 = Student("박 결", 27, 1, 201811111)
s1.getOlder() # s1은 Student이지만 Person을 계승했으므로 Person 안에있는 메소드를 사용 가능
s1.upgrade()
print(s1)

s2 = Student("함진경", 22, 3, 201611111)
s2.getOlder()
s2.upgrade()
print(s2)

# Person과 Student를 포함하는 리스트 생성
l = [p1, p2, s1, s2]
for i in l:
    print(i)