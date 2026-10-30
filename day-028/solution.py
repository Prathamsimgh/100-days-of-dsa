"""Reorder List.

Given the head of a singly linked list, reorder it to:

    L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

Do this in place, without changing the values of the nodes.
"""

from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return f"ListNode({self.val})"


def reorder_list(head: Optional[ListNode]) -> None:
    """Reorder the list in place: L0 -> Ln -> L1 -> Ln-1 -> ..."""
    if head is None or head.next is None:
        return

    # 1. Find the middle with slow/fast pointers. Slow ends on the last
    #    node of the first half.
    slow, fast = head, head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse the second half in place.
    second = slow.next
    slow.next = None
    prev: Optional[ListNode] = None
    while second is not None:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    second = prev

    # 3. Merge the two halves alternately.
    first = head
    while second is not None:
        first_next, second_next = first.next, second.next
        first.next = second
        second.next = first_next
        first, second = first_next, second_next


def build(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list[int]:
    out: list[int] = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([], []),
    ]
    for values, expected in cases:
        head = build(values)
        reorder_list(head)
        assert to_list(head) == expected, (values, to_list(head), expected)
    print("all self-tests passed")
