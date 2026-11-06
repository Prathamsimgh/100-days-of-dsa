"""Maximum Depth of Binary Tree.

Given the root of a binary tree, return its maximum depth — the number
of nodes along the longest path from the root down to the farthest leaf.
"""

from collections import deque
from typing import Optional


class TreeNode:
    """Binary tree node."""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


def max_depth(root: Optional[TreeNode]) -> int:
    """Recursively: an empty tree has depth 0, otherwise 1 plus the
    deeper of the two subtrees. Each node is visited once, and the
    recursion stack is as deep as the tree is tall."""
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_iterative(root: Optional[TreeNode]) -> int:
    """Breadth-first version: count levels. Same result, and the queue
    keeps memory proportional to the widest level instead of the height.
    Useful when a degenerate (linked-list-shaped) tree would blow the
    recursion limit."""
    if root is None:
        return 0
    depth = 0
    queue: deque[TreeNode] = deque([root])
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return depth


def build(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list (None = missing
    child). Helper for tests."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue: deque[TreeNode] = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    # classic example: depth 3
    assert max_depth(build([3, 9, 20, None, None, 15, 7])) == 3
    assert max_depth_iterative(build([3, 9, 20, None, None, 15, 7])) == 3

    # single node: depth 1
    assert max_depth(build([1])) == 1

    # empty tree: depth 0
    assert max_depth(None) == 0
    assert max_depth_iterative(None) == 0

    # skewed tree: depth equals the node count
    assert max_depth(build([1, 2, None, 3, None, 4])) == 4

    # balanced tree: depth grows logarithmically
    assert max_depth(build([1, 2, 3, 4, 5, 6, 7])) == 3

    # left-heavy vs right-heavy: the longer side wins
    assert max_depth(build([1, 2, None, 3])) == 3
    assert max_depth(build([1, None, 2, None, 3])) == 3

    print("all self-tests passed")
