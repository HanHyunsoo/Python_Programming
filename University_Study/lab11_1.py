"""
챕터: day6
주제: class
문제: 정수집합 클래스
1. intSet 클래스는 정수들의 집합이다. 정수들을 관리하는 리스트 self.vals를 애트리뷰트로 가진다.
2. 새로운 정수 e를 추가하는 insert 메소드. 해당 요소가 이미 있다면 추가하지않음
3. e가 정수집합에 포합되어 있는지 확인하는 메소드인 involve 정의(True, False 반환)
4. e를 제거하는 remove 메소드.
5. 단, e가 해당 집합에 없다면 적당한 오류 메세지를 출력.
6. 집합 형식의 문자열로 반환시켜주는 __str__메소드. 단, 정수들은 정렬되어 반환되어야 한다.
작성자: 한현수
작성일: 2018.11.1
"""
class intSet:
    def __init__(self):
        """
        :param vals: 정수들의 리스트
        """
        self.vals = []

    def insert(self, e):
        """
        :param e: 리스트에 추가하는 정수
        """
        if self.vals.count(e) == 0: # e가 self.vals에 없으면 e를 추가
            self.vals.append(e)

    def involve(self, e):
        """
        :param e: 리스트에 있는지 확인하는 정수
        :return: 정수가 있으면 True 없으면 False를 반환
        """
        if self.vals.count(e) > 0:
            return True
        else:
            return False

    def remove(self, e):
        """
        :param e: 리스트에 있으면 삭제하는 정수
        """
        if self.vals.count(e) > 0:
            self.vals.remove(e)
        else:
            print("해당 정수가 리스트에 없습니다.")

    def __str__(self):
        result = self.vals # 원래의 리스트가 변환되지 않기위해 변수를 하나 생성한다.
        result.sort()
        return "%s" % result

# 실행 부분
"""
A. intSet을 저장하는 변수 s를 정의
B. s에 insert를 이용하여 하나씩 5, 3, 7을 삽입
C. s를 정렬하여 출력
D. s에 8이 있는지 결과 출력
E. s에 3이 있는지 결과 출력
F. s에서 3을 제거
G. s에서 4를 제거
H. s를 정렬하여 출력
"""

# A
s = intSet()
# B
s.insert(5)
s.insert(3)
s.insert(7)
# C
print(s.__str__())
# D
print(s.involve(8))
# E
print(s.involve(3))
# F
s.remove(3)
# G
s.remove(4)
# H
print(s.__str__())
