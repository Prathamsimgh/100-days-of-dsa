from typing import List, Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly-linked list in place, returning the new head."""
    prev: Optional[ListNode] = None
    curr = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def is_palindrome(head: Optional[ListNode]) -> bool:
    """Return True if the linked list reads the same forwards and back.

    Fast and slow pointers find the middle; the second half is reversed
    in place, then the two halves are compared node by node. The second
    half is reversed back afterwards so the caller's list is left
    unchanged. O(n) time, O(1) space.
    """
    if head is None or head.next is None:
        return True

    # find the middle: slow lands on the middle node (odd length) or
    # the first node of the second half (even length)
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # odd length: skip the middle node, it never needs comparing
    second_half = slow.next if fast is not None else slow
    reversed_half = reverse(second_half)

    first, second = head, reversed_half
    result = True
    while second is not None:
        if first.val != second.val:
            result = False
            break
        first = first.next
        second = second.next

    reverse(reversed_half)  # restore the original list
    return result


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
    # even-length palindrome, list left intact afterwards
    even = build([1, 2, 2, 1])
    assert is_palindrome(even) is True
    assert to_list(even) == [1, 2, 2, 1]

    # odd-length palindrome
    odd = build([1, 2, 3, 2, 1])
    assert is_palindrome(odd) is True
    assert to_list(odd) == [1, 2, 3, 2, 1]

    # not a palindrome
    not_pal = build([1, 2, 3, 4])
    assert is_palindrome(not_pal) is False
    assert to_list(not_pal) == [1, 2, 3, 4]

    # single node and empty list are palindromes
    assert is_palindrome(build([7])) is True
    assert is_palindrome(None) is True

    # equal values that are not symmetric
    assert is_palindrome(build([1, 2, 1, 2])) is False

    # two nodes, same value
    assert is_palindrome(build([5, 5])) is True
    print("all self-tests passed")
