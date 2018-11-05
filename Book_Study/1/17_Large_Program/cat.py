# cat.py
# class 구축

class Cat: # 클래스의 첫 글자는 대문자여야함.
    # 생성자
    def __init__(self, name): 
        self.name = name
    # 메서드
    def speak(self):
        print(self.name, "가 야옹합니다.")

    def drink(self):
        print(self.name, "가 우유를 마십니다.")
        print(self.name, "가 낮잠을 잡니다.")
