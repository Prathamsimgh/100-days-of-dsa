# Day 57 — Network Delay Time

**Topic:** Graphs

## Problem

There are `n` nodes labelled `1` to `n`, connected by directed edges.
Each entry `[u, v, w]` in `times` means a signal takes `w` time to
travel from node `u` to node `v`. Starting from node `k`, find how
long it takes for the signal to reach every node. If some node can
never be reached, return `-1`.

## Approach

This is single-source shortest path on a weighted directed graph with
non-negative weights — Dijkstra's algorithm. Build an adjacency list,
then grow the settled set from `k` outwards: a min-heap always yields
the unsettled node with the smallest known arrival time, and that
arrival time is final, because any alternative route would have to
pass through a node at least as far away. Relax each outgoing edge as
nodes are settled, pushing improved arrival times back onto the heap
(a stale heap entry is skipped when popped if its distance no longer
matches the recorded one). When the heap empties, every reachable node
has its shortest delay; the answer is the largest of them. If fewer
than `n` nodes were reached, some node is unreachable and the answer
is `-1`.

## Complexity

- **Time:** O(E log V) — each edge is relaxed once, each relaxation can push onto the heap.
- **Space:** O(V + E) — the adjacency list, the distance map, and the heap.

## Edge cases

- A single node with no edges: the signal is already there, answer `0`.
- A node with no path from `k`: return `-1`, even if all other nodes are reached.
- A direct edge that is slower than a multi-hop route — Dijkstra still finds the shorter path.
- Zero-weight edges are fine; negative weights would break the greedy settling (use Bellman-Ford instead).
