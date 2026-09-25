from collections import deque

# Campus Graph Representation
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

def bfs(graph, start, goal):
    """
    Breadth-First Search using a Queue (FIFO).
    Guarantees finding the path with the fewest edges (hops).
    """
    # Queue stores tuples of (current_node, path_taken, total_cost)
    queue = deque([(start, [start], 0)])
    visited = set()

    nodes_expanded = 0

    while queue:
        current_node, path, cost = queue.popleft()
        nodes_expanded += 1

        if current_node == goal:
            return path, cost, nodes_expanded

        if current_node not in visited:
            visited.add(current_node)

            for neighbor, weight in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], cost + weight))

    return None, float('inf'), nodes_expanded

if __name__ == "__main__":
    start_node = 'L1'  # Main Gate
    goal_node = 'L4'   # Science Lab

    path, cost, expanded = bfs(CAMPUS_GRAPH, start_node, goal_node)
    
    path_named = " -> ".join([f"{node} ({LOCATION_NAMES[node]})" for node in path])
    print("=== Breadth-First Search (BFS) ===")
    print(f"Path Found:     {path_named}")
    print(f"Total Distance: {cost} km")
    print(f"Nodes Expanded: {expanded}")
