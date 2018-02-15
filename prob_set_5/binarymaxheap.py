class Node(object):
    def __init__(self, key, left_child=None, right_child=None):
        self.key = key
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return f'Node with value {self.key}'

    def __lt__(self, other):
        # print('strangely in here')
        return self.key < other.key
    # in heapify this __lt__ was called several times before loop. Why?
    # Although it works

    def __eq__(self, other):
        return self.key == other.key

    def __le__(self, other):
        return self.key <= other.key


class BinaryMaxHeap(object):
    def __init__(self, root_node=None):
        self.root_node = root_node
        self.heap = []

    def heapify(self, *arg_nodes):
        self.heap =[]
        for i in arg_nodes:
            self.heap.append(i)
        self.heap = sorted(self.heap, reverse=True)
        length = len(self.heap)
        i = 0
        while i < length:
            # print('in while')
            try:
                # print('in try')
                self.heap[i].left_child = self.heap[2*(i+1)-1]
                self.heap[i].right_child = self.heap[2*(i+1)]
                i += 1
            except IndexError:
                break
        self.root_node = self.heap[0]

    def push(self, node):
        try:
            if not isinstance(node, Node):
                raise TypeError
            self.heap.append(node)
            self.heapify(*self.heap)
        except TypeError:
            print('Please insert a Node(val)!')

    def delete(self, key):
        if key not in [item.key for item in self.heap]:
            return None
        for item in self.heap:
            if item.key == key:
                self.heap.remove(item)
                self.heapify(*self.heap)
                return item

    def pop(self):
        pop_node = Node(self.root_node.key)
        self.heap.remove(self.root_node)
        self.heapify(*self.heap)
        return pop_node
