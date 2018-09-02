# (소괄호): 튜플
# [대괄호]: 리스트
# {중괄호}: 사전

# 튜플: 문자열, 숫자, 다른 자료형 저장 가능
my_tuple = ( "a", "b", "c", "d", 1, 2, 3, 4)
i = 0
while i <= 7:
    print(my_tuple[i])
    i += 1

print("")

# 리스트: 튜플과 비슷하지만 함수로 항목을 삽입하거나 삭제할 수 있다.
my_list = [ 1, 2, 3, 4, "a", "b", "c", "d" ]
i = 0
while i <= 7:
    print(my_list[i])
    i += 1

print("")

# 사전: 항목을 가르키는 고유한 키(문자열, 정수, 실수, 튜플)를 가진다.
my_dictionary = { 1:"고양이", 2:"개", "1":"말", "2":"물고기" }
print(my_dictionary[1])
print(my_dictionary["2"])
