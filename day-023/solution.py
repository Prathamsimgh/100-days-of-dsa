from typing import List, Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def merge_two_lists(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    """Merge two sorted linked lists into one sorted list (in place).

    Walk both lists with a dummy head, always linking the smaller head node
    next. The loser list's tail is appended whole once the other list is
    exhausted — no extra nodes are allocated. O(n + m) time, O(1) space.
    """
    dummy = ListNode()
    tail = dummy
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 is not None else l2
    return dummy.next


def build(values: List[int]) -> Optional[ListNode]:
    """Build a linked list from a Python list (helper for tests)."""
    head: Optional[ListNode] = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    """Convert a linked list back to a Python list."""
    out: List[int] = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    # basic interleaving
    assert to_list(merge_two_lists(build([1, 2, 4]), build([1, 3, 4]))) == [
        1, 1, 2, 3, 4, 4,
    ]
    # one or both lists empty
    assert to_list(merge_two_lists(None, None)) == []
    assert to_list(merge_two_lists(build([1, 3]), None)) == [1, 3]
    assert to_list(merge_two_lists(None, build([2, 5]))) == [2, 5]
    # disjoint ranges: one list consumed wholesale
    assert to_list(merge_two_lists(build([1, 2]), build([3, 4]))) == [
        1, 2, 3, 4,
    ]
    assert to_list(merge_two_lists(build([5, 6]), build([1, 2]))) == [
        1, 2, 5, 6,
    ]
    # duplicate-heavy input
    assert to_list(merge_two_lists(build([1, 1, 1]), build([1, 1]))) == [
        1, 1, 1, 1, 1,
    ]
    # negative values stay ordered
    assert to_list(merge_two_lists(build([-3, -1]), build([-2, 0]))) == [
        -3, -2, -1, 0,
    ]
    # single-element lists
    assert to_list(merge_two_lists(build([0]), build([0]))) == [0, 0]
    print("all cases passed")
