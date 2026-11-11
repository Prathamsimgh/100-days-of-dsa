from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None,
                 right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Invert a binary tree in place, swapping left and right children.

    Recursive post-order swap: invert both subtrees, then swap them at
    the current node. O(n) time, O(h) stack space.
    """
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


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


def to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Serialize a tree to a level-order list, trimming trailing Nones."""
    if root is None:
        return []
    out: List[Optional[int]] = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


if __name__ == "__main__":
    assert to_list(invert_tree(from_list([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert to_list(invert_tree(from_list([2, 1, 3]))) == [2, 3, 1]
    assert to_list(invert_tree(from_list([]))) == []
    assert to_list(invert_tree(from_list([1]))) == [1]
    assert to_list(invert_tree(from_list([1, 2, None, 3]))) == [1, None, 2, None, 3]
    print("all cases passed")
