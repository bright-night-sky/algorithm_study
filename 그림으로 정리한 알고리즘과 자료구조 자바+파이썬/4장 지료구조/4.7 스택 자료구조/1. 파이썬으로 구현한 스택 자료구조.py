# 스택(Stack) : 데이터가 입력되면 입력되는 순서대로 쌓고, 나중에 들어온 것부터 먼저 사용하는 자료구조
# 스택 형태의 데이터 구조 : LIFO(Last In First Out)
# 스택에 데이터를 넣는 것 : push
# 스택에서 데이터를 꺼내는 것 : pop
# 스택의 구현은 배열, 연결 리스트 아무거나 이용해도 됨

# 스택은 대표적으로 프로그램을 수행할 때 사용
# 주 프로그램에서 함수 A를 호출하면 주 프로그램 위에 함수 A가 쌓이고, 함수 A의 수행 중에 함수 B가 호출되면, 함수 A 위에 함수 B가 스택처럼 쌓인다.
# 함수 B의 실행이 완료되면 함수 A가 실행되고, 함수 A의 실행이 완료되면 주 프로그램의 실행이 시작된다.

# 스택 자료구조는 일반적으로 프로그램의 수행 과정에서 함수를 불러 수행하는 경우
# 컴퓨터에서 수식의 연산을 수행하는 과정에서 사용함(후위 표기법)
# 사람이 사용하는 수식은 중위 표기법이다.

def Stack():
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    print(stack)

    while stack:
        print("POP Value is", stack.pop())

Stack()