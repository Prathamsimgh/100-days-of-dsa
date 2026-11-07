"""Lowest Common Ancestor of a Binary Tree.

Given a binary tree, find the lowest common ancestor (LCA) of two given
nodes. The LCA is the deepest node that has both p and q as descendants
(a node counts as a descendant of itself).
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


def lowest_common_ancestor(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    """Recursively: the LCA is the first node where p and q split into
    different subtrees, or p or q itself when one is an ancestor of the
    other. Each node is visited once; the recursion stack is as deep as
    the tree is tall."""
    if root is None or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left is not None and right is not None:
        return root
    return left if left is not None else right


def lowest_common_ancestor_parent_map(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    """Iterative version: record each node's parent with a stack walk,
    then climb from p collecting its ancestors and walk up from q until
    the paths meet. Uses O(n) extra memory but never recurses, so a
    degenerate tree cannot blow the recursion limit."""
    if root is None:
        return None
    parent: dict[TreeNode, Optional[TreeNode]] = {root: None}
    stack = [root]
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left is not None:
            parent[node.left] = node
            stack.append(node.left)
        if node.right is not None:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    node: Optional[TreeNode] = p
    while node is not None:
        ancestors.add(node)
        node = parent[node]
    node = q
    while node not in ancestors:
        node = parent[node]
    return node


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


def find(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Find the first node with the given value. Helper for tests."""
    if root is None:
        return None
    if root.val == val:
        return root
    return find(root.left, val) or find(root.right, val)


if __name__ == "__main__":
    # classic example: LCA of 5 and 1 is 3
    tree = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert lowest_common_ancestor(tree, find(tree, 5), find(tree, 1)).val == 3
    assert lowest_common_ancestor_parent_map(tree, find(tree, 5), find(tree, 1)).val == 3

    # LCA of 5 and 4 is 5: p is an ancestor of q
    assert lowest_common_ancestor(tree, find(tree, 5), find(tree, 4)).val == 5
    assert lowest_common_ancestor_parent_map(tree, find(tree, 5), find(tree, 4)).val == 5

    # LCA of 6 and 4 is 5: both in the left subtree
    assert lowest_common_ancestor(tree, find(tree, 6), find(tree, 4)).val == 5

    # LCA of 0 and 8 is 1: both in the right subtree
    assert lowest_common_ancestor(tree, find(tree, 0), find(tree, 8)).val == 1

    # same node twice: LCA is the node itself
    assert lowest_common_ancestor(tree, find(tree, 7), find(tree, 7)).val == 7

    # two-node tree: LCA of root and its child is the root
    small = build([1, 2])
    assert lowest_common_ancestor(small, small, find(small, 2)).val == 1

    print("all self-tests passed")
