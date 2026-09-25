import heapq

CAMPUS_GRAPH = {
    'L1': [('L2', 1), ('L6', 3)],
    'L2': [('L1', 1), ('L3', 2), ('L4', 2)],
    'L3': [('L2', 2)],
    'L4': [('L2', 2), ('L5', 2)],
    'L5': [('L4', 2), ('L6', 2)],
    'L6': [('L1', 3), ('L5', 2)]
}

LOCATION_NAMES = {
    'L1': 'Main Gate',
    'L2': 'Admin Block',
    'L3': 'Library',
    'L4': 'Science Lab',
    'L5': 'Student Affairs',
    'L6': 'Cafeteria'
}

# Pre-computed minimum hop count heuristic relative to L4 (Science Lab)
HEURISTIC_TO_L4 = {
    'L1': 2,
    'L2': 1,
    'L3': 2,
    'L4': 0,
    'L5': 1,
    'L6': 2
}

def astar(graph, start, goal, heuristic):
    """
    A* Search using a Priority Queue (Min-Heap).
    Evaluates nodes using f(n) = g(n) + h(n).
    """
    # Priority Queue stores tuples of (f_score, g_score, current_node, path)
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))
    
    visited = {}

    nodes_expanded = 0

    while pq:
        f_score, g_score, current_node, path = heapq.heappop(pq)
        nodes_expanded += 1

        if current_node == goal:
            return path, g_score, nodes_expanded

        if current_node in visited and visited[current_node] <= g_score:
            continue
        visited[current_node] = g_score

        for neighbor, weight in graph[current_node]:
            tentative_g = g_score + weight
            
            if neighbor not in visited or tentative_g < visited.get(neighbor, float('inf')):
                f_neighbor = tentative_g + heuristic[neighbor]
                heapq.heappush(pq, (f_neighbor, tentative_g, neighbor, path + [neighbor]))

    return None, float('inf'), nodes_expanded

if __name__ == "__main__":
    start_node = 'L1'  # Main Gate
    goal_node = 'L4'   # Science Lab

    path, cost, expanded = astar(CAMPUS_GRAPH, start_node, goal_node, HEURISTIC_TO_L4)
    
    path_named = " -> ".join([f"{node} ({LOCATION_NAMES[node]})" for node in path])
    print("=== A* Search Algorithm ===")
    print(f"Path Found:     {path_named}")
    print(f"Total Distance: {cost} km")
    print(f"Nodes Expanded: {expanded}")
