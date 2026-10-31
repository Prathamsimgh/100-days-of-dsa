"""Rotate List.

Given the head of a linked list, rotate the list to the right by k places.
"""

from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Rotate the list right by k places in O(n) time and O(1) space.

    Close the list into a ring, then break it at the new tail: the new
    head is (length - k % length) steps from the old head. When k is a
    multiple of the length the list is unchanged.
    """
    if head is None or head.next is None or k == 0:
        return head

    # Find the length and the current tail.
    length = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        length += 1

    k %= length
    if k == 0:
        return head

    # Close the ring, then walk to the new tail.
    tail.next = head
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head


def build(values: list[int]) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_list(head: Optional[ListNode]) -> list[int]:
    values: list[int] = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    assert to_list(rotate_right(build([1, 2, 3, 4, 5]), 2)) == [4, 5, 1, 2, 3]
    assert to_list(rotate_right(build([0, 1, 2]), 4)) == [2, 0, 1]
    assert to_list(rotate_right(build([1, 2]), 0)) == [1, 2]
    assert to_list(rotate_right(build([1]), 99)) == [1]
    assert rotate_right(None, 3) is None
    print("all tests passed")
