# 큐(Queue) : 데이터가 입력되면 입력되는 순서대로 쌓고, 먼저 들어온 것부터 먼저 사용하는 자료구조
# 큐 형태의 데이터 구조 : FIFO(First In First Out(
# 순환 큐 : 배열 이용
# 링크드 큐 : 연결 리스트 이용

# 컴퓨터 안에 여러 개의 프로세스가 수행 중인데, 새로운 프로세스가 수행되어야 하는 경우 기존에 수행되던 프로세스 중에서 가장 먼저 메모리에 올라온 프로세스가 아웃되고,
# 새로운 프로세스를 메모리에 올리게 된다. 이 경우 운영체제는 현재 수행 중인 프로세스를 큐의 형태로 관리한다.

# 윈도우 운영체제를 사용하는 컴퓨터에서 수행 중인 프로그램에 이벤트(버튼 누르기, 윈도우 크기 조정, 메뉴 선택하기 등)가 발생하면,
# 발생한 이벤트가 큐에 저장되고, 수행 중인 프로그램이 큐에 저장된 것을 앞에서부터 읽어 와서 처리한다.(선입선출) 이 때도 큐가 사용된다.

def Queue():
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    print(queue)

    while queue:
        print("Get Value :", queue.pop(0))

Queue()

