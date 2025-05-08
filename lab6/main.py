from priority_queue import PriorityQueue
def client_server_latency(
        NM: tuple[int, int],
        clients: tuple[int, ...],
        *links: tuple[int, int, int], ) -> int:
    """
    Calculate the latency between clients and servers.
    :param NM: a tuple of:
     N - the number of nodes in the graph
     M - the number of connections between nodes
    :param clients: a tuple of clients
    :param links: a tuple of links: startnode, endnode, latency
    :return: the shortest latency between clients and servers
    """
    N, M = NM

    graph = {i: [] for i in range(1, N + 1)}

    for start, end, latency in links:
        graph[start].append((end, latency))
        graph[end].append((start, latency))

    def dijkstra(start_node):
        distances = {node: float('inf') for node in range(1, N + 1)}
        distances[start_node] = 0
        queue = PriorityQueue()
        queue.enqueue((0, start_node))

        while not queue.is_empty():
            current_distance, current_node = queue.dequeue()

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    queue.enqueue((distance, neighbor))

        return distances

    latencies = [dijkstra(router) for router in graph if router not in clients]
    routers = [i for i in graph if i not in clients]
    for i in latencies:
        for j in routers:
            i.pop(j)

    res = {i+1: max(d.values()) for i, d in enumerate(latencies) }



    return min(res.values()) if res else 0
