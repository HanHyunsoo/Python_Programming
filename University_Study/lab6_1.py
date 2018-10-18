"""
챕터: day6
주제: class
문제: 숫자를 하나씩 발생시키는 Counter 클래스 정의
작성자: 한현수
작성일: 2018.10.18.
"""
#관습적으로 Class 이름은 대문자로 시작함.

class Counter :
    #특별한 method
    def __init__(self):
        #instance를 생성할 때 초기화하는 method. instance를 생성할 때 자동 호출됨
        self.count = 0

    def __init__(self, start=0):
        self.count = start

    def reset(self): #Counter를 초기화하는 메소드
        #self는 method가 수행되는 instance자신을 의미
        #:return
        self.count=0

    def increment(self):
        self.count += 1

    def get(self):
        return self.count

#실행 코드 시작
#class Counter의 instance를 생성해서 변수 a에 저장
a = Counter()
#class Counter의 instance를 생성해서 변수 B에 저장. 매개변수를 포함하는 __init함수가 호출됨.
b = Counter(10)
a.reset()
a.increment()
a.increment()
a.increment()
print("%s" % a.get())

print("%s" % b.get())