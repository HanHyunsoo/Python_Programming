import os
"""
문제 5-1

두 개의 정수 값을 받아 두 값의 평균을 구하는 함수를 작성하세요.
"""
def myaverage(a, b):
    return (a + b) / 2

"""
문제 5-2

함수의 인자로 리스트를 받은 후 리스트 내에 있는 모든 정수 값에 대한
최댓값과 최솟값을 반환하는 함수를 작성하세요.
"""
def get_max_min(data_list):
    max_val = max(data_list)
    min_val = min(data_list)
    return (max_val, min_val)

"""
문제 5-3

절대 경로를 입력받은 후 해당 경로에 있는 *.txt 파일의 목록을
파이썬 리스트로 반환하는 함수를 작성하세요.
"""
def get_txt_list(path):
    os_file_list = os.listdir(path)
    result_txt_list = []
    
    for i in os_file_list:
        if i.endswith('txt'):
            result_txt_list.append(i)
            
    return result_txt_list

"""
문제 5-4

체질량 지수(BMI; Body Mass Index)는 인간의 비만도를 나타내는 지수로서 체중과 키의 관계로 아래의 수식을 통해 계산합니다.
여기서 중요한 점은 체중의 단위는 킬로그램(kg)이고 신장의 단위는 미터(m)라는 점입니다.

BMI=체중(kg) / 신장(m)2

일반적으로 BMI 값에 따라 다음과 같이 체형을 분류하고 있습니다.

BMI <18.5, 마른체형
18.5 <= BMI < 25.0, 표준
25.0 <= BMI < 30.0, 비만
BMI >= 30.0, 고도 비만

함수의 인자로 체중(kg)과 신장(cm)을 받은 후 BMI 값에 따라
'마른체형', '표준', '비만', '고도 비만' 중 하나를 출력하는 함수를 작성하세요.
"""
def BMI(kg, cm):
    m = cm * 0.01
    bmi = kg / (m**2)
    if bmi < 18.5:
        print("마른 체형")
    elif 18.5 <= bmi or bmi < 25.0:
        print("표준")
    elif 25.0 <= bmi or bmi < 30.0:
        print("비만")
    else:
        print("고도 비만")

"""
문제 5-5

위 문제와 동일
"""

"""
문제 5-6

삼각형의 밑변과 높이를 입력받은 후 삼각형의 면적을 계산하는 함수를 작성하세요.
"""
def get_triangle_area(width, height):
    return height * width / 2

"""
문제 5-7

함수의 인자로 시작과 끝을 나타내는 숫자를 받아 시작부터 끝까지의
모든 정수값의 합을 반환하는 함수를 작성하세요(시작값과 끝값을 포함).
"""
def add_start_to_end(start, end):
    return (sum(range(start, end + 1)))

"""
문제 5-8

함수의 인자로 문자열을 포함하는 리스트가 입력될 때 각 문자열의 첫 세 글자로만 구성된 리스트를 반환하는 함수를 작성하세요.
예를 들어, 함수의 입력으로 ['Seoul', 'Daegu', 'Kwangju', 'Jeju']가 입력될 때 함수의 반환값은 ['Seo', 'Dae', 'Kwa', 'Jej']입니다.
"""
def get_three_letters_to_list(data_list):
    result = []
    for i in data_list:
        result.append(i[0:3])
    return result
