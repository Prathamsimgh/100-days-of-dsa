from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """Serialize / deserialize a binary tree with preorder traversal.

    Preorder with '#' marking null children rebuilds the tree uniquely:
    every node is followed by exactly its left and right subtrees, so a
    single pass with an index pointer reconstructs it. O(n) time, O(n)
    space for the serialized string.
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        parts: list[str] = []

        def walk(node: Optional[TreeNode]) -> None:
            if node is None:
                parts.append("#")
                return
            parts.append(str(node.val))
            walk(node.left)
            walk(node.right)

        walk(root)
        return ",".join(parts)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = deque(data.split(","))

        def build() -> Optional[TreeNode]:
            token = tokens.popleft()
            if token == "#":
                return None
            node = TreeNode(int(token))
            node.left = build()
            node.right = build()
            return node

        return build()


def _same(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None or b is None:
        return a is b
    return a.val == b.val and _same(a.left, b.left) and _same(a.right, b.right)


if __name__ == "__main__":
    codec = Codec()

    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    assert codec.deserialize(codec.serialize(tree)) is not None
    assert _same(codec.deserialize(codec.serialize(tree)), tree)

    single = TreeNode(7)
    assert codec.serialize(single) == "7,#,#"
    assert _same(codec.deserialize(codec.serialize(single)), single)

    assert codec.serialize(None) == "#"
    assert codec.deserialize("#") is None

    left_only = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert _same(codec.deserialize(codec.serialize(left_only)), left_only)

    print("all cases passed")
