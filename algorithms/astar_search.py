from heapq import heappush, heappop

class Node:
    """A node in a graph"""

    # How do we handle difference distance functions?

    def __init__(self, id, neighbors={}):
        self.id = id
        self.neighbors = neighbors
        self.previous = None
        self.shortest_distance = None

    def __str__(self):
        return f'id:{self.id}; previous:{self.previous}; shortest_distance:{self.shortest_distance}; neighbors:{self.neighbors}'

    def set_shortest_distance(self, node, sd):
        self.previous = node
        self.shortest_distance = sd



def astar_search(start, goal, heuristic):
    frontier = [start]
    visited = set()

    while frontier:
        current_node = heappop(frontier)

        if current_node == goal:
            # return path
            shortest_path = []
            n = current_node

            while n.previous:
                shortest_path.append(n)
                n = n.previous
            shortest_path.append(n)

            return shortest_path.reversed()

        for n in current_node.neighbors:
            if n not in visited:
                heappush(frontier, (heuristic(n) + n.shortest_distance, n))
        visited.add(current_node)

    return None
