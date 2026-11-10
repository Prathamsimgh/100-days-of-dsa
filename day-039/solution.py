from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Return node values level by level, left to right.

    Breadth-first traversal with a queue: process one full level at a
    time, snapshotting the queue size so values never leak into the
    next level. O(n) time, O(w) space where w is the max tree width.
    """
    if root is None:
        return []
    result: List[List[int]] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        level: List[int] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def _build(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a level-order list (None = missing child)."""
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
    assert level_order(_build([3, 9, 20, None, None, 15, 7])) == [
        [3], [9, 20], [15, 7]
    ]
    assert level_order(_build([1])) == [[1]]
    assert level_order(_build([])) == []
    assert level_order(_build([1, 2, 3, 4, 5, 6, 7])) == [
        [1], [2, 3], [4, 5, 6, 7]
    ]
    assert level_order(_build([1, None, 2, None, 3])) == [[1], [2], [3]]
    print("all cases passed")
