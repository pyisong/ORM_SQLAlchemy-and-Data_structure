def min_breadth(root):
    """
    层次遍历求最小值
    """
    if root is None:
        return None
    min_value = None
    queue = [root]
    while queue:
        node = queue.pop(0)
        if min_value is None or min_value > node.elem:
            min_value = node.elem
        if node.lchild is not None:
            queue.append(node.lchild)
        if node.rchild is not None:
            queue.append(node.rchild)
    return min_value


def tree_deep(root):
    """
    递归求二叉树的深度
    算法描述如下：
    如果根结点为None，那么深度=0
    如果根结点不是None，那么就看该当前结点的左孩子的深度和右孩子的深度
    如果左孩子深度>=右孩子的深度，那么当前根结点的深度就是左孩子的深度+1.
    反之则为右孩子的深度+1
    对每个左孩子右孩子也是采用同样的算法。到某一节点是None的时候，才能返回0；
    """
    if root is None:
        return 0
    left_child_deep = tree_deep(root.lchild)
    right_child_deep = tree_deep(root.rchild)
    return 1 + left_child_deep if left_child_deep >= right_child_deep else 1 + right_child_deep


def tree_level(root, dep):
    """
    算法描述：
    刚开始深度为dep，每往下递归一层，则深度减一（dep=dep-1），当dep==1的时候，
    便输出那个元素，如果先递归左子树，那么则实现从左到右打印，如果先递归右子树，
    则实现从右往左打印
    """
    if root is None or dep <= 0:
        return
    if 1 == dep:
        print(root.elem, end=" ")
    else:
        tree_level(root.lchild, dep - 1)
        tree_level(root.rchild, dep - 1)
