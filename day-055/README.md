# Day 55 — Clone Graph

**Topic:** Graphs

## Problem

Given a reference to a node in a connected undirected graph, return a
deep copy (clone) of the graph. Each node has a value and a list of its
neighbours. The graph may contain cycles, so a naive recursive copy
would loop forever.

## Approach

BFS from the start node, cloning each node on first visit. A dict maps
every original node to its clone — it serves both as the visited set
and as the lookup that lets each cloned edge point at a clone rather
than the original. When a neighbour is first seen, create its clone and
enqueue it; then append the neighbour's clone to the current clone's
neighbour list.

## Complexity

- **Time:** O(V + E) — each node and edge is visited once.
- **Space:** O(V) — the clone map plus the BFS queue.

## Edge cases

- Empty graph (`None`) returns `None`.
- A single node with no neighbours clones to a single isolated node.
- Cycles are handled by the clone map — a node already cloned is never
  enqueued again.
- The clone is a true deep copy: mutating it never affects the original.
