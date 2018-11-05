def problem(question, answer):
    if input(question) == answer:
        print("정답입니다.")
    else:
        print("틀렸습니다.")


d = {"파이썬을 윈도우 환경에 직접 설치하셨습니까? (O, X)\n답: ":"O",
     "파이썬 IDLE를 실행한 후 화면에 '주식은 대박이다.'라는 글자를 출력하게 코드를 작성해보세요.\n답: ":"print('주식은 대박이다.')",
     "파이썬에서 콘솔에 어떤 값을 출력할 때 사용하는 키워드는 무엇인가요?\n답: ":"print",
     """다음 다섯 가지 파이썬 표현 중 정상적으로 화면에 값이 출력되는 것을 고르시오.
1 - print("I love 'you'")
2 - print("I like you')
3 - print('Korea')
4 - print{Hello}
5 - print[Hello]
답: """:"1"
     }

for i in d:
    problem(i, d[i])
    print("\n")
