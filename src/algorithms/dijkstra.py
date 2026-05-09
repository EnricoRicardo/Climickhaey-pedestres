import heapq

def dijkstra(graph, start_node, end_node):
    # 1. Trava de Segurança: Verifica se os pontos existem no grafo
    if start_node not in graph.adjacency_list or end_node not in graph.adjacency_list:
        return [], float('inf')

    # 2. Inicialização
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

        # 3. Exploração de vizinhos
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
        if current in predecessors:
            current = predecessors[current]
        else:
            break
    return path[::-1] if (len(path) > 0 and path[-1] == start) else []