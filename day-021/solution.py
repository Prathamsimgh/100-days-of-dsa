from typing import List, Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return the head of the reversed linked list.

    Iterative three-pointer in-place reversal: walk the list keeping
    track of the previous node, and flip each node's ``next`` pointer
    to point backwards as we go. O(n) time, O(1) extra space.
    """
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def build(values: List[int]) -> Optional[ListNode]:
    """Build a linked list from a Python list (helper for tests)."""
    head: Optional[ListNode] = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    """Convert a linked list back to a Python list (helper for tests)."""
    out: List[int] = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    assert to_list(reverse_list(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse_list(build([1, 2]))) == [2, 1]
    assert to_list(reverse_list(build([1]))) == [1]
    assert reverse_list(None) is None
    # reversal is an involution: reversing twice restores the original
    original = build([7, 8, 9])
    assert to_list(reverse_list(reverse_list(original))) == [7, 8, 9]
    print("all cases passed")
