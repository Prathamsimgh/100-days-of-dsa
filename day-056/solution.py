from collections import deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Return True if all courses can be finished, False if a cycle blocks it.

    Each prerequisite [a, b] means course b must be taken before course a,
    i.e. a directed edge b -> a. Kahn's algorithm: repeatedly take a course
    with no remaining prerequisites (in-degree 0) and drop its outgoing
    edges. If every course is taken, the graph is acyclic; if some courses
    remain, they sit in a cycle and can never be scheduled.
    """
    graph: List[List[int]] = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque(i for i in range(num_courses) if in_degree[i] == 0)
    taken = 0

    while queue:
        course = queue.popleft()
        taken += 1
        for nxt in graph[course]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    return taken == num_courses


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """Return one valid course order, or [] if no such order exists.

    Same Kahn's pass as can_finish, recording the order courses are taken
    in. An empty result is ambiguous on its own (it also means zero
    courses), so pair it with can_finish when that matters.
    """
    graph: List[List[int]] = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque(i for i in range(num_courses) if in_degree[i] == 0)
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)
        for nxt in graph[course]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    return order if len(order) == num_courses else []


if __name__ == "__main__":
    # Two courses, one prerequisite — finishable
    assert can_finish(2, [[1, 0]]) is True
    assert find_order(2, [[1, 0]]) == [0, 1]
    # Two courses depending on each other — a cycle
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert find_order(2, [[1, 0], [0, 1]]) == []
    # Diamond: 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3
    assert can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True
    order = find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert order[0] == 0 and order[-1] == 3
    assert order.index(1) < order.index(3) and order.index(2) < order.index(3)
    # No prerequisites at all
    assert can_finish(3, []) is True
    assert sorted(find_order(3, [])) == [0, 1, 2]
    # Self-loop: a course depending on itself
    assert can_finish(1, [[0, 0]]) is False
    # Larger cycle hidden among finishable courses
    assert can_finish(4, [[1, 0], [2, 1], [0, 2], [3, 1]]) is False
    print("all cases passed")
