s = "bar" # 문자열
t = ("b", "a", "r") # 튜플
l = ["b", "a", "r"] # 리스트
d = {1:"b", 2:"a", 3:"r"} # 사전

def print_data_type(a,b,c,d):
    print("\n원본 자료형들")
    print("1.",a,"(문자열)")
    print("2.",b,"(튜플)")
    print("3.",c,"(리스트)")
    print("4.",d,"(사전)\n")

functions = {
    "1":"모든 요소 출력",
    "2":"요소 출력",
    "3":"결합",
    "4":"요소 추가",
    "5":"정렬",
    "6":"요소 삭제",
    "7":"요소 치환",
    "8":"찾기",
    "9":"길이 얻음"
}

i = 1
while i <= 9:
    print(i,functions[str(i)])
    i += 1

user_input = input("\n위 번호중 한개를 입력하고 엔터를 쳐주세요.\n")

if user_input == "1":
    print("\n1.문자열\n2.튜플\n3.리스트\n4.사전\n")
    print(functions["1"])
    print("1.",s)
    print("2.",t)
    print("3.",l)
    print("4.",d,"\n")

elif user_input == "2":
    print_data_type(s,t,l,d)
    print(functions["2"])
    print("모든 자료형의 2번을 출력합니다.")
    print("1.",s[2])
    print("2.",t[2])
    print("3.",l[2])
    print("4.",d[2],"\n")

elif user_input == "3":
    print_data_type(s,t,l,d)
    print(functions["3"])
    print("모든 자료형에 ""f""를 결합합니다.")
    a=s+"f"
    print("1.",a)
    a=t+("f",)
    print("1.",a)
    a=l+["f"]
    print("1.",a)
    print("4. ?\n")

elif user_input == "4":
    print_data_type(s,t,l,d)
    print(functions["4"])
    print("모든 자료형에 ""f""라는 요소를 추가합니다")
    print("1. 안 됨")
    print("2. 안 됨")
    l.append("f")
    print("3.",l)
    d[4]="f"
    print("4.",d,"\n")

elif user_input == "5":
    print_data_type(s,t,l,d)
    print(functions["5"])
    print("모든 자료형을 정렬합니다.")
    print("1. 안 됨")
    print("2. 안 됨")
    l.sort()
    print("3.",l)
    sorted(d) # 키 값 배열
    print("4.",sorted(d.values()),"\n") # value 값 배열

elif user_input == "6":
    print_data_type(s,t,l,d)
    print(functions["6"])
    print("모든 자료형의 1번을 삭제합니다.")
    print("1. 안 됨")
    print("2. 안 됨")
    del l[1]
    print("3.",l)
    del d[1]
    print("4.",d,"\n")

elif user_input == "7":
    print_data_type(s,t,l,d)
    print(functions["7"])
    print("모든 자료형의 첫번째를 ""c""로 치환합니다.")
    print("1. 안 됨")
    print("2. 안 됨")
    l[0]="c"
    print("3.",l)
    d[1]="c"
    print("4.",d,"\n")

elif user_input == "8":
    print_data_type(s,t,l,d)
    print(functions["8"])
    print("모든 자료형에 ""b""의 인덱스 값을 찾습니다.(찾지 못 할경우 음수 반환)")
    print("1.",s.find("b"))
    print("2.",t.index("b"))
    print("3.",l.index("b"))
    print("4. ?\n")

elif user_input == "9":
    print_data_type(s,t,l,d)
    print(functions["9"])
    print("모든 자료형의 길이를 구합니다.")
    print("1.",len(s))
    print("2.",len(t))
    print("3.",len(l))
    print("4.",len(d),"\n")
else:
    print("\n입력된 값 오류\n")
