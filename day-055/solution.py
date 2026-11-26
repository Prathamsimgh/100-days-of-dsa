from collections import deque
from typing import Dict, List, Optional


class Node:
    """Graph node: a value and a list of neighbours."""

    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """Return a deep copy of an undirected connected graph.

    BFS from the start node, cloning each node on first visit and
    wiring the cloned neighbours as they are discovered. A dict
    from original node to its clone is the whole trick: it both
    prevents revisiting nodes (cycles) and lets every edge point
    at the clone instead of the original.
    """
    if node is None:
        return None

    clones: Dict[Node, Node] = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        current = queue.popleft()
        for neighbour in current.neighbors:
            if neighbour not in clones:
                clones[neighbour] = Node(neighbour.val)
                queue.append(neighbour)
            clones[current].neighbors.append(clones[neighbour])

    return clones[node]


def build_graph(adj: List[List[int]]) -> Optional[Node]:
    """Build a graph from an adjacency list (1-indexed values)."""
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, neighbours in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbours]
    return nodes[0]


def to_adj(node: Optional[Node]) -> List[List[int]]:
    """Serialise a graph back to an adjacency list for comparison."""
    if node is None:
        return []
    seen = {node}
    queue = deque([node])
    adj: Dict[int, List[int]] = {}
    while queue:
        current = queue.popleft()
        adj[current.val] = sorted(n.val for n in current.neighbors)
        for neighbour in current.neighbors:
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)
    return [adj[i] for i in sorted(adj)]


if __name__ == "__main__":
    # Square: 1-2, 1-4, 2-3, 3-4
    original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    clone = clone_graph(original)
    assert to_adj(clone) == [[2, 4], [1, 3], [2, 4], [1, 3]]
    # Clone is a deep copy: mutating it leaves the original intact
    assert clone is not original
    assert all(c is not o for c, o in zip(clone.neighbors, original.neighbors))
    clone.neighbors[0].val = 99
    assert original.neighbors[0].val == 2
    # Single node, no edges
    assert to_adj(clone_graph(build_graph([[]]))) == [[]]
    # Two nodes, one edge
    assert to_adj(clone_graph(build_graph([[2], [1]]))) == [[2], [1]]
    # Empty graph
    assert clone_graph(None) is None
    print("all cases passed")
