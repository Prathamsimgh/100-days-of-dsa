from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None,
                 right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """Check whether a binary tree is a mirror image of itself.

    Recursive mirror check: two trees are mirrors when their roots match
    and the left subtree of one mirrors the right subtree of the other.
    O(n) time, O(h) stack space.
    """
    def is_mirror(left: Optional[TreeNode],
                  right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.val == right.val
                and is_mirror(left.left, right.right)
                and is_mirror(left.right, right.left))

    if root is None:
        return True
    return is_mirror(root.left, root.right)


def from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a level-order list (None = missing child)."""
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


if __name__ == "__main__":
    assert is_symmetric(from_list([1, 2, 2, 3, 4, 4, 3])) is True
    assert is_symmetric(from_list([1, 2, 2, None, 3, None, 3])) is False
    assert is_symmetric(from_list([])) is True
    assert is_symmetric(from_list([1])) is True
    assert is_symmetric(from_list([1, 2, 2, 3, None, None, 3])) is True
    assert is_symmetric(from_list([1, 2, 3])) is False
    print("all cases passed")
