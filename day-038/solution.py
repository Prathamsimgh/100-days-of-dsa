"""Validate Binary Search Tree.

Given the root of a binary tree, determine whether it is a valid binary
search tree: for every node, all values in its left subtree are smaller
than the node's value and all values in its right subtree are larger.
Each node's value must be strictly inside the range its ancestors
impose on it, not just different from its immediate neighbours.
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


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Walk the tree carrying the allowed (low, high) range for each
    node, inherited from its ancestors. The root may hold any value;
    a left child must be below its parent, a right child above it, and
    those bounds only tighten further down. A node that falls outside
    its range fails immediately. Each node is visited once; the
    recursion stack is as deep as the tree is tall."""
    def check(node: Optional[TreeNode], low: float, high: float) -> bool:
        if node is None:
            return True
        if not low < node.val < high:
            return False
        return check(node.left, low, node.val) and check(
            node.right, node.val, high
        )

    return check(root, float("-inf"), float("inf"))


def is_valid_bst_iterative(root: Optional[TreeNode]) -> bool:
    """Same property, read off an inorder walk instead: an inorder
    traversal of a valid BST visits values in strictly increasing
    order, so the check is just "each value larger than the previous
    one". An explicit stack keeps the traversal off the call stack,
    and only the previous value needs remembering."""
    stack: list[TreeNode] = []
    node = root
    prev: Optional[int] = None
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if prev is not None and node.val <= prev:
            return False
        prev = node.val
        node = node.right
    return True


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
    # textbook valid BST
    valid = build([2, 1, 3])
    assert is_valid_bst(valid) is True
    assert is_valid_bst_iterative(valid) is True

    # right child smaller than the root: not a BST
    broken = build([5, 1, 4, None, None, 3, 6])
    assert is_valid_bst(broken) is False
    assert is_valid_bst_iterative(broken) is False

    # looks fine locally (3 < 5, 6 > 5) but 6 sits in the left subtree
    # of 5, so the ancestor bound catches it
    deep = build([5, 4, 6, None, None, 3, 7])
    assert is_valid_bst(deep) is False
    assert is_valid_bst_iterative(deep) is False

    # duplicate values: BST ordering is strict, so [2, 2, 2] fails
    dupes = build([2, 2, 2])
    assert is_valid_bst(dupes) is False
    assert is_valid_bst_iterative(dupes) is False

    # single node and empty tree are trivially valid
    assert is_valid_bst(build([1])) is True
    assert is_valid_bst_iterative(build([1])) is True
    assert is_valid_bst(None) is True
    assert is_valid_bst_iterative(None) is True

    # left-skewed chain, decreasing values: valid
    chain = build([5, 4, None, 3, None, 2, None, 1])
    assert is_valid_bst(chain) is True
    assert is_valid_bst_iterative(chain) is True

    print("all self-tests passed")
