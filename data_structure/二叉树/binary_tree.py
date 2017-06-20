class Node(object):
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left_child = left
        self.right_child = right


class BinaryTree(object):
    """binary tree"""
    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            queue = [self.root]
            while len(queue) > 0:
                node = queue.pop(0)
                if not node.left_child:
                    node.left_child = Node(item)
                    return
                else:
                    queue.append(node.left_child)
                if not node.right_child:
                    node.right_child = Node(item)
                    return
                else:
                    queue.append(node.right_child)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return None
        else:
            queue = [self.root]
            while len(queue) > 0:
                node = queue.pop(0)
                print(node.item, end=',')
                if node.left_child:
                    queue.append(node.left_child)
                if node.right_child:
                    queue.append(node.right_child)

    def preorder_travel(self, node):
        """先序遍历， 根、左、右"""
        if node:
            print(node.item, end=",")
            self.preorder_travel(node.left_child)
            self.preorder_travel(node.right_child)
        else:
            return

    def inorder_travel(self, node):
        """中序遍历， 左、根、右"""
        if node:
            self.inorder_travel(node.left_child)
            print(node.item, end=',')
            self.inorder_travel(node.right_child)
        else:
            return

    def postorder_travel(self, node):
        """后序遍历， 左、右、根"""
        if node:
            self.postorder_travel(node.left_child)
            self.postorder_travel(node.right_child)
            print(node.item, end=',')
        else:
            return

if __name__ == '__main__':
    t = BinaryTree()
    t.add(0)
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    t.breadth_travel()
    print("")
    t.preorder_travel(t.root)
    print("")
    t.inorder_travel(t.root)
    print("")
    t.postorder_travel(t.root)
    print("")
