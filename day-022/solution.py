from typing import List, Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def has_cycle(head: Optional[ListNode]) -> bool:
    """Return True if the linked list contains a cycle.

    Floyd's tortoise-and-hare: move one pointer one step and another two
    steps per iteration. If they ever meet, a cycle exists; if the fast
    pointer reaches the end, there is none. O(n) time, O(1) extra space.
    """
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def build(values: List[int], cycle_at: int = -1) -> Optional[ListNode]:
    """Build a linked list from a Python list (helper for tests).

    If ``cycle_at`` >= 0, the tail's next points at the node at that index.
    """
    head: Optional[ListNode] = None
    nodes: List[ListNode] = []
    for val in reversed(values):
        head = ListNode(val, head)
        nodes.append(head)
    nodes.reverse()  # nodes[i] is the i-th node
    if cycle_at >= 0 and nodes:
        nodes[-1].next = nodes[cycle_at]
    return head


if __name__ == "__main__":
    # plain acyclic lists
    assert not has_cycle(None)
    assert not has_cycle(build([1]))
    assert not has_cycle(build([1, 2, 3, 4, 5]))
    # cycles at different entry points
    assert has_cycle(build([1, 2, 3, 4], cycle_at=0))   # cycle back to head
    assert has_cycle(build([1, 2, 3, 4], cycle_at=2))   # cycle into the middle
    assert has_cycle(build([1], cycle_at=0))            # self-loop
    assert has_cycle(build([1, 2], cycle_at=1))         # tail points at itself
    # meeting-point independence: longer list, cycle in the middle
    assert has_cycle(build(list(range(100)), cycle_at=37))
    print("all cases passed")
