import heapq
from typing import List, Optional


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge k sorted linked lists into one sorted list.

    Push the head of each list into a min-heap keyed by node value,
    then repeatedly pop the smallest node, append it to the result,
    and push its successor. O(N log k) time, O(k) space, where N is
    the total number of nodes and k the number of lists.
    """
    heap = []
    for i, node in enumerate(lists):
        if node is not None:
            # index breaks ties so nodes are never compared directly
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    tail = dummy
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next


def _to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def _from_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


if __name__ == "__main__":
    assert _to_list(merge_k_lists([
        _from_list([1, 4, 5]),
        _from_list([1, 3, 4]),
        _from_list([2, 6]),
    ])) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert _to_list(merge_k_lists([])) == []
    assert _to_list(merge_k_lists([None, None])) == []
    assert _to_list(merge_k_lists([_from_list([0])])) == [0]
    assert _to_list(merge_k_lists([
        _from_list([-2, -1]),
        _from_list([-3, 0, 2]),
    ])) == [-3, -2, -1, 0, 2]
    print("all cases passed")
