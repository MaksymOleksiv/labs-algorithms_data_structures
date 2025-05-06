import sys


def prim_mst(graph) -> int:
    """
    Prim's algorithm for finding the minimum spanning tree (MST) of a graph.
    :param graph: list[list[int]]: Adjacency matrix representation of the graph.
    :return: int: Total weight of the minimum spanning tree.
    """
    N = len(graph)
    selected = [False] * N
    min_edge = [sys.maxsize] * N
    min_edge[0] = 0
    total_weight = 0

    for _ in range(N):
        u = -1
        for v in range(N):
            if not selected[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v

        selected[u] = True
        total_weight += min_edge[u]

        for v in range(N):
            if graph[u][v] != 0 and not selected[v] and graph[u][v] < min_edge[v]:
                min_edge[v] = graph[u][v]

    return total_weight
