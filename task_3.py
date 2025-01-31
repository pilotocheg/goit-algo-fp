import heapq


def dijkstra(graph, start_node):
    heap = []
    heapq.heappush(heap, (0, start_node))  # (відстань, вершина)
    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0

    while heap:
        # Вибираємо вершину з найменшою вагою
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        # Оновлення відстаней до сусідів
        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            # Якщо знайдено коротший шлях
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return distances


graph = {
    "A": [("B", 4), ("C", 1)],
    "B": [("A", 4), ("C", 2), ("D", 5)],
    "C": [("A", 1), ("B", 2), ("D", 8)],
    "D": [("B", 5), ("C", 8)],
}

start_node = "A"
shortest_paths = dijkstra(graph, start_node)
print("Найкоротші шляхи від", start_node, ":", shortest_paths)
