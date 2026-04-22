import heapq

def dijkstra(graph, start_node, end_node):
    distances = {node: float('inf') for node in graph.adjacency_list}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    predecessors = {node: None for node in graph.adjacency_list}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end_node:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.adjacency_list[current_node]:
            weight = neighbor['weight']
            distance = current_distance + weight

            if distance < distances[neighbor['target']]:
                distances[neighbor['target']] = distance
                predecessors[neighbor['target']] = current_node
                heapq.heappush(priority_queue, (distance, neighbor['target']))

    return reconstruct_path(predecessors, start_node, end_node), distances[end_node]

def reconstruct_path(predecessors, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    return path[::-1] if (len(path) > 0 and path[-1] == start) else []