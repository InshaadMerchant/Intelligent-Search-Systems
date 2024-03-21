import sys
import heapq


class Node:
    #Initializing variables
    def __init__(self, city, parent=None, distance=0):
        self.city = city
        self.parent = parent
        self.distance = distance


def parse_input(input_filename):
    graph = {}
    with open(input_filename, 'r') as file:
        for line in file:
            if line.strip() == "END OF INPUT":  #Checking for end of file
                break
            source, destination, distance = line.split()  #Parsing Input
            distance = float(distance)
            if source not in graph:
                graph[source] = []
            if destination not in graph:
                graph[destination] = []
            graph[source].append((destination, distance))
            graph[destination].append((source, distance))  # Assuming bidirectional connections
    return graph

def bfs(graph, origin, destination):
    queue = [Node(origin)]
    visited = set()
    generated_nodes = set()  # Track generated nodes to avoid double-counting
    np = 0
    ne = 0
    ng = 1  # Initial node is generated
    while queue:
        node = queue.pop(0)
        np += 1
        if node.city == destination:
            # Reconstruct the route
            route = []
            while node.parent:
                route.append((node.city, node.distance))
                node = node.parent
            route.append((origin, 0))
            route.reverse()
            return node, np, ne, ng, route
        visited.add(node.city)
        for neighbor, distance in graph.get(node.city, []):
            if neighbor not in visited and neighbor not in generated_nodes:
                queue.append(Node(neighbor, node, node.distance + distance))
                generated_nodes.add(neighbor)
                ng += 1
        ne += 1
    return None, np, ne, ng, []  # Return an empty route list

def a_star_search(graph, origin, destination, heuristic_dict):
    heap = [(0, origin)]
    visited = set()
    distances = {city: float('inf') for city in graph}
    distances[origin] = 0
    np = 0
    ne = 0
    ng = 1  # Initial node is generated
    parents = {}
    generated_nodes = set()

    while heap:
        _, city = heapq.heappop(heap)
        np += 1

        if city == destination:
            # Reconstruct the route
            route = []
            while city != origin:
                route.append((city, distances[city]))
                city = parents[city]
            route.append((origin, 0))
            route.reverse()
            return Node(destination), np, ne, ng, route

        if city in visited:
            continue

        visited.add(city)

        for neighbor, distance in graph.get(city, []):
            if neighbor not in visited:
                # Update distance if a better path is found
                new_distance = distances[city] + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    parents[neighbor] = city
                    if neighbor not in generated_nodes:
                        heapq.heappush(heap, (new_distance + heuristic(neighbor, destination, heuristic_dict), neighbor))
                        generated_nodes.add(neighbor)
                        ng += 1
        ne += 1  # Increment nodes_expanded after processing all neighbors

    return None, np, ne, ng, []

def heuristic(city, destination, heuristic_dict):
    return heuristic_dict.get(city, float('inf'))


def print_route(node):
    if node is None:
        print("None")
    else:
        route = []
        while node:
            route.append((node.city, node.distance))
            node = node.parent
        for i in range(len(route) - 1, 0, -1):
            print("{} to {}, {} km".format(route[i][0], route[i - 1][0], route[i - 1][1] - route[i][1]))


def main():
    if len(sys.argv) < 4:
        print("Usage: find_route input_filename origin_city destination_city [heuristic_filename]")
        sys.exit(1)

    input_file = sys.argv[1]
    origin = sys.argv[2]
    destination = sys.argv[3]

    graph = parse_input(input_file)
    heuristic_dict = {}
    if len(sys.argv) == 5:
        h_file = sys.argv[4]
        with open(h_file, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) == 2:
                    city, h_value = parts
                    heuristic_dict[city] = float(h_value)

    if heuristic_dict:
        result, popped, expanded, generated, route = a_star_search(graph, origin,
                                                                                     destination, heuristic_dict)
    else:
        result, popped, expanded, generated, route = bfs(graph, origin,
                                                                                            destination)

    print("Nodes Popped:", popped)
    print("Nodes Expanded:", expanded)
    print("Nodes Generated:", generated)

    if result is not None:

        if route:  # Check if the route list is not empty
            distance = route[-1][1]
            print("Distance:", distance, "km")
            print("Route:")
            for i in range(len(route) - 1):
                print("{} to {}, {} km".format(route[i][0], route[i + 1][0], route[i + 1][1] - route[i][1]))
        else:
            print("None")
    else:
        print("Distance: infinity")
        print("Route:")
        print("None")


if __name__ == "__main__":
    main()
