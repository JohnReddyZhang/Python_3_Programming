class TreeNode(object):
    """ built strictly according to the requirement, so all comparisons happen based on keys. Thus all
    keys in one tree must be comparable to each other"""
    def __init__(self, key, left_child=None, right_child=None, parent=None):
        self.key = key
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    # def constructor(self, key):
    #     self.key = key

    def __repr__(self):
        return f'Node Data {self.key}'

    def has_left(self):
        return self.left_child

    def has_right(self):
        return self.right_child

    def has_child(self):
        return self.right_child or self.left_child

    def has_two_child(self):
        return self.right_child and self.left_child

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    # def find_succ(self):
    #     successor = None
    #     if self.has_right():
    #         successor = self.right_child.find_min()
    #     else:
    #         if self.parent:
    #             if self.parent.left_child == self:
    #                 successor = self.parent
    #             else:
    #                 self.parent.right_child = None
    #                 successor = self.parent.find_succ()
    def find_min(self):
        mini = self
        while mini.has_left():
            mini = mini.left_child
        return mini


class BinarySearchTree:
    def __init__(self, set_root_node=None):
        self.root_node = set_root_node
        self.__size = 0

    def is_empty(self):
        if not self.root_node:
            print('Empty Tree!')
            return True

    def insert(self, insert_node):
        # inserting root?
        if not self.root_node:
            self.root_node = insert_node
            self.__size += 1
        else:
            temp_node = self.root_node
            while True:
                if temp_node.key > insert_node.key:
                    if temp_node.has_left():
                        # print('Assigning temp node')
                        temp_node = temp_node.left_child
                    else:
                        # print('end, should break')
                        insert_node.parent = temp_node
                        temp_node.left_child = insert_node
                        self.__size += 1
                        break
                else:
                    if temp_node.has_right():
                        print('Assigning temp node right')
                        temp_node = temp_node.right_child
                    else:
                        # print('should break right')
                        insert_node.parent = temp_node
                        temp_node.right_child = insert_node
                        self.__size += 1
                        break

    def remove(self, value):
        if self.is_empty():
            return None
        if self.__size > 1:
            target_node = self.__search_recursive(value, self.root_node)
            if target_node:
                self._delete(target_node)
                self.__size -= 1
            else:
                print('No such node in tree!')
        elif self.__size == 1 and self.root_node.key == value:
            self.root_node = None
            self.__size -= 1
        else:
            print('Key not found')

    def _delete(self, target_node):
        if target_node.is_leaf():
            if target_node.parent.left_child == target_node:
                target_node.parent.left_child = None
            else:
                target_node.parent.right_child = None
            return target_node

        elif target_node.has_child() and not target_node.has_two_child():
            if target_node.left_child:
                temp_node = target_node.left_child
            else:
                temp_node = target_node.right_child
            if target_node.parent:
                if target_node.parent.left_child is target_node:
                    target_node.parent.left_child = temp_node
                else:
                    target_node.parent.right_child = temp_node
                return target_node
            else:
                # target is root
                self.root_node = temp_node
                return target_node

        elif target_node.has_two_child():
            successor = target_node.right_child.find_min()
            pop_node = target_node
            target_node.key = successor.key
            self._delete(successor)
            return pop_node

    def search(self, search_value, from_node=None):
        # True if found
        # Recursive
        if self.is_empty():
            return None
        if not from_node:
            from_node = self.root_node
        else:
            from_node = self.__search_recursive(from_node.key, self.root_node)
        result_node = self.__search_recursive(search_value, from_node)
        if not result_node:
            return False
        else:
            return True

    def __search_recursive(self, target_value, current_node):
        if not current_node:
            return None
        elif current_node.key == target_value:
            return current_node
        elif target_value < current_node.key:
            return self.__search_recursive(target_value, current_node.left_child)
        else:
            return self.__search_recursive(target_value, current_node.right_child)

    def min(self):
        # min in the tree
        min_node = self.root_node
        if not min_node:
            return None
        while min_node.left_child:
            min_node = min_node.left_child
        return min_node.key

    def max(self):
        # max in tree
        def findmax(node):
            if node is None:
                return None
            while node.right_child:
                node = node.right_child
            return node.key
        return findmax(self.root_node)

