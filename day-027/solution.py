from typing import List, Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    """Add two numbers stored in reverse order in linked lists.

    Each list holds one non-negative integer with its digits in reverse
    order (the head is the least significant digit), and each node holds
    a single digit. The result is returned in the same format.

    Walk both lists together, keeping a running carry. A dummy head
    avoids special-casing the first result node, and the loop runs
    until both lists are exhausted and no carry remains, so a final
    carry naturally appends one last digit. O(max(m, n)) time, O(1)
    extra space beyond the output list.
    """
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 is not None or l2 is not None or carry:
        total = carry
        if l1 is not None:
            total += l1.val
            l1 = l1.next
        if l2 is not None:
            total += l2.val
            l2 = l2.next
        carry, digit = divmod(total, 10)
        curr.next = ListNode(digit)
        curr = curr.next
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
    # classic example: 342 + 465 = 807
    assert to_list(add_two_numbers(build([2, 4, 3]), build([5, 6, 4]))) == [
        7,
        0,
        8,
    ]

    # unequal lengths, carry ripples through the longer list
    assert to_list(add_two_numbers(build([9, 9, 9]), build([1]))) == [
        0,
        0,
        0,
        1,
    ]

    # no carry, single digits
    assert to_list(add_two_numbers(build([2]), build([3]))) == [5]

    # both lists empty: no digits, no carry, result is empty
    assert add_two_numbers(None, None) is None

    # one list empty behaves like adding zero
    assert to_list(add_two_numbers(build([4, 5]), None)) == [4, 5]

    # carry in the final position creates a new most-significant digit
    assert to_list(add_two_numbers(build([5]), build([5]))) == [0, 1]

    print("all self-tests passed")
