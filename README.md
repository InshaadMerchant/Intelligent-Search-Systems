# Intelligent-Search-Systems
This code was written as part of my CSE 4308 Artificial Intelligence class.

Name: Inshaad Merchant

ID: 1001861293


Language used: Python

Python Version: Python 3.9.13

For compilation and testing use: PyCharm

Omega Compatibility: No


How the code is structured:

1. parse_input: This function parses the input file containing information about the graph, extracting the source, destination, and distance between nodes, and constructs a dictionary representing the graph based on bidirectional connections.

2. breadth_first_search: This function performs breadth-first search (BFS) traversal on the graph, starting from the origin node and searching for the shortest path to the destination node. It utilizes a queue to explore nodes in layers and tracks the number of nodes popped, expanded, and generated during the traversal.

3. heuristic: This function provides a heuristic estimate of the distance from a given city to the destination, using a dictionary of heuristic values for each city.

4. a_star_search: This function implements the A* search algorithm to find the shortest path from the origin to the destination node in the graph. It utilizes a priority queue based on the sum of the actual cost and the heuristic estimate for each node, and tracks the number of nodes popped, expanded, and generated during the search.

5. print_route: This function prints the route obtained from either BFS or A* search, starting from the destination node and traversing back to the origin node, along with the corresponding distances between consecutive nodes.

6. main(): This function serves as the entry point of the program, parsing command-line arguments, reading input files, and invoking either BFS or A* search based on the presence of a heuristic file. It prints the counts of nodes popped, expanded, and generated, along with the shortest path and its distance obtained from the chosen search algorithm.


How to run the code: 

1. Decompress imm1293_assmt1.zip and open the source code in PyCharm. 

2. Move all the heuristic files and input file in the same folder as the source code.

3. Either press build and run on PyCharm.

4. Or, On the terminal, type "python find_route.py input1.txt Bremen Kassel" and press Enter for uninformed search.
   and type "python find_route.py input1.txt Bremen Kassel h_kassel.txt" and press Enter for informed search.
