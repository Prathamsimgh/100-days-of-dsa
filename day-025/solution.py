from typing import List, Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def get_intersection_node(
    head_a: Optional[ListNode], head_b: Optional[ListNode]
) -> Optional[ListNode]:
    """Return the node at which two singly-linked lists intersect.

    Two pointers walk both lists, switching to the other list's head on
    reaching the end. After at most one switch each, both pointers have
    travelled the same total distance, so they meet at the intersection
    node — or both reach None together when there is none. The meeting
    is by node identity, not by value, so equal values before the
    intersection do not fool it. O(m + n) time, O(1) space.
    """
    p_a, p_b = head_a, head_b
    while p_a is not p_b:
        p_a = head_b if p_a is None else p_a.next
        p_b = head_a if p_b is None else p_b.next
    return p_a


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


def attach(
    head: Optional[ListNode], tail: Optional[ListNode]
) -> Optional[ListNode]:
    """Append tail to the end of head (helper for building intersections)."""
    if head is None:
        return tail
    node = head
    while node.next is not None:
        node = node.next
    node.next = tail
    return head


if __name__ == "__main__":
    # shared tail 8 -> 4 -> 5, lists intersect at 8
    shared = build([8, 4, 5])
    list_a = attach(build([4, 1]), shared)
    list_b = attach(build([5, 6, 1]), shared)
    node = get_intersection_node(list_a, list_b)
    assert node is shared and node.val == 8

    # intersection at the head itself (identical lists)
    same = build([1, 2, 3])
    assert get_intersection_node(same, same) is same

    # no intersection, same values throughout
    assert get_intersection_node(build([2, 6, 4]), build([1, 5])) is None

    # one list empty
    assert get_intersection_node(build([1, 2]), None) is None

    # both lists empty
    assert get_intersection_node(None, None) is None

    # intersection at the last node only
    last = ListNode(9)
    assert get_intersection_node(attach(build([1]), last), last) is last
    print("all self-tests passed")
