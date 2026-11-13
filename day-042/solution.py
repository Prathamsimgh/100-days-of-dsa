from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list (None = missing node)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """Return the kth smallest value in a BST.

    Iterative inorder traversal: a BST's inorder sequence is sorted,
    so the kth node visited is the answer. The walk stops as soon as
    it is found — no need to traverse the whole tree. O(h) space for
    the explicit stack, where h is the tree height.
    """
    stack: List[TreeNode] = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
    raise ValueError("k is larger than the number of nodes")


if __name__ == "__main__":
    assert kth_smallest(build_tree([3, 1, 4, None, 2]), 1) == 1
    assert kth_smallest(build_tree([3, 1, 4, None, 2]), 2) == 2
    assert kth_smallest(build_tree([3, 1, 4, None, 2]), 3) == 3
    assert kth_smallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
    assert kth_smallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 1) == 1
    assert kth_smallest(build_tree([1]), 1) == 1
    print("all cases passed")
