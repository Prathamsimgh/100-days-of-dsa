import heapq
from typing import Dict, List, Tuple


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """Return the time for a signal from node k to reach every node, or -1.

    Each entry [u, v, w] means a signal takes w time to travel from u to v.
    Dijkstra's algorithm: repeatedly settle the unvisited node with the
    smallest known arrival time (a min-heap gives it in O(log n)). The
    first time a node is popped its distance is final, because any other
    route to it would go through a node at least as far away. Once every
    node is settled, the answer is the largest arrival time; if a node is
    never reached, the signal can't cover the network.
    """
    graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {k: 0}
    heap = [(0, k)]

    while heap:
        d, node = heapq.heappop(heap)
        if d != dist[node]:
            continue
        for nxt, w in graph[node]:
            nd = d + w
            if nxt not in dist or nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))

    if len(dist) < n:
        return -1
    return max(dist.values())


if __name__ == "__main__":
    # Classic example: 2 -> 1 in 1, 2 -> 3 in 1, 3 -> 4 in 1
    assert network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    # Single node, no edges — the signal is already there
    assert network_delay_time([], 1, 1) == 0
    # Node 3 is unreachable from 1
    assert network_delay_time([[1, 2, 1]], 3, 1) == -1
    # Longer direct edge loses to a two-hop route (1 -> 2 -> 3 is 2, not 5)
    assert network_delay_time([[1, 2, 1], [2, 3, 1], [1, 3, 5]], 3, 1) == 2
    # Equal-cost alternate paths still settle every node
    assert network_delay_time([[1, 2, 3], [1, 3, 3], [2, 4, 1], [3, 4, 1]], 4, 1) == 4
    print("all cases passed")
