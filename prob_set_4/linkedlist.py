

class Node:
    def __init__(self, obj=None):
        self.data = obj
        self.next_node = None

    def __repr__(self):
        if self.data:
            return f'Node with data {self.data}'
        else:
            return f'Node without data'


class LinkedList:
    def __init__(self, head=None):
        self.head = Node(head)
        # instance of head Node
        self.length = 1

    def insert(self, node_data=None, index=None):
        node = Node(node_data)
        if index is None:
            self.insert_last(node_data)
            # print('not index')
        elif index == 0:
            self.change_head(node_data)
        else:
            try:
                if index > self.length:
                    raise IndexError
                else:
                    # print('index more than 0')
                    temp_node = self.head
                    for i in range(index-1):
                        temp_node = temp_node.next_node
                    node.next_node = temp_node.next_node
                    temp_node.next_node = node
                    self.length += 1
            except IndexError:
                print('No such Node!')

    def remove(self, index=None):
        if index is None:
            return None
        elif index == 0:
            self.remove_head()
        else:
            try:
                if index > self.length:
                    raise IndexError
                else:
                    # print('index more than 0')
                    temp_node = self.head
                    for i in range(index-1):
                        temp_node = temp_node.next_node
                    temp_node.next_node = temp_node.next_node.next_node
                    self.length -= 1
            except IndexError:
                print('No such Node!')

    def remove_head(self):
        self.head = self.head.next_node
        self.length -= 1

    def find(self, desired_data):
        finder = self.head
        at = 0
        for i in range(self.length):
            print(i)
            if finder.data == desired_data:
                at = i
            else:
                finder = finder.next_node
        return 'At head Node' if at == 0 else f'At {at}'

    def print_list(self):
        list_content = [self.head.data]
        for i in range(self.length):
            if i == 0:
                temp_node = self.head
            else:
                temp_node = temp_node.next_node
                list_content.append(temp_node.data)
        print(list_content)

    def insert_last(self, node_data=None):
        temp_node = self.head
        while temp_node.next_node:
            temp_node = temp_node.next_node
        temp_node.next_node = Node(node_data)
        self.length += 1

    def change_head(self, node_data=None):
        node = Node(node_data)
        node.next_node = self.head
        self.head = node
        self.length += 1
