from typing import List, Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def remove_nth_from_end(
    head: Optional[ListNode], n: int
) -> Optional[ListNode]:
    """Remove the nth node from the end of a singly-linked list.

    Two pointers, one gap of n nodes ahead: when the fast pointer reaches
    the end, the slow pointer sits on the node just before the one to
    remove. A dummy head covers removing the first node with no special
    case. O(n) time, O(1) space.
    """
    dummy = ListNode(0, head)
    fast: Optional[ListNode] = dummy
    slow: Optional[ListNode] = dummy
    for _ in range(n + 1):
        # n is guaranteed valid, so fast never runs out early.
        assert fast is not None
        fast = fast.next
    while fast is not None:
        fast = fast.next
        assert slow is not None
        slow = slow.next
    assert slow is not None and slow.next is not None
    slow.next = slow.next.next
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
    # middle removal
    assert to_list(remove_nth_from_end(build([1, 2, 3, 4, 5]), 2)) == [
        1, 2, 3, 5,
    ]
    # remove the head (n == length)
    assert to_list(remove_nth_from_end(build([1, 2, 3, 4, 5]), 5)) == [
        2, 3, 4, 5,
    ]
    # remove the tail (n == 1)
    assert to_list(remove_nth_from_end(build([1, 2, 3]), 1)) == [1, 2]
    # single-node list becomes empty
    assert to_list(remove_nth_from_end(build([1]), 1)) == []
    # two nodes, remove the first
    assert to_list(remove_nth_from_end(build([1, 2]), 2)) == [2]
    print("all self-tests passed")
