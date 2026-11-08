"""Diameter of Binary Tree.

The diameter of a binary tree is the length (in edges) of the longest
path between any two nodes. The path may or may not pass through the
root, and it may or may not use every level of the tree.
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


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """One post-order pass: at each node, the diameter passing through it
    is left height + right height (in edges). Track the max across all
    nodes and return the height of each subtree to its parent. Each node
    is visited once; the recursion stack is as deep as the tree is tall."""
    best = 0

    def height(node: Optional[TreeNode]) -> int:
        nonlocal best
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        best = max(best, left + right)
        return 1 + max(left, right)

    height(root)
    return best


def diameter_of_binary_tree_iterative(root: Optional[TreeNode]) -> int:
    """Same idea without recursion: process nodes in post-order with an
    explicit stack, recording each node's height in a dict as its
    children are finished. A skewed tree can never blow the recursion
    limit this way, at the cost of O(n) extra memory for the map."""
    if root is None:
        return 0
    heights: dict[TreeNode, int] = {}
    best = 0
    stack = [(root, False)]
    while stack:
        node, done = stack.pop()
        if done:
            left = heights.get(node.left, 0)
            right = heights.get(node.right, 0)
            best = max(best, left + right)
            heights[node] = 1 + max(left, right)
        else:
            stack.append((node, True))
            if node.left is not None:
                stack.append((node.left, False))
            if node.right is not None:
                stack.append((node.right, False))
    return best


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
    # classic example: longest path 4 -> 2 -> 1 -> 3 -> 5, length 3
    tree = build([1, 2, 3, 4, 5])
    assert diameter_of_binary_tree(tree) == 3
    assert diameter_of_binary_tree_iterative(tree) == 3

    # diameter passes through the root: 3 edges either way
    balanced = build([1, 2, 3, 4, 5, 6, 7])
    assert diameter_of_binary_tree(balanced) == 4

    # diameter passes through the root only at the top: longest path is
    # 4 -> 3 -> 2 -> 1, length 3 (the 4 -> 3 -> 5 branch is only 2)
    lopsided = build([1, 2, None, 3, None, 4, 5])
    assert diameter_of_binary_tree(lopsided) == 3

    # single node: no edges, diameter 0
    assert diameter_of_binary_tree(build([1])) == 0
    assert diameter_of_binary_tree_iterative(build([1])) == 0

    # empty tree: diameter 0
    assert diameter_of_binary_tree(None) == 0
    assert diameter_of_binary_tree_iterative(None) == 0

    # straight chain: diameter is the number of edges, n - 1
    chain = build([1, 2, None, 3, None, 4, None, 5])
    assert diameter_of_binary_tree(chain) == 4

    print("all self-tests passed")
