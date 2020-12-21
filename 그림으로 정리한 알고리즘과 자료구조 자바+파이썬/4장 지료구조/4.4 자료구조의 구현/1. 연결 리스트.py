# 연결 리스트(Linked List) : 저장하는 각 데이터(기본 데이터, 배열, 구조체, 클래스)가 데이터 외에 다음과 이전의 데이터를 가리키는 정보를 가지고 있는 구조

# 연결 리스트 : 저장된 각 데이터가 (데이터)+(다음 데이터의 포인터)로 이루어진 것, 한 방향으로만 탐색 가능
# 더블 연결 리스트(Doubly Linked List) : 저장된 각 데이터가 (이전 데이터의 포인터)+(데이터)+(다음 데이터의 포인터)로 이루어진 것, 양방향 탐색 가능
# 환형 연결 리스트(Circular Linked List) : 더블 연결 리스트의 양 끝이 연결되어 있는 구조

# 삽입과 삭제를 할 때는 전체 데이터의 변동은 X
# 앞, 뒤의 연관된 데이터만 변동하면 됨 => 지우는 과정을 빠르게 수행 가능
# 하지만, 특정 데이터를 찾는 것은 포인터를 따라 이동해야 하므로 성능이 떨어짐
# 그러므로 데이터의 변화가 많은 상황이라면 연결 리스트를 사용하는 것이 현명함

# 연결 리스트를 구성하는 단위 데이터의 모습은 데이터+다음 데이터
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 연결 리스트를 만든다. node 1 ~ node 4 그리고 연결 포인터 구성
def init() :
    global node1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

# 구성된 리스트에서 데이터를 지우고, 나머지를 연결한다.
def delete(del_data):
    global node1
    pre_node = node1
    next_node = pre_node.next

    if pre_node.data == del_data:
        node1 = next_node
        del pre_node
        return

    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next

# 연결 리스트에 데이터를 추가한다.
def insert(ins_data):
    global node1
    new_node = Node(ins_data)
    new_node.next = node1
    node1 = new_node

# 연결 리스트의 데이터를 출력한다.
def print_list():
    global node1
    node = node1
    while node:
        print(node.data)
        node = node.next
    print()

def LinkedList():
    init()
    delete(2)
    insert(9)
    print_list()

LinkedList()