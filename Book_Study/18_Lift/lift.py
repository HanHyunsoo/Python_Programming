# Lift 클래스가 있는 lift.py

class Lift:
    # 생성자
    def __init__(self, current_floor = 0):
        self.current_floor = current_floor
    # 메서드
    def get_floor(self):
        return self.current_floor
    def move_to_floor(self, floor_number):
        self.current_floor = floor_number
