from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    """Return the values visible when looking at the tree from the right.

    Level-order traversal, keeping the last node of each level. O(n) time,
    O(w) space for the widest level.
    """
    if root is None:
        return []
    view = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                view.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return view


def _build(values):
    """Build a tree from a level-order list, None for missing nodes."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
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
    assert right_side_view(_build([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert right_side_view(_build([1, None, 3])) == [1, 3]
    assert right_side_view(_build([])) == []
    assert right_side_view(_build([1, 2, 3, 4])) == [1, 3, 4]
    print("all cases passed")
